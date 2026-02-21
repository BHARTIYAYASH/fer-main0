import cv2
import numpy as np
import tensorflow as tf
import os

# Mapping of emotion classes
EMOTIONS = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear', 'contempt']

# Path to the TFLite model
MODEL_PATH = os.path.join('model', 'ferplus_model_pd_best.tflite')

def main():
    # Load TFLite model and allocate tensors
    try:
        interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
        interpreter.allocate_tensors()
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Load the Haar cascade for face detection
    # Try to find it in opencv data folder automatically
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    if face_cascade.empty():
        print("Error: Could not load face cascade.")
        return

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting real-time emotion recognition. Press 'q' to quit.")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(48, 48))

        for (x, y, w, h) in faces:
            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Preprocess the face for the model
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48))
            
            # Normalize pixel values
            roi_normalized = roi_gray.astype('float32') / 255.0
            
            # Prepare input data (add batch and channel dimensions)
            input_data = np.expand_dims(roi_normalized, axis=0) # (1, 48, 48)
            input_data = np.expand_dims(input_data, axis=-1)   # (1, 48, 48, 1)

            # Set the tensor to point to the input data to be inferred
            interpreter.set_tensor(input_details[0]['index'], input_data)

            # Run inference
            interpreter.invoke()

            # Get the result
            output_data = interpreter.get_tensor(output_details[0]['index'])
            prediction_idx = np.argmax(output_data[0])
            emotion = EMOTIONS[prediction_idx]
            confidence = output_data[0][prediction_idx]

            # Label the frame with prediction
            label = f"{emotion} ({confidence*100:.1f}%)"
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Facial Emotion Recognition', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
