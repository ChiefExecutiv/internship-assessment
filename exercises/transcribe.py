import os
import requests
from dotenv import load_dotenv
from mutagen import File

load_dotenv()

url = "https://api.sunbird.ai/tasks/stt"
access_token = os.getenv("AUTH_TOKEN")
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}",
}

accepted_strings = ["English", "Luganda", "Runyankole", "Ateso", "Lugbara", "Acholi"]


def is_audio_duration_valid(audio_path, max_minutes=5):
    try:
        audio = File(audio_path)
        if audio is None or not hasattr(audio.info, 'length'):
            print("Can't read duration.")
            return False
        duration_seconds = audio.info.length
        return duration_seconds <= max_minutes * 60
    except Exception as e:
        print(f"Error reading audio duration: {e}")
        return False

def get_audio_input():
    while True:
        audio_input = input("Please provide path to the audio file (Audio length less than 5 minutes): ")
        if not os.path.exists(audio_input):
            print("Path does not exist. Please try again.")
            continue
        if not is_audio_duration_valid(audio_input):
            print("Please provide a shorter file. (less than 5 minutes)")
            continue
        return audio_input


def get_target_language():
    target_language = input("Please choose the target language (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi): ")
    while target_language not in accepted_strings:
        print("Invalid input! Please select one of the listed languages.")
        target_language = input("Please choose the target language (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi): ")
    return target_language

interpreter = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Ateso": "teo",
    "Lugbara": "lgg",
    "Acholi": "ach"
}

audio_path = get_audio_input()
target_language = get_target_language()

with open(audio_path, "rb") as audio_file:
    files = {
        "audio": (
            os.path.basename(audio_path),
            audio_file,
            "audio/mpeg",
        ),
    }
    data = {
        "language": interpreter[target_language],
        "adapter": interpreter[target_language],
        "whisper": True,
    }

    response = requests.post(url, headers=headers, files=files, data=data)

    response_result = response.json()
    print(f"Audio transcription text in {target_language}:\n")
    print(response_result.get("audio_transcription", ""))
