from pydantic import BaseModel

class Question(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    question: str
    answer: str

