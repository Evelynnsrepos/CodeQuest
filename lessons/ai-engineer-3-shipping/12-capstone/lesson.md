---
title: Capstone: ship your notes assistant
minutes: 90
xp: 150
hint: Everything goes between TRACKER = [] and the end of the file. The starter has every line as a comment: remove the # in front of each, one part at a time
hint: search: score every note, keep the ones above 0, then take the best k with a best-so-far loop
hint: /ask: ids = search(body.question, 3), and if not ids: return the "I don't know." answer before calling the model
hint: /ask: build lines like [1] (nix-gc) text with a counter n, then sources = "\n".join(lines) and the prompt
hint: /eval: hits = 0, then for q, right in GOLDEN: if right in search(q, 3): add one, and return hits / len(GOLDEN)
---
# One service, everything in it

⏱️ About 90 minutes

> **Warm-up:** list every lesson of the three AI engineer courses that this capstone uses.

Put it together: a FastAPI service that answers questions about notes with **hybrid-ready retrieval**, **citations**, **validation**, **a fake-able model**, **cost tracking** and a **retrieval eval endpoint**. The starter has the notes, a BM25 class and a pretend model so it runs anywhere; on your machine you'll swap in Ollama.

## 🐍 Python you need

This capstone only uses pieces you met in this course and in AI engineer 2:

| You write | Say it | What it does | Met in |
|---|---|---|---|
| `list(NOTES)` | | the note ids, in order | |
| `BM.score(q, i)` | | how well note number `i` matches the question (given BM25 class) | AI engineer 2, lesson 06 |
| best-so-far loop, `k` times | | picks the highest score, removes it, repeats | AI engineer 2 |
| `class SearchBody(BaseModel):` with `Field(...)` | | checks the request body | lesson 02 |
| `@app.get(...)`, `@app.post(...)` | | routes | lesson 02 |
| `llm=Depends(get_llm)` | | a model the test can swap for a fake | lesson 03 |
| `raise HTTPException(503, ...)` | | "the model is down" | lesson 03 |
| `"\n".join(lines)` | | the lines glued with line breaks | |
| `text, tokens_in, tokens_out = llm(prompt)` | | the model gives back three things | |

### 👀 Worked example: one search

`search("download a model with ollama", 2)`:

1. Every note gets a BM25 score. Most have 0 (no shared words) and are left out.
2. `ollama-models` has "download", "model" and "ollama" → the highest score. It's picked first and removed from the list.
3. The best of the rest is picked second: `lora`, because it has the word "model" ("the base model"). Word search isn't perfect, which is why the real capstone adds embeddings.
4. Result: `["ollama-models", "lora"]`.

`/ask` then builds the sources like this:

```
[1] (ollama-models) Ollama downloads models with ollama pull llama3.2. ...
[2] (lora) LoRA trains two small matrices A and B per layer. ...
```

## 🎯 Your quest

Build `app` with:

1. `GET /health` → `{"status": "ok", "notes": <number of notes>}`.
2. `POST /search` with body `{"q": str (min length 1), "k": int 1..10, default 3}` → `{"results": [note ids, best first]}` using `BM25` over the `NOTES` texts (only notes with a score above 0).
3. `POST /ask` with body `{"question": str (min length 1, max 1000)}`:
   - retrieve the top 3 ids (as in `/search`); if none, return `{"answer": "I don't know.", "sources": []}` without calling the model;
   - build a prompt with numbered sources `[n] (id) text` (AI engineer 2 lesson 07), call the model through `Depends(get_llm)` (`llm(prompt)` returns `(text, tokens_in, tokens_out)`);
   - record the call in `TRACKER` (a list of dicts with `tokens_in` and `tokens_out`);
   - return `{"answer": text, "sources": [ids in prompt order]}`.
   - If the model raises `RuntimeError`, answer 503.
4. `GET /eval` → `{"recall@3": ...}` over `GOLDEN`, using the same retrieval as `/search`.

The check calls every endpoint with a fake model, checks citations point to real sources, and wants `recall@3 ≥ 0.9`.

The starter already has every line below as a comment, under `TRACKER = []`. Remove the `# ` in front of each line (or type them yourself), one part at a time. Leave the empty lines between the parts as they are.

**Part 1:** the search index:

1. `IDS = list(NOTES)`
2. `TEXTS = []`
3. `for i in IDS:`
4. `    TEXTS.append(NOTES[i])`
5. `BM = BM25(TEXTS)`

**Part 2:** `search(q, k)`, the best `k` notes with a score above 0:

6. `def search(q, k=3):`
7. `    scored = []`
8. `    for i in range(len(IDS)):`
9. `        s = BM.score(q, i)`
10. `        if s > 0:`
11. `            scored.append((s, IDS[i]))`
12. `    out = []`
13. `    for step in range(k):`
14. `        if len(scored) == 0:`
15. `            break`
16. `        top = scored[0]`
17. `        for pair in scored:`
18. `            if pair[0] > top[0]:`
19. `                top = pair`
20. `        out.append(top[1])`
21. `        scored.remove(top)`
22. `    return out`

**Part 3:** the two request bodies:

23. `class SearchBody(BaseModel):`
24. `    q: str = Field(min_length=1)`
25. `    k: int = Field(default=3, ge=1, le=10)`
26. `class AskBody(BaseModel):`
27. `    question: str = Field(min_length=1, max_length=1000)`

**Part 4:** the routes, under `app = FastAPI()`:

28. `@app.get("/health")`
29. `def health():`
30. `    return {"status": "ok", "notes": len(NOTES)}`
31. (empty line)
32. `@app.post("/search")`
33. `def search_endpoint(body: SearchBody):`
34. `    return {"results": search(body.q, body.k)}`
35. (empty line)
36. `@app.post("/ask")`
37. `def ask(body: AskBody, llm=Depends(get_llm)):`
38. `    ids = search(body.question, 3)`
39. `    if not ids:`
40. `        return {"answer": "I don't know.", "sources": []}`
41. `    lines = []`
42. `    n = 1`
43. `    for i in ids:`
44. `        lines.append("[" + str(n) + "] (" + i + ") " + NOTES[i])`
45. `        n = n + 1`
46. `    sources = "\n".join(lines)`
47. `    prompt = ("Answer using only the sources. Cite them like [1]. Say \"I don't know\" if they don't help.\n\n"`
48. `              + sources + "\n\nQuestion: " + body.question)`
49. `    try:`
50. `        text, tokens_in, tokens_out = llm(prompt)`
51. `    except RuntimeError:`
52. `        raise HTTPException(503, "model unavailable")`
53. `    TRACKER.append({"tokens_in": tokens_in, "tokens_out": tokens_out})`
54. `    return {"answer": text, "sources": ids}`
55. (empty line)
56. `@app.get("/eval")`
57. `def evaluate():`
58. `    hits = 0`
59. `    for q, right in GOLDEN:`
60. `        if right in search(q, 3):`
61. `            hits = hits + 1`
62. `    return {"recall@3": hits / len(GOLDEN)}`

### How to answer

Press **Run** first: the last line prints `{'status': 'ok', 'notes': 12}`. Then press **Submit**. It calls all four routes with a fake model and passes when the sources in `/ask` are real notes, an empty-result question gets "I don't know.", a broken model gives 503, and `/eval` shows `recall@3` of at least 0.9.

**On your machine (the real capstone).** Tick each step as you finish it; the ticks are saved on this device. One step per sitting is a fine pace.

- [ ] Make a git repo with `main.py` and `requirements.txt`
- [ ] Add the Dockerfile from lesson 08
- [ ] Add the CI workflow from lesson 09
- [ ] Add tests with fakes (lesson 03)
- [ ] Add a `.env.example` (lesson 01)
- [ ] Put in your own notes and write 30+ golden questions
- [ ] Replace `get_llm` with a call to Ollama (AI engineer 2 lesson 08)
- [ ] Add the embedding half of hybrid search (AI engineer 2 lessons 02 to 05)
- [ ] Write the README from lesson 11 with your own numbers
- [ ] Publish it on GitHub: that repository is your portfolio piece

## Review

<details><summary>Which status codes has this course used, and for what?</summary>200 OK, 422 invalid input, 429 rate limited, 503 model unavailable.</details>
