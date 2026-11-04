---
title: Capstone: ship your notes assistant
xp: 150
---
# One service, everything in it

> **Warm-up:** list every lesson of the three AI engineer courses that this capstone uses.

Put it together: a FastAPI service that answers questions about notes with **hybrid-ready retrieval**, **citations**, **validation**, **a fake-able model**, **cost tracking** and a **retrieval eval endpoint**. The starter has the notes, a BM25 class and a pretend model so it runs anywhere; on your machine you'll swap in Ollama.

## Your quest

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
