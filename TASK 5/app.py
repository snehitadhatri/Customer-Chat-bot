import streamlit as st
import random
import json
import pickle

# Load sentiment model & vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Load responses
with open("responses.json") as f:
    responses = json.load(f)

# Function for sentiment detection
def detect_sentiment(user_input):
    vec = vectorizer.transform([user_input])
    return model.predict(vec)[0]

# Get chatbot response
def get_response(user_input):
    sentiment = detect_sentiment(user_input)
    reply = random.choice(responses[sentiment])
    return reply, sentiment

# Streamlit UI
st.title("🧠 Sentiment-Aware Customer Support Chatbot")
st.write("This chatbot adjusts responses based on your emotions.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    reply, sentiment = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", f"{reply} (Detected: {sentiment})"))

# Display chat history
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**{sender}:** {msg}")
    else:
        st.markdown(f"**{sender}:** {msg}")
