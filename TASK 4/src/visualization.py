import streamlit as st
import networkx as nx
from pyvis.network import Network
import spacy
from io import BytesIO


nlp = spacy.load('en_core_web_sm')




def extract_concepts(text, top_k=15):
doc = nlp(text)
keywords = [chunk.text for chunk in doc.noun_chunks]
# frequency-based selection
uniq = []
for k in keywords:
if k.lower() not in [u.lower() for u in uniq]:
uniq.append(k)
return uniq[:top_k]




def build_and_show_graph(concepts):
g = nx.Graph()
for i, c in enumerate(concepts):
g.add_node(c, size=10 + 2*i)
# naive co-occurrence edges: connect each to next
for i in range(len(concepts)-1):
g.add_edge(concepts[i], concepts[i+1])
net = Network(height='500px', width='100%')
net.from_nx(g)
return net




def pyvis_to_html(net):
html = net.generate_html()
return html
