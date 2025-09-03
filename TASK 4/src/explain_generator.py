from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import os


class ExplainGenerator:
def __init__(self, model_name='google/flan-t5-large'):
# Flan-T5 is a good open-source instruction model for explanations.
self.tokenizer = AutoTokenizer.from_pretrained(model_name)
self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
self.pipe = pipeline('text2text-generation', model=self.model, tokenizer=self.tokenizer, device=0 if __import__('torch').cuda.is_available() else -1)


def generate(self, question, context='', max_length=512):
prompt = """
You are an expert in Computer Science research. Use the context below (mostly paper abstracts and short excerpts) to answer the user's question precisely. If the answer is not in the context, answer concisely and indicate uncertainty.


Context:
""" + context + "\n\nQuestion: " + question + "\nAnswer:"
resp = self.pipe(prompt, max_length=max_length, do_sample=False)[0]['generated_text']
return resp


# For very large models or local LLaMA usage, users can swap this module to call a local server (e.g. Llama.cpp or text-generation-inference).
