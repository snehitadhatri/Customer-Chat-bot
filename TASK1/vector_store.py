import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.index_path = "models/faiss_index.bin"
        self.vectorizer_path = "models/vectorizer.pkl"
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.load_index()

    def load_index(self):
        try:
            self.index = faiss.read_index(self.index_path)
            with open(self.vectorizer_path, "rb") as f:
                self.docs = pickle.load(f)
        except:
            self.index = faiss.IndexFlatL2(384)
            self.docs = []

    def save_index(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.vectorizer_path, "wb") as f:
            pickle.dump(self.docs, f)

    def add_document(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
        embedding = self.model.encode([text])
        self.index.add(np.array(embedding, dtype="float32"))
        self.docs.append(text)
        self.save_index()

    def search(self, query, top_k=2):
        if len(self.docs) == 0:
            return None
        embedding = self.model.encode([query])
        D, I = self.index.search(np.array(embedding, dtype="float32"), top_k)
        return "\n".join([self.docs[i] for i in I[0]])
