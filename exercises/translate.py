import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.sunbird.ai/tasks/nllb_translate"
access_token = os.getenv("AUTH_TOKEN")
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

accepted_strings = ["English", "Luganda", "Runyankole", "Ateso", "Lugbara", "Acholi"]

def get_source_and_target():
    source_language = input("Please choose the source language: (one of English, Luganda, Runyankole, Ateso, Lugbara or  Acholi: ")
    while source_language not in accepted_strings:
        print("Please input a valid language")
        source_language = input("Please choose the source language: (one of English, Luganda, Runyankole, Ateso, Lugbara or  Acholi: ")

    target_language = input("Please choose the target language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi: ")
    while target_language not in accepted_strings:
        print("Please input a valid language")
        target_language = input("Please choose the target language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi: ")

    return [source_language, target_language]

source_and_target = get_source_and_target()
text_to_translate = input("Enter the text to translate: ")

interpreter = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Ateso": "teo",
    "Lugbara": "lgg",
    "Acholi": "ach"
}

data = {
    "source_language": interpreter[source_and_target[0]],
    "target_language": interpreter[source_and_target[1]],
    "text": text_to_translate
}

response = requests.post(url, headers=headers, json=data)

response_result = response.json()
print(response_result['output']['translated_text'])

