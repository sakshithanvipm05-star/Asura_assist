from fastapi import FastAPI
from pydantic import BaseModel
from rag import get_answer
from fastapi.middleware.cors import CORSMiddleware

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)