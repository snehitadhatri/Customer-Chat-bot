import streamlit as st
from chatbot import ChatBot
from utils import save_uploaded_file

# Initialize chatbot
bot = ChatBot()

st.set_page_config(page_title="Real-Time Gen AI Customer Support Bot", layout="wide")
st.title("🤖 Real-Time Gen AI Customer Support Bot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Upload new files to knowledge base
uploaded_file = st.file_uploader("📂 Upload file to expand knowledge base", type=["txt", "pdf"])
if uploaded_file:
    file_path = save_uploaded_file(uploaded_file, "data/new_uploads")
    bot.update_knowledge_base(file_path)
    st.success("✅ Knowledge base updated successfully!")

# Display chat
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your query..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.spinner("Thinking..."):
        response = bot.get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
