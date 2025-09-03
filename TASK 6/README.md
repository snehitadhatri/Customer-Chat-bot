# 🌍 Multilingual GenAI Chatbot

## 🚀 Features
- Supports **English, Spanish, French, Hindi**
- Automatic **language detection** with `langdetect`
- **Seamless switching** between languages
- Uses HuggingFace `facebook/m2m100_418M` for translation
- Provides **culturally appropriate responses**
- Built with **Streamlit** UI

## 📂 Project Structure
```
multilingual_chatbot/
│── app.py
│── language_utils.py
│── responses.json
│── requirements.txt
│── README.md
│── models/
│ ├── chatbot_model.pkl
│ ├── vectorizer.pkl
│── notebooks/
│ ├── train_model.ipynb
```


## ⚙️ Installation
```bash
git clone https://github.com/yourusername/multilingual_chatbot.git
cd multilingual_chatbot
pip install -r requirements.txt
```
## ▶️ Run
```bash
streamlit run app.py
```
## 🌐 Languages Supported
* English
* Spanish
* French
* Hindi

## 📖 Future Enhancements
Add more languages
Use LLM-based contextual answers
Improve cultural adaptation

## 🧑‍💻 Author
* Name: Snehita Dhatri
* Internship Role: AI Developer Intern
* Organization: NullClass

### 📜 License
This project is for academic and internship use only.

