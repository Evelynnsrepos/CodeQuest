from fastapi import Depends, FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field


class Question(BaseModel):
    text: str = Field(min_length=1)


def get_llm():
    def real_llm(text):
        raise RuntimeError("no real model in this lesson")
    return real_llm


app = FastAPI()


@app.post("/ask")
def ask(q: Question, llm=Depends(get_llm)):
    try:
        return {"answer": llm(q.text)}
    except RuntimeError:
        raise HTTPException(503, "model unavailable")


def run_tests():
    client = TestClient(app)

    def fake_llm(text):
        return "FAKE: " + text

    def get_fake():
        return fake_llm

    def broken(text):
        raise RuntimeError("down")

    def get_broken():
        return broken

    try:
        app.dependency_overrides[get_llm] = get_fake
        r = client.post("/ask", json={"text": "hi"})
        assert r.status_code == 200 and r.json() == {"answer": "FAKE: hi"}
        app.dependency_overrides[get_llm] = get_broken
        r = client.post("/ask", json={"text": "hi"})
        assert r.status_code == 503 and r.json() == {"detail": "model unavailable"}
        return True
    finally:
        app.dependency_overrides.clear()


print(run_tests())
