import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle
from tqdm import tqdm


EMB_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'




def load_and_filter(csv_path, categories_prefix='cs'):
df = pd.read_csv(csv_path)
# Some datasets use 'categories' or 'category'
col = 'categories' if 'categories' in df.columns else 'category'
df = df[df[col].str.contains(categories_prefix, na=False)]
df = df.reset_index(drop=True)
return df




def build_faiss_index(df, text_field='abstract', emb_model_name=EMB_MODEL, out_dir='data/faiss_index'):
os.makedirs(out_dir, exist_ok=True)
model = SentenceTransformer(emb_model_name)
texts = df[text_field].fillna('').tolist()
batch_size = 256
embeddings = []
for i in tqdm(range(0, len(texts), batch_size), desc='Embedding batches'):
batch = texts[i:i+batch_size]
emb = model.encode(batch, show_progress_bar=False)
embeddings.append(emb)
embeddings = np.vstack(embeddings).astype('float32')
dim = embeddings.shape[1]
index = faiss.IndexFlatIP(dim)
faiss.normalize_L2(embeddings)
index.add(embeddings)
faiss.write_index(index, os.path.join(out_dir, 'index.faiss'))
with open(os.path.join(out_dir, 'metadata.pkl'), 'wb') as f:
pickle.dump(df.to_dict(orient='records'), f)
print('Saved FAISS index and metadata')




if __name__ == '__main__':
df = load_and_filter('data/arxiv_subset.csv')
build_faiss_index(df)
