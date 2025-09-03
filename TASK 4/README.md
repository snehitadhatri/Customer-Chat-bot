# ArXiv CS Expert Chatbot

An interactive chatbot built with **Streamlit**, powered by embeddings from **arXiv Computer Science papers**. The chatbot can:

* Retrieve and search papers from the arXiv CS subset.
* Summarize abstracts and sections.
* Explain complex concepts using an open-source LLM.
* Maintain conversation history for follow-up questions.
* Visualize key concepts as interactive graphs.

---

## 🚀 Features

* **Paper Search**: Semantic search using FAISS + Sentence Transformers.
* **Summarization**: Condenses abstracts into concise summaries.
* **Explanations**: Generates human-friendly answers with a local or remote LLM.
* **Conversational Memory**: Handles multi-turn Q\&A with context.
* **Visualization**: Extracts and displays concepts with interactive networks.

---

## 📂 Project Structure

```
ArXiv-CS-Expert-Chatbot/
│
├── src/
│   ├── app.py                # Streamlit application (main UI)
│   ├── retriever.py          # FAISS retriever logic
│   ├── summarizer.py         # Summarization module
│   ├── explain_generator.py  # LLM-based explanation generator
│   ├── visualization.py      # Concept extraction + graph visualization
│   └── data_processing.py    # Preprocessing pipeline for arXiv data
│
├── models/
│   └── local_llm_config.json # Configuration for local Hugging Face / GPTQ model
│
├── notebooks/
│   └── build_embeddings.ipynb # Build embeddings + FAISS index
│
├── data/
│   ├── arxiv_subset.csv      # Preprocessed arXiv CS dataset
│   └── faiss_index/          # FAISS index + metadata
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ArXiv-CS-Expert-Chatbot.git
cd ArXiv-CS-Expert-Chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Build FAISS index

Run the notebook to generate embeddings:

```bash
jupyter notebook notebooks/build_embeddings.ipynb
```

This will create:

* `data/faiss_index/index.faiss`
* `data/faiss_index/index.pkl`

### 4. Run the chatbot

```bash
streamlit run src/app.py
```

---

## 🔍 Usage

* Enter a query in the text box (e.g., *“What is graph neural network?”*).
* The retriever fetches relevant papers.
* Summaries of abstracts are displayed.
* Explanations are generated using a local or remote LLM.
* You can add papers to **context** to refine answers.
* Ask follow-up questions to continue the conversation.
* Explore concepts with interactive visualizations.

---

## 🧠 Configuration

The chatbot supports both **local** and **remote** LLMs. Configure local models in:

```
models/local_llm_config.json
```

Example:

```json
{
  "model_name": "TheBloke/Llama-2-7B-GGML",
  "backend": "transformers",
  "device": "cuda",
  "max_new_tokens": 512,
  "temperature": 0.7
}
```

---

## 📊 Requirements

```
streamlit
pandas
faiss-cpu
sentence-transformers
transformers
torch
networkx
pyvis
jupyter
```

---

## ✅ Next Steps

* Extend to full-text PDF parsing with **PyMuPDF**.
* Deploy on Docker with GPU inference.
* Expand dataset beyond CS to Physics, Math, etc.
* Improve summarization with larger models (e.g., `bart-large-cnn`).

---

### 🧑‍💻 Author
* Name: Snehita Dhatri
* Internship Role: AI Developer Intern
* Organization: NullClass
---

### 📜 License
This project is for academic and internship use only.
