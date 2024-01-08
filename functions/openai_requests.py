import openai
from decouple import config

# Retrieve Enviroment Variables
open.organization = config("OPEN_AI_ORG")
open.api_key = config("OPEN_AI_KEY")

# Open AI - Whisper
# Convert Audio to Text

def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript("text")
        return message_text
    except Exception as e:
        print(e)
        return
