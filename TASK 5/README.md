# 🧠 Sentiment-Aware Customer Support Chatbot

This project is part of the **Nullclass Internship (Task 5)**.  
The chatbot integrates **sentiment analysis** into customer interactions, allowing it to recognize emotions (positive, negative, neutral) and respond empathetically.

---

### 🚀 Features
- Real-time customer interaction via **Streamlit UI**
- Sentiment detection using **TF-IDF + Logistic Regression**
- Predefined empathetic responses for:
  - 😊 Positive
  - 😔 Negative
  - 😐 Neutral
- Saves trained model (`sentiment_model.pkl`) and vectorizer (`vectorizer.pkl`)
- Extensible with more datasets and advanced models

---

### 📂 Folder Structure
```
TASK 5/
│── app.py # Streamlit UI for chatbot
│── sentiment_model.pkl # Trained sentiment model
│── vectorizer.pkl # TF-IDF vectorizer
│── responses.json # Predefined chatbot responses
│── train_sentiment.ipynb # Training notebook for sentiment model
│── requirements.txt # Dependencies
│── README.md # Project documentation
|── sentiment_data.csv #Sample dataset
```
---


---

### ⚙️ Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/sentiment_chatbot.git
   cd sentiment_chatbot
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Train the model :
   ```bash
   jupyter notebook train_sentiment.ipynb
4. Run the chatbot:
   ```bash
   streamlit run app.py

### 🎯 Usage

* Type a message in the input box.
* The chatbot will:
  1. Detect sentiment (positive/negative/neutral).
  2. Reply with an empathetic response.
* Sentiment detection is displayed along with the response.

### 🧪 Example Interaction

  You: "I’m really upset with the service."
  Bot: "I’m sorry you feel this way 😔. Let me try to resolve this for you. (Detected: negative)"

  You: "This is great, thank you!"
  Bot: "I’m glad to hear that! 😊 How else can I assist you? (Detected: positive)"

### 📊 Evaluation Criteria
* Accuracy of sentiment detection
* Appropriateness of chatbot responses
* Customer satisfaction during simulated interactions

### 🔮 Future Improvements
* Use pretrained transformers (BERT, RoBERTa) for sentiment detection
* Add multi-language support
* Personalize empathetic responses based on context

### 🧑‍💻 Author
* Name: Snehita Dhatri
* Internship Role: Data Science Intern
* Organization: NullClass

### 📜 License
This project is for academic and internship use only.
