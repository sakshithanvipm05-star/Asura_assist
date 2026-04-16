from fastapi import FastAPI
from pydantic import BaseModel
from rag import get_answer

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/chat")
def chat(q: Query):
    answer, sources = get_answer(q.query)
    return {"answer": answer, "sources": sources}

@app.get("/")
def root():
    return {"status": "MVP running"}