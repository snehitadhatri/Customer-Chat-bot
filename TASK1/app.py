import streamlit as st
from utils.chatbot_logic import get_chatbot_response, load_faiss_index

st.set_page_config(page_title="Gen AI Customer Support Bot", layout="centered")
st.title("💬 Real-Time Gen AI Customer Support Bot")

# Load FAISS index
index, embeddings = load_faiss_index()

# Chat session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    role = "🤖 Bot" if message["role"] == "bot" else "🧑 You"
    st.markdown(f"**{role}:** {message['content']}")

# User input
user_input = st.text_input("Type your question:")

if st.button("Send") and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input})
    bot_reply = get_chatbot_response(user_input, index, embeddings)
    st.session_state.messages.append({"role": "bot", "content": bot_reply})
    st.experimental_rerun()
