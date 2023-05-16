#nlp module
import spacy
import json

def extract_keyword_and_language(input_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_text)
    
    common_words = ["a", "an", "the", "of", "is", "are", "what", "give", "me"]
    
    keyword = None
    is_meaning_found = False
    for token in doc:
        if token.text.lower() == "meaning":
            is_meaning_found = True
        elif is_meaning_found and token.pos_ in ["NOUN", "PROPN"] and token.text.lower() not in common_words:
            keyword = token.text
            break
    
    result = {
        "keyword": keyword,
        "source_language": "English"
    }
    
    return json.dumps(result)

# Example usage
input_text = "Give me the meaning of Computer"
output = extract_keyword_and_language(input_text)
print(output)


***********************************************************
# meaning module
import requests
from bs4 import BeautifulSoup

def search_word_definition(word):
    url = f"https://www.merriam-webster.com/dictionary/{word}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    definition = soup.find(class_="dtText").get_text().strip()
    return definition

word = "Machine-Learning"
definition = search_word_definition(word)
print(f"Definition of '{word}': {definition}")



*******************************************************
#translation module

import requests
import uuid


def translate_text(source_lang, target_lang, text):
    subscription_key = 'b7804aadaccf4b1b97885bedd28fb9a6'
    endpoint = 'https://api.cognitive.microsofttranslator.com/translate'
    location = "centralindia"
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    params = {
        'api-version': '3.0',
        'from': source_lang,
        'to': target_lang
    }
    body = [{
        'text': text
    }]
    response = requests.post(endpoint, headers=headers,
                             params=params, json=body)
    if response.status_code != 200:
        return 'Error: ' + str(response.status_code)
    else:
        return response.json()[0]['translations'][0]['text']


print(translate_text("en", "hi", "the process by which a computer is able to improve its own performance (as in analyzing image files) by continuously incorporating new data into an existing statistical model"))


*********************************
#play music at google colab
from IPython.display import Audio

audio_file_path = '/content/output.mp3'  # Replace with the actual path to your audio file

Audio(audio_file_path)
