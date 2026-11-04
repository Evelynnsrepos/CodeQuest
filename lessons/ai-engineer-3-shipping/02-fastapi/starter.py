from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

FEEDBACK = []


def answer_question(text, k):
    return f"(fake answer to {text!r})", [f"note-{i}" for i in range(k)]


app = FastAPI()


client = TestClient(app)
print(client.get("/health").json())
print(client.post("/ask", json={"text": "how do I free disk space?"}).json())
