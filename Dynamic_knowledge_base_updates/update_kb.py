from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle

data_path = "knowledge_base"
index_path = "faiss_index"
model = SentenceTransformer("all-MiniLM-L6-v2")

def load_documents():
    docs = []
    for filename in os.listdir(data_path):
        with open(os.path.join(data_path, filename), "r", encoding="utf-8") as f:
            docs.append(f.read())
    return docs

def build_vector_store():
    docs = load_documents()
    embeddings = model.encode(docs)
    
    index = faiss.IndexFlatL2(384)
    index.add(embeddings)
    os.makedirs(index_path, exist_ok=True)

    faiss.write_index(index, f"{index_path}/kb.index")
    with open(f"{index_path}/docs.pkl", "wb") as f:
        pickle.dump(docs, f)

if __name__ == "__main__":
    build_vector_store()

