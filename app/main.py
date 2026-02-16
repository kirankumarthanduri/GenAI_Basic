from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Mock GenAI server is running"}

@app.post("/ask")
def ask_ai(q: Question):
    return {
        "answer": f"(Mock AI) You asked: {q.question}"
    }