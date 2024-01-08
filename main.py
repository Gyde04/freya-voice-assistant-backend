# uvicorn main:app --reload
# uvicorn main:app

from typing import Union
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom Function Imports
from functions.openai_requests import convert_audio_to_text

# Initiate App
app = FastAPI()

# CORS - Origins
origins = [
    "http://127.0.0.1:8000",
    "https://localhost:5174",
    "https://localhost:4173",
    "https://localhost:3174",
    "https://localhost:3000"
]

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Check Health
@app.get("/health")
def check_health():
    return {"message": "healthy"}

# Get audio
@app.get("/post-audio-get/")
async def get_audio():

    try:
        # Get saved audio
        audio_input = open("voice.mp3", "rb")

        # Decode audio using convert_audio_to_text function
        message_decoded = convert_audio_to_text(audio_input)

        # Print decoded message
        print(message_decoded)

        return {"message": "Audio decoded successfully"}
    except Exception as e:
        print(f"Error decoding audio: {e}")
        raise HTTPException(status_code=500, detail="Error decoding audio")

# Define other endpoints (e.g., /items/{item_id})



# # Post bot response
# # Note: Not playing in brower when using post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):

#     return


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}