import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"
FAISS_INDEX_PATH = "models/faiss_index.index"
EMBEDDINGS_PATH = "models/embeddings.pkl"

def load_faiss_index():
    index = faiss.read_index(FAISS_INDEX_PATH)
    with open(EMBEDDINGS_PATH, "rb") as f:
        embeddings = pickle.load(f)
    return index, embeddings

def get_chatbot_response(query, index, embeddings):
    model = SentenceTransformer(MODEL_NAME)
    query_vector = model.encode([query])
    D, I = index.search(np.array(query_vector).astype("float32"), k=1)
    return embeddings[I[0][0]]["text"]
