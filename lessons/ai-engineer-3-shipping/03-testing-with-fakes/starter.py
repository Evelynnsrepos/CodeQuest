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
def ask(q: Question):
    return {"answer": ""}


def run_tests():
    return False


print(run_tests())
