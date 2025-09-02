import streamlit as st
from gemini_client import get_text_response, analyze_image, generate_image

st.set_page_config(page_title="Multi-Modal Chatbot", layout="wide")
st.title("🤖 Multi-Modal Chatbot (Text + Image with Gemini)")

# Chat input
user_input = st.text_input("💬 Ask me anything...")

# Image upload
uploaded_file = st.file_uploader("📷 Upload an image", type=["jpg", "png", "jpeg"])

if user_input:
    if "generate image" in user_input.lower():
        filename = generate_image(user_input)
        st.image(filename, caption="🖼️ Generated Image")
        st.success("✅ Image generated successfully!")
    else:
        reply = get_text_response(user_input)
        st.markdown(f"**🤖 Bot:** {reply}")

if uploaded_file is not None:
    with open("temp.png", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image("temp.png", caption="📷 Uploaded Image")
    response = analyze_image("temp.png", user_prompt=user_input or "Describe this image.")
    st.markdown(f"**🤖 Bot (Image Analysis):** {response}")
