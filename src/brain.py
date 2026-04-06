import pandas as pd
import torch
import ollama
from sentence_transformers import SentenceTransformer, util
import os

class Brain:
    def __init__(self, csv_path='..data/django_data.csv', model_name='all-MiniLM-L6-v2'):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        current_dir = os.path.dirname(os.path.abspath(__file__))

        csv_path = os.path.join(current_dir, '..', 'data', 'django_data.csv')

        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Error: Cannot find th CSV")

        self.df = pd.read_csv(csv_path)
        self.model = SentenceTransformer(model_name).to(self.device)

        print(f"[INFO] Initializing DataBase on {self.device}...")
        self.embeddings = self.model.encode(self.df['Content'].tolist(), convert_to_tensor=True)

    def search_context(self, question, treshold=0.1):
        question_embedding = self.model.encode(question, convert_to_tensor=True)
        cosine_scores = util.cos_sim(question_embedding, self.embeddings)[0]

        best_id = cosine_scores.argmax().item() 
        certainity = cosine_scores[best_id].item()

        if certainity < treshold:
            return None, None, None
        
        row = self.df.iloc[best_id]
        return row['Topic'], row['Content'], row['Code']
    
    def ask_llm(self, question):
        theme, content, code = self.search_context(question)

        if content is None:
            return "Sorry, I dont know the answer to that question."
        
        instruction = f"""
        You are a professional Django Mentor. 
        Use ONLY the provided documentation context to answer the user's question.
        
        GUIDELINES:
        1. Answer in POLISH (po polsku).
        2. If the answer is in the documentation, explain it using the context and the code example.
        3. If the documentation is not related to the question at all, say: "Nie znalazłem tego w lokalnej bazie."

        DOCUMENTATION CONTEXT:
        {content}
        
        CODE EXAMPLE:
        {code}
        
        USER QUESTION: 
        {question}"""

        response = ollama.chat(model='llama3.2:3b', messages=[
            {"role": "user", "content": instruction}
        ])

        return response['message']['content']
    
# Tests questions try to insert yours
if __name__ == "__main__":
    try:
        mentor = Brain()

        print(mentor.ask_llm("How to define a model field? "))

        print(mentor.ask_llm("Jak ugotowac jajecznice?"))

    except Exception as e:
        print(f"[ERROR]: {e}")