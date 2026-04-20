import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.brain import Brain
from schemas import Question, AnswerResponse

app = FastAPI(title="Django Mentor API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    mentor = Brain()

except Exception as e:
    print(f"Error initializing Brain: {e}")
    mentor = None

@app.get("/")
async def root():
    return {"status": "ok", "message": "Backend online"}

@app.post('/ask', response_model=AnswerResponse)
async def ask_question(item: Question):
    if mentor is None:
        raise HTTPException(status_code=500, detail="AI Brain is not initialized")
    
    if not item.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    answer = mentor.ask_llm(item.question)

    return AnswerResponse(question=item.question, answer=answer)