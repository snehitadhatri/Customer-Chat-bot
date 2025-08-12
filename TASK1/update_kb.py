import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"
FAISS_INDEX_PATH = "models/faiss_index.index"
EMBEDDINGS_PATH = "models/embeddings.pkl"
KB_FILE = "data/knowledge_base.txt"

def update_knowledge_base(new_text):
    model = SentenceTransformer(MODEL_NAME)
    vector = model.encode([new_text])
    
    index = faiss.read_index(FAISS_INDEX_PATH)
    with open(EMBEDDINGS_PATH, "rb") as f:
        embeddings = pickle.load(f)
    
    index.add(np.array(vector).astype("float32"))
    embeddings.append({"text": new_text})
    
    faiss.write_index(index, FAISS_INDEX_PATH)
    with open(EMBEDDINGS_PATH, "wb") as f:
        pickle.dump(embeddings, f)

    with open(KB_FILE, "a") as f:
        f.write("\n" + new_text)

if __name__ == "__main__":
    text = input("Enter new knowledge base text: ")
    update_knowledge_base(text)
    print("✅ Knowledge base updated successfully.")
