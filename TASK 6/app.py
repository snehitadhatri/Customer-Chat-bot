import streamlit as st
from language_utils import detect_language, translate_text, get_response
import json

# Load responses
with open("responses.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

st.set_page_config(page_title="Multilingual Chatbot", layout="centered")
st.title("🌍 Multilingual GenAI Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("💬 Say something:")

if user_input:
    # Detect user language
    lang = detect_language(user_input)

    # Process response
    bot_response = get_response(user_input, lang, responses)

    # Save history
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", bot_response))

# Display chat
for speaker, message in st.session_state.history:
    st.markdown(f"**{speaker}:** {message}")
