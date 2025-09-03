import faiss
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from PyPDF2 import PdfReader

# Load or create vectorizer
if os.path.exists("vectorizer.pkl"):
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
else:
    vectorizer = TfidfVectorizer(stop_words="english")

# Load FAISS index
if os.path.exists("faiss_index.index"):
    index = faiss.read_index("faiss_index.index")
    with open("kb_data.pkl", "rb") as f:
        kb_data = pickle.load(f)
else:
    index = None
    kb_data = []

def add_document(file):
    global index, kb_data, vectorizer
    if file.name.endswith(".txt"):
        text = file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        pdf = PdfReader(file)
        text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    else:
        return
    
    kb_data.append(text)
    vectors = vectorizer.fit_transform(kb_data).toarray().astype("float32")
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    faiss.write_index(index, "faiss_index.index")
    with open("vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    with open("kb_data.pkl", "wb") as f:
        pickle.dump(kb_data, f)

def search_query(query):
    global index, vectorizer, kb_data
    if index is None or not kb_data:
        return []
    query_vector = vectorizer.transform([query]).toarray().astype("float32")
    distances, indices = index.search(query_vector, k=3)
    return [kb_data[i] for i in indices[0] if i < len(kb_data)]
