import openai
from decouple import config

# Retrieve Environment Variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# Open AI - Whisper
# Convert Audio to Text

def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        # Check if the transcript is not None and contains 'text' attribute
        if transcript and "text" in transcript:
            message_text = transcript["text"]
            return message_text
        else:
            print("Transcript is empty or missing 'text' attribute")
            return None
    except Exception as e:
        print(f"Error occurred during audio transcription: {e}")
        return None
