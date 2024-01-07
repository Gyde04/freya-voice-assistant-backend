# uvicorn main:app --reload
# uvicorn main:app


from typing import Union

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom Funtion Imports
#

# Initiate App
app = FastAPI()


# CORS - Origins
origins = [
    "https://localhost:5173"
    "https://localhost:5174"
    "https://localhost:4173"
    "https://localhost:3174"
    "https://localhost:3000"
]

#CORS - Middleware
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

# # Post bot response
# # Note: Not playing in brower when using post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):

#     return


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}