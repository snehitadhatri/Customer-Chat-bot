import streamlit as st
from utils import load_models, retrieve_answers, extract_medical_entities


st.set_page_config(page_title='MedQuAD — Medical Q&A', layout='centered')
st.title('MedQuAD — Medical Q&A Chatbot')
st.markdown('A retrieval-based medical QA demo using the MedQuAD dataset.')


@st.cache_resource
def load_all(models_dir='models'):
return load_models(models_dir)


vectorizer, nn, qa_table = load_all()


query = st.text_input('Ask a medical question', placeholder='e.g. What are the side effects of metformin?')


if st.button('Get Answer') or (query and st.session_state.get('auto_run')):
if not query.strip():
st.warning('Please type a question.')
else:
# Entity recognition
ents = extract_medical_entities(query)
st.subheader('Detected medical entities')
st.json(ents)


# Retrieval
results = retrieve_answers(query, vectorizer, nn, qa_table, topk=5)
st.subheader('Top answers (retrieved)')
for i,res in enumerate(results,1):
st.markdown(f"**Result {i} — Score: {res['score']:.3f}**")
st.write(res['answer'])
if res.get('url'):
st.markdown(f"Source: {res['url']}")
st.write('---')


st.subheader('Helpful tips')
st.write('- Ask specific questions (include symptoms, drug names, timeframes).')
st.write('- This system retrieves answers from the MedQuAD dataset; it is for research/demo only and not a substitute for professional medical advice.')
