from sentence_transformers import SentenceTransformer
import faiss
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("faiss_index/kb.index")

with open("faiss_index/docs.pkl", "rb") as f:
    docs = pickle.load(f)

def search_knowledge_base(query):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k=1)
    return docs[indices[0][0]]

# Example:
query = input("Ask me anything: ")
response = search_knowledge_base(query)
print("🤖 Answer:\n", response)
