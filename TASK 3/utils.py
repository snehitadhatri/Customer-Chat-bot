import pickle
import os
import re
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity




def load_models(models_dir='models'):
with open(os.path.join(models_dir, 'vectorizer.pkl'), 'rb') as f:
vectorizer = pickle.load(f)
with open(os.path.join(models_dir, 'nn_index.pkl'), 'rb') as f:
nn_blob = pickle.load(f)
qa = pd.read_csv(os.path.join(models_dir, 'qa_table.csv'))
return vectorizer, nn_blob['nn'], qa




def retrieve_answers(query, vectorizer, nn, qa_table, topk=3):
doc = query
qv = vectorizer.transform([doc])
distances, idx = nn.kneighbors(qv, n_neighbors=topk)
# distances are cosine distances (0 best)
results = []
for d,i in zip(distances[0], idx[0]):
score = 1 - d
row = qa_table.iloc[i].to_dict()
row.update({'score': float(score)})
results.append(row)
return results




# Very simple keyword-based medical entity recognition
SYMPTOM_KEYWORDS = [
'fever','cough','fatigue','nausea','headache','pain','shortness of breath','vomit','dizziness'
]
DISEASE_KEYWORDS = [
'diabetes','hypertension','cancer','asthma','covid','influenza','tuberculosis','arthritis'
]
TREATMENT_KEYWORDS = [
'surgery','chemotherapy','radiation','antibiotic','antiviral','therapy','vaccine','insulin'
]




def extract_medical_entities(text):
t = text.lower()
entities = {'symptoms':set(), 'diseases':set(), 'treatments':set()}
for kw in SYMPTOM_KEYWORDS:
if kw in t:
entities['symptoms'].add(kw)
for kw in DISEASE_KEYWORDS:
if kw in t:
entities['diseases'].add(kw)
for kw in TREATMENT_KEYWORDS:
if kw in t:
entities['treatments'].add(kw)
# simple dates/measurements extraction (example)
numbers = re.findall(r'\b\d{1,3}(?:\.\d+)?\b', text)
if numbers:
entities['numbers'] = numbers
# convert sets to lists for JSON-serializable output
return {k:list(v) for k,v in entities.items()}
