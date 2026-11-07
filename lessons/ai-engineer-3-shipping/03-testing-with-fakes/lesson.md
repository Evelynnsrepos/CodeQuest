---
title: Testing AI apps with fakes
minutes: 45
xp: 60
hint: ask: change the line to def ask(q: Question, llm=Depends(get_llm)): and inside: try: return {"answer": llm(q.text)}
hint: ask: except RuntimeError: raise HTTPException(503, "model unavailable")
hint: run_tests: define fake_llm and get_fake (returns fake_llm), broken and get_broken, then try: set app.dependency_overrides[get_llm] = get_fake
hint: run_tests: post, assert the answer, switch to get_broken, post, assert 503, return True. finally: app.dependency_overrides.clear()
---
# Tests that don't call a real model

⏱️ About 45 minutes

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
def fake_llm(text):
    return "FAKE"

def get_fake():
    return fake_llm

app.dependency_overrides[get_llm] = get_fake
```

What to test with fakes: validation, the prompt you build, error handling (the model raises → your API answers **503**, not a crash with a stack trace), and the response format.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `llm=Depends(get_llm)` | | "to run this endpoint, call `get_llm()` and give me what it returns as `llm`" |
| `raise HTTPException(503, "model unavailable")` | | FastAPI turns this into a 503 answer with `{"detail": "model unavailable"}` |
| `def fake_llm(text):` inside `run_tests` | | a function defined inside another function; it only exists in there |
| `app.dependency_overrides[get_llm] = get_fake` | | "whenever an endpoint asks for `get_llm`, call `get_fake` instead" |
| `assert condition` | | crashes with an error if the condition is false: that's how a test fails |
| `try:` ... `finally:` | | the `finally` lines **always** run, even if an `assert` failed or a `return` happened |

### 👀 Why two functions for one fake

`Depends` calls the function you give it, and uses what **that** returns. So the override must be a function that returns the fake model:

1. `get_fake()` is called by FastAPI → it returns `fake_llm`.
2. Your endpoint gets `llm = fake_llm` and calls `llm("hi")` → `"FAKE: hi"`.

The example at the top of this lesson works the same way.

## 🎯 Your quest

1. Complete `/ask` so it uses `Depends(get_llm)`. If the LLM call raises `RuntimeError`, return status **503** with `{"detail": "model unavailable"}` (raise `HTTPException(503, "model unavailable")`).
2. Write `run_tests()` that, using `TestClient` and `app.dependency_overrides`:
   - checks a fake LLM's answer comes back in `{"answer": ...}`;
   - checks a fake that raises `RuntimeError` gives 503;
   - clears the overrides at the end (`app.dependency_overrides.clear()`), even if an assert fails (`try`/`finally`);
   - returns `True` when both pass.

**Part 1:** `/ask`. Replace the two lines `def ask(q: Question):` and `return {"answer": ""}` with (keep `@app.post("/ask")` above them):

1. `def ask(q: Question, llm=Depends(get_llm)):`
2. `    try:`
3. `        return {"answer": llm(q.text)}`
4. `    except RuntimeError:`
5. `        raise HTTPException(503, "model unavailable")`

**Part 2:** `run_tests`. Replace `return False` with:

1. `client = TestClient(app)`
2. `def fake_llm(text):`
3. `    return "FAKE: " + text`
4. `def get_fake():`
5. `    return fake_llm`
6. `def broken(text):`
7. `    raise RuntimeError("down")`
8. `def get_broken():`
9. `    return broken`
10. `try:`
11. `    app.dependency_overrides[get_llm] = get_fake`
12. `    r = client.post("/ask", json={"text": "hi"})`
13. `    assert r.status_code == 200 and r.json() == {"answer": "FAKE: hi"}`
14. `    app.dependency_overrides[get_llm] = get_broken`
15. `    r = client.post("/ask", json={"text": "hi"})`
16. `    assert r.status_code == 503 and r.json() == {"detail": "model unavailable"}`
17. `    return True`
18. `finally:`
19. `    app.dependency_overrides.clear()`

(The starter has empty lines between the small functions to make them easier to read. They're optional.)

**Remember:** fake the model for app tests; evals test the real model.

## Review

<details><summary>What does FastAPI answer when a request breaks the pydantic model?</summary>422 Unprocessable Entity, and the function doesn't run.</details>
