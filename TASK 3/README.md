# MedQuAD — Medical Q\&A Chatbot

This repository contains an implementation of a **medical question-answering chatbot** using the [MedQuAD dataset](https://github.com/abachaa/MedQuAD). The chatbot retrieves relevant answers from the dataset, performs basic medical entity recognition, and provides an interactive **Streamlit-based interface**.

⚠️ **Disclaimer:** This system is intended for **educational and research purposes only**. It is **not** a substitute for professional medical advice.

---

## 🚀 Features

* Retrieval-based QA using **TF-IDF + Nearest Neighbors**
* Basic medical entity recognition (symptoms, diseases, treatments)
* Streamlit user interface for asking medical questions
* Simple and extensible code structure

---

## 📂 Project Structure

```
MedQuAD-MedQA/
├─ data/                      # Place MedQuAD XML files here
├─ models/                    # Saved vectorizer, index, and QA table
│  ├─ vectorizer.pkl
│  ├─ nn_index.pkl
│  └─ qa_table.csv
├─ app.py                     # Streamlit app
├─ build_index.py             # Parse dataset + build index
├─ utils.py                   # Helper functions (retrieval, NER)
├─ requirements.txt           # Dependencies
└─ README.md                  # Documentation
```

---

## 🔧 Installation & Setup

1. **Clone this repository** and the MedQuAD dataset:

   ```bash
   git clone https://github.com/abachaa/MedQuAD
   git clone <this-repo-url>
   cd MedQuAD-MedQA
   ```

2. **Create a virtual environment** and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Build the index** (parse MedQuAD XML and save models):

   ```bash
   python build_index.py --data_folder path/to/MedQuAD --out_dir models
   ```

4. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser (default: [http://localhost:8501](http://localhost:8501)).

---

## 🎯 Usage

* Enter a medical question in the text box.
* The app will:

  * Detect basic **medical entities** (symptoms, diseases, treatments)
  * Retrieve **top answers** from the MedQuAD dataset
  * Display **sources (URLs)** when available

---

## 🛠️ Future Improvements

* Replace TF-IDF with **Sentence-BERT embeddings + FAISS** for semantic retrieval
* Integrate **scispaCy / medSpaCy** for high-quality medical NER
* Implement **re-ranking** with cross-encoders for better answer selection
* Add **logging & analytics** to monitor user queries

---
### 🧑‍💻 Author
* Name: Snehita Dhatri
* Internship Role: AI Developer Intern
* Organization: NullClass

---
## 📜 License
This is for educational purpose only
Please refer to the original [MedQuAD dataset license](https://github.com/abachaa/MedQuAD).
