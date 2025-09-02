import os
def parse_medquad_xml(folder):
"""Parse MedQuAD XML files in given folder. Returns DataFrame with columns: id, question, answer, url, focus, qtype"""
records = []
xml_files = glob.glob(os.path.join(folder, "**", "*.xml"), recursive=True)
for xf in xml_files:
try:
tree = etree.parse(xf)
root = tree.getroot()
for qa in root.findall('.//Question'):
qid = qa.get('id') or None
qtext = (qa.findtext('QuestionText') or '').strip()
ans = (qa.findtext('Answer') or '').strip()
url = (qa.findtext('AnswerURL') or '')
qtype = (qa.get('type') or '')
focus = (qa.findtext('QuestionFocus') or '')
records.append({'id': qid, 'question': qtext, 'answer': ans, 'url': url, 'qtype': qtype, 'focus': focus})
except Exception as e:
print(f"Failed parsing {xf}: {e}")
df = pd.DataFrame(records)
df = df.drop_duplicates(subset=['question','answer']).reset_index(drop=True)
return df




if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('--data_folder', type=str, default='data', help='Folder with MedQuAD XML files')
parser.add_argument('--out_dir', type=str, default='models', help='Where to save vectorizer + index')
parser.add_argument('--n_neighbors', type=int, default=5)
args = parser.parse_args()


os.makedirs(args.out_dir, exist_ok=True)
print('Parsing MedQuAD XMLs...')
df = parse_medquad_xml(args.data_folder)
print(f'Parsed {len(df)} QA pairs')


# Build corpus: use question + answer as document for retrieval
df['doc'] = (df['question'].fillna('') + ' . ' + df['answer'].fillna(''))


vectorizer = TfidfVectorizer(max_features=50000, ngram_range=(1,2))
X = vectorizer.fit_transform(df['doc'].values)


print('Fitting NearestNeighbors index (cosine)...')
nn = NearestNeighbors(n_neighbors=args.n_neighbors, metric='cosine', algorithm='brute')
nn.fit(X)


# Save everything
with open(os.path.join(args.out_dir, 'vectorizer.pkl'), 'wb') as f:
pickle.dump(vectorizer, f)
with open(os.path.join(args.out_dir, 'nn_index.pkl'), 'wb') as f:
pickle.dump({'nn': nn, 'X_indices_shape': X.shape}, f)
df[['id','question','answer','url','qtype','focus']].to_csv(os.path.join(args.out_dir, 'qa_table.csv'), index=False)


print('Saved vectorizer, index and qa_table to', args.out_dir)
