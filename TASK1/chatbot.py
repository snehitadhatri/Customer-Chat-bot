import json
from vector_store import VectorStore
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

class ChatBot:
    def __init__(self):
        self.vs = VectorStore()
        self.responses = self.load_responses()

    def load_responses(self):
        with open("responses.json", "r") as f:
            return json.load(f)

    def get_response(self, query):
        context = self.vs.search(query)
        if context:
            full_prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
            return self.ask_llm(full_prompt)
        return self.ask_llm(query)

    def ask_llm(self, prompt):
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are a helpful customer support assistant."},
                          {"role": "user", "content": prompt}]
            )
            return completion.choices[0].message["content"].strip()
        except Exception as e:
            return f"⚠️ Error: {e}"

    def update_knowledge_base(self, file_path):
        self.vs.add_document(file_path)
