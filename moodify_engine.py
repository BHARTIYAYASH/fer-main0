import os
import cv2
import numpy as np
import tensorflow as tf
import requests
from dotenv import load_dotenv
from song_dictionary import SONG_DICTIONARY, infer_weather_key_from_ambee

# Load environment variables
load_dotenv()

AMBEE_API_KEY = os.getenv("AMBEE_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Mapping of emotion classes (Match index to name)
EMOTIONS = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear', 'contempt']

class MoodifyEngine:
    def __init__(self):
        # Load TFLite model
        model_path = os.path.join('model', 'ferplus_model_pd_best.tflite')
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        
        # Load Face Cascade
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        self.spotify_token = self._get_spotify_token()
        
        # Weather Cache
        self.weather_cache = None
        self.last_weather_update = 0
        self.weather_cache_duration = 600 # 10 minutes (600 seconds)

    def _get_spotify_token(self):
        """Get Spotify access token using Client Credentials Flow"""
        auth_url = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'client_credentials',
            'client_id': SPOTIFY_CLIENT_ID,
            'client_secret': SPOTIFY_CLIENT_SECRET,
        }
        res = requests.post(auth_url, data=data)
        if res.status_code == 200:
            return res.json()['access_token']
        return None

    def get_weather(self, lat="18.5204", lng="73.8567"): # Default to Pune
        """Get weather from Ambee API with 10-minute caching"""
        import time
        current_time = time.time()
        
        # If we have a fresh cache, use it
        if self.weather_cache and (current_time - self.last_weather_update < self.weather_cache_duration):
            return self.weather_cache

        url = f"https://api.ambeedata.com/weather/latest/by-lat-lng?lat={lat}&lng={lng}"
        headers = {'x-api-key': AMBEE_API_KEY, 'Content-type': 'application/json'}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json().get('data', {})
                weather_key = infer_weather_key_from_ambee(data)
                
                # Update cache
                self.weather_cache = weather_key
                self.last_weather_update = current_time
                return weather_key
        except Exception as e:
            print(f"Weather API Error: {e}")
        
        return self.weather_cache if self.weather_cache else "any"

    def detect_emotion(self, frame):
        """Detect dominant emotion from a frame"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) == 0:
            return None, None
            
        (x, y, w, h) = faces[0]
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        roi_normalized = roi_gray.astype('float32') / 255.0
        
        input_data = np.expand_dims(roi_normalized, axis=(0, -1))
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
        prediction_idx = np.argmax(output_data[0])
        return EMOTIONS[prediction_idx], (x, y, w, h)

    def search_spotify(self, song_name):
        """Find the Spotify URL for a song"""
        url = f"https://api.spotify.com/v1/search?q={song_name}&type=track&limit=1"
        headers = {"Authorization": f"Bearer {self.spotify_token}"}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            items = res.json().get('tracks', {}).get('items', [])
            if items:
                return items[0]['external_urls']['spotify']
        return f"https://open.spotify.com/search/{song_name}"

    def get_recommendation(self, emotion, weather):
        """Pick a song from the dictionary based on mood and weather"""
        emotion_dict = SONG_DICTIONARY.get(emotion, SONG_DICTIONARY['neutral'])
        rec = emotion_dict.get(weather, emotion_dict['any'])
        import random
        song = random.choice(rec['tracks'])
        return song, rec

if __name__ == "__main__":
    # Test Run
    engine = MoodifyEngine()
    print("Engine Initialized.")
    weather = engine.get_weather()
    print(f"Current weather key: {weather}")
