---
title: A web API with FastAPI
minutes: 45
xp: 60
hint: The code goes under app = FastAPI(). Start with the two classes: class Question(BaseModel): and class Feedback(BaseModel):
hint: Each route is a decorator line like @app.get("/health") directly above a normal def
hint: /ask: answer, sources = answer_question(q.text, q.k), then return {"answer": answer, "sources": sources}
hint: /feedback: FEEDBACK.append(f.model_dump()), then return {"saved": len(FEEDBACK)}
---
# Your AI behind a URL

⏱️ About 45 minutes

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

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `class Question(BaseModel):` | | describes what a request body must look like |
| `text: str = Field(min_length=1, max_length=2000)` | | a field `text` that must be text, 1 to 2000 characters long |
| `k: int = Field(default=3, ge=1, le=10)` | | a whole number from 1 to 10 (`ge` = greater or equal, `le` = less or equal), 3 if not given |
| `@app.get("/health")` | "app get health" | a **decorator**: the line right above a `def`. It tells FastAPI "call this function for GET requests to /health". |
| `@app.post("/ask")` | | the same for POST requests (requests that send a body) |
| `def ask(q: Question):` | | FastAPI reads the JSON body, checks it against `Question`, and hands it over as `q` |
| `q.text`, `q.k` | | the fields of the checked body |
| `f.model_dump()` | | the model turned back into a plain dictionary |

### 👀 What happens to one request

`POST /ask` with `{"text": "hi"}`:

1. FastAPI checks it with `Question`: `text` is 2 characters (OK), `k` is missing → default 3.
2. Your `ask(q)` runs with `q.text = "hi"` and `q.k = 3`.
3. You return a dictionary; FastAPI sends it as JSON.

With `{"text": ""}` step 1 fails (min length 1), FastAPI answers **422** and your function never runs.

## 🎯 Your quest

Build `app` with:
1. `GET /health` → `{"status": "ok"}`.
2. `POST /ask` taking the `Question` model above and returning `{"answer": ..., "sources": ...}` from the given `answer_question(text, k)`.
3. `POST /feedback` taking a model `Feedback` with `question: str` (min length 1) and `rating: int` from 1 to 5; it appends the dict to `FEEDBACK` and returns `{"saved": len(FEEDBACK)}`.

The starter has all these lines under `app = FastAPI()`, as comments. Remove the `# ` in front of each, or type them yourself:

1. `class Question(BaseModel):`
2. `    text: str = Field(min_length=1, max_length=2000)`
3. `    k: int = Field(default=3, ge=1, le=10)`
4. (two empty lines)
5. `class Feedback(BaseModel):`
6. `    question: str = Field(min_length=1)`
7. `    rating: int = Field(ge=1, le=5)`
8. (two empty lines)
9. `@app.get("/health")`
10. `def health():`
11. `    return {"status": "ok"}`
12. (two empty lines)
13. `@app.post("/ask")`
14. `def ask(q: Question):`
15. `    answer, sources = answer_question(q.text, q.k)`
16. `    return {"answer": answer, "sources": sources}`
17. (two empty lines)
18. `@app.post("/feedback")`
19. `def feedback(f: Feedback):`
20. `    FEEDBACK.append(f.model_dump())`
21. `    return {"saved": len(FEEDBACK)}`

**Remember:** pydantic models at the edge; 422 for bad input.

## Review

<details><summary>Why fail fast on missing settings?</summary>So the app stops at startup with a clear message instead of failing confusingly later.</details>
