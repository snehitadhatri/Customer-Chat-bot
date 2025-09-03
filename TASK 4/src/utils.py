import streamlit as st
from retriever import Retriever
from summarizer import Summarizer
from explain_generator import ExplainGenerator


@st.cache_resource
def get_components():
retriever = Retriever()
summarizer = Summarizer()
explainer = ExplainGenerator()
return retriever, summarizer, explainer
