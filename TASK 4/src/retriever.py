import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer


class Retriever:
def __init__(self, index_path='data/faiss_index/index.faiss', meta_path='data/faiss_index/metadata.pkl', emb_model='sentence-transformers/all-MiniLM-L6-v2'):
self.index = faiss.read_index(index_path)
with open(meta_path, 'rb') as f:
self.metadata = pickle.load(f)
self.model = SentenceTransformer(emb_model)


def search(self, query, top_k=5):
q_emb = self.model.encode([query])
faiss.normalize_L2(q_emb)
D, I = self.index.search(np.array(q_emb).astype('float32'), top_k)
results = []
for idx, score in zip(I[0], D[0]):
meta = self.metadata[idx]
meta['_score'] = float(score)
results.append(meta)
return results
