from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from moodify_engine import MoodifyEngine
import cv2
import base64
import numpy as np
import uvicorn
import os

app = FastAPI()

# Global engine instance
engine = MoodifyEngine()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    img_data = data['image'].split(",")[1]
    
    # Convert base64 to opencv image
    nparr = np.frombuffer(base64.b64decode(img_data), np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Detect Emotion
    emotion, coords = engine.detect_emotion(frame)
    if not emotion:
        return {"error": "No face detected"}
    
    # Coordinates for drawing box on frontend
    x, y, w, h = [int(v) for v in coords]
    
    # Get Weather
    weather = engine.get_weather()
    
    # Get Recommendation
    song_name, details = engine.get_recommendation(emotion, weather)
    spotify_url = engine.search_spotify(song_name)
    
    return {
        "emotion": emotion.capitalize(),
        "weather": weather.replace("-", " ").capitalize(),
        "song": song_name,
        "spotify_url": spotify_url,
        "genre": details['genre'],
        "mechanism": details['mechanism'],
        "box": {"x": x, "y": y, "w": w, "h": h}
    }

if __name__ == "__main__":
    if not os.path.exists("templates"):
        os.makedirs("templates")
    uvicorn.run(app, host="0.0.0.0", port=8000)
