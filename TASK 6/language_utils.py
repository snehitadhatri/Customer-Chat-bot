from langdetect import detect
from transformers import pipeline
import random

# Multilingual Translation (using HuggingFace M2M100)
translator = pipeline("translation", model="facebook/m2m100_418M")

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

def translate_text(text, src, tgt):
    if src == tgt:
        return text
    result = translator(text, src_lang=src, tgt_lang=tgt)
    return result[0]['translation_text']

def get_response(user_input, lang, responses):
    # Normalize lang codes
    lang_map = {"en": "english", "es": "spanish", "fr": "french", "hi": "hindi"}
    lang_key = lang_map.get(lang, "english")

    if lang_key not in responses:
        lang_key = "english"

    possible_responses = responses[lang_key]
    return random.choice(possible_responses)
