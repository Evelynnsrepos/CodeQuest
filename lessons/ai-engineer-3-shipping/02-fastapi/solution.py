from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

FEEDBACK = []


def answer_question(text, k):
    sources = []
    for i in range(k):
        sources.append("note-" + str(i))
    return "(fake answer to " + repr(text) + ")", sources


app = FastAPI()


class Question(BaseModel):
    text: str = Field(min_length=1, max_length=2000)
    k: int = Field(default=3, ge=1, le=10)


class Feedback(BaseModel):
    question: str = Field(min_length=1)
    rating: int = Field(ge=1, le=5)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(q: Question):
    answer, sources = answer_question(q.text, q.k)
    return {"answer": answer, "sources": sources}


@app.post("/feedback")
def feedback(f: Feedback):
    FEEDBACK.append(f.model_dump())
    return {"saved": len(FEEDBACK)}


client = TestClient(app)
print(client.get("/health").json())
print(client.post("/ask", json={"text": "how do I free disk space?"}).json())
