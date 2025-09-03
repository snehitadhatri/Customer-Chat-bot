import streamlit as st
# store abstract in context (append)
st.session_state['context'] += '


' + (r.get('title','') + '
' + r.get('abstract',''))
st.success('Added to context')
else:
st.info('Already in context')


if cols[1].button('Use as only context', key=only_key):
st.session_state['context'] = (r.get('title','') + '
' + r.get('abstract',''))
st.session_state['selected_ids'] = [r.get('id','paper_only')]
st.success('Set as only context')


# open arXiv link if possible
arxiv_id = r.get('id') or r.get('paper_id') or r.get('pdf_url')
if arxiv_id:
url = None
# if id looks like 1703.00001 or cs/9901001
if isinstance(arxiv_id, str) and ('/' in arxiv_id or arxiv_id.count('.')>=1):
url = f'https://arxiv.org/abs/{arxiv_id}'
elif isinstance(arxiv_id, str) and arxiv_id.startswith('http'):
url = arxiv_id
if url:
cols[2].markdown(f"[Open on arXiv]({url})")


# build context to send to LLM
if st.session_state['context'].strip():
context_text = truncate_text(st.session_state['context'], max_chars=max_context_chars)
else:
# use top-K retrieved abstracts
context_text = build_combined_context(results, max_chars=max_context_chars)


st.markdown('---')
st.markdown('### Explanation / Answer')
with st.spinner('Generating answer...'):
try:
answer = explainer.generate(query, context=context_text, max_length=512)
except Exception as e:
st.error(f'Explanation generation failed: {e}')
answer = 'Error: explanation generation failed.'


st.markdown('**Answer:**')
st.write(answer)


# Save to conversation history
st.session_state['conversation'].append({'q': query, 'a': answer, 'context': context_text})


st.markdown('---')
st.markdown('### Concept visualization')
try:
concepts = extract_concepts(context_text if context_text else ' '.join([r.get('abstract','') for r in results]))
net = build_and_show_graph(concepts)
html = pyvis_to_html(net)
st.components.v1.html(html, height=500, scrolling=True)
except Exception:
st.info('Concept visualization is unavailable (pyvis or networkx missing).')


# Follow-up question box (uses conversation history)
st.markdown('---')
st.subheader('Ask a follow-up (uses conversation history)')
followup = st.text_input('Follow-up question', key='followup_input')
if st.button('Ask follow-up') and followup:
# build conversational context (last N turns)
last_turns = st.session_state.get('conversation', [])[-4:]
convo_text = ''
for turn in last_turns:
convo_text += f"Q:
