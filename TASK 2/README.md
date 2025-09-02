# 🤖 Multi-Modal Chatbot (Text + Image with Gemini AI)

This project is part of my **Nullclass Internship – Task 2**.  
It extends a customer support chatbot to handle **text + image queries** using **Google Gemini AI**.  

---

## 🚀 Features
- ✅ **Text Conversations** – Chat with AI in real time.  
- ✅ **Image Understanding** – Upload an image and get AI analysis.  
- ✅ **Image Generation (Simulated)** – Create placeholder images based on prompts.  
- ✅ **Streamlit UI** – Clean, interactive interface.  

---

## 📂 Project Structure
TASK 2/
│── app.py # Main Streamlit app
│── gemini_client.py # Gemini API calls
│── responses.json # Predefined fallback/greetings
│── requirements.txt # Dependencies
│── README.md # Documentation
│── prompts/
│ └── system_prompt.txt

└── system_prompt.txt

---

## ⚙️ Installation & Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/multimodal_chatbot.git
   cd multimodal_chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Gemini API Key in gemini_client.py:
   ```python
   genai.configure(api_key="YOUR_API_KEY_HERE")
   ```

4. Run the chatbot:
   ```bash
   streamlit run app.py
   ```

## 📝 Notes
Gemini currently understands images but does not generate images (that’s handled by Google Imagen).
In this repo, image generation is simulated with a placeholder output.

## 📌 Expected Outcome
A chatbot that:
Understands user queries (text + image)
Generates relevant responses
Provides an interactive Streamlit UI
