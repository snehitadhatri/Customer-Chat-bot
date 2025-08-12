import streamlit as st
import pickle
import faiss
import os
import json
from knowledge_base import add_document, search_query
from chatbot_logic import generate_response

# Load model & vectorizer
with open("chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load FAISS index
if os.path.exists("faiss_index.index"):
    index = faiss.read_index("faiss_index.index")
else:
    index = None

# Streamlit UI
st.set_page_config(page_title="Real-Time GenAI Customer Support Bot", layout="wide")
st.title("🤖 Real-Time GenAI Customer Support Bot")

# File upload section
uploaded_file = st.file_uploader("📂 Upload a .txt or .pdf document to expand knowledge base", type=["txt", "pdf"])
if uploaded_file is not None:
    add_document(uploaded_file)
    st.success("✅ Knowledge base updated with uploaded file!")

# Chat section
user_input = st.text_input("💬 Ask your question:")
if st.button("Send"):
    if user_input.strip():
        faiss_result = search_query(user_input)
        bot_response = generate_response(user_input, faiss_result)
        st.markdown(f"**Bot:** {bot_response}")
