from transformers import pipeline


# two-mode summarizer: abstractive (transformers) or extractive via keywords


class Summarizer:
def __init__(self, model_name='facebook/bart-large-cnn'):
self.pipe = pipeline('summarization', model=model_name, device=0 if __import__('torch').cuda.is_available() else -1)


def summarize(self, text, max_length=150, min_length=30):
if len(text.split()) < 30:
return text
out = self.pipe(text, max_length=max_length, min_length=min_length, truncation=True)
return out[0]['summary_text']
