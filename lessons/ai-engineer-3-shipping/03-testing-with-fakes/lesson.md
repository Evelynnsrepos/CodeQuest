---
title: Testing AI apps with fakes
xp: 60
---
# Tests that don't call a real model

> **Warm-up:** your test suite calls a real LLM 200 times. What goes wrong?

It's slow, it costs money, it fails when the network does, and the answers change between runs. So the tests for your **app logic** swap the model for a **fake** that returns a fixed answer. (The real model gets tested separately, by the eval suite from AI engineer 2.)

FastAPI does this with **dependencies**: an endpoint asks for what it needs with `Depends`, and tests replace it with `app.dependency_overrides`:

```python
def get_llm():
    return RealLLM(settings)                 # the real thing

@app.post("/ask")
def ask(q: Question, llm=Depends(get_llm)):
    return {"answer": llm(q.text)}

# in a test:
app.dependency_overrides[get_llm] = lambda: (lambda text: "FAKE")
```

What to test with fakes: validation, the prompt you build, error handling (the model raises → your API answers **503**, not a crash with a stack trace), and the response format.

## Your quest

1. Complete `/ask` so it uses `Depends(get_llm)`. If the LLM call raises `RuntimeError`, return status **503** with `{"detail": "model unavailable"}` (raise `HTTPException(503, "model unavailable")`).
2. Write `run_tests()` that, using `TestClient` and `app.dependency_overrides`:
   - checks a fake LLM's answer comes back in `{"answer": ...}`;
   - checks a fake that raises `RuntimeError` gives 503;
   - clears the overrides at the end (`app.dependency_overrides.clear()`), even if an assert fails (`try`/`finally`);
   - returns `True` when both pass.

**Remember:** fake the model for app tests; evals test the real model.

## Review

<details><summary>What does FastAPI answer when a request breaks the pydantic model?</summary>422 Unprocessable Entity, and the function doesn't run.</details>
