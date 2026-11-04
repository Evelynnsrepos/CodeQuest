---
title: A web API with FastAPI
xp: 60
---
# Your AI behind a URL

> **Warm-up:** how could a phone app, a website and a Discord bot all use the same RAG code?

Put it behind an **HTTP API**. **FastAPI** is the standard Python choice for AI services: you write normal functions, and it handles URLs, JSON and **validation** using **pydantic** models.

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Question(BaseModel):
    text: str = Field(min_length=1, max_length=2000)
    k: int = Field(default=3, ge=1, le=10)      # ge = greater or equal, le = less or equal

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(q: Question):
    return {"answer": "...", "sources": [...]}
```

If a request breaks the rules (empty text, `k = 50`), FastAPI answers **422** with a description, and your function never runs. That's the trust boundary from the Data cleaning course: validate everything that comes from outside.

Run it for real with `uvicorn main:app --reload` and open `http://localhost:8000/docs`: FastAPI writes interactive documentation for you. In code (and in the check) you use `TestClient(app)`, which calls the app without a network.

## Your quest

Build `app` with:
1. `GET /health` → `{"status": "ok"}`.
2. `POST /ask` taking the `Question` model above and returning `{"answer": ..., "sources": ...}` from the given `answer_question(text, k)`.
3. `POST /feedback` taking a model `Feedback` with `question: str` (min length 1) and `rating: int` from 1 to 5; it appends the dict to `FEEDBACK` and returns `{"saved": len(FEEDBACK)}`.

**Remember:** pydantic models at the edge; 422 for bad input.

## Review

<details><summary>Why fail fast on missing settings?</summary>So the app stops at startup with a clear message instead of failing confusingly later.</details>
