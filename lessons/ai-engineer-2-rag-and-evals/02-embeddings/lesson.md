---
title: Embeddings: real and local
xp: 60
---
# Text in, vector out

> **Warm-up:** in LLMs 3 you compared word vectors with cosine similarity. Where did the vectors come from?

An **embedding model** turns a text into a vector so that texts with similar **meaning** get similar vectors (cosine close to 1), even with no words in common. Real options:

| Model | Runs | How to call |
|---|---|---|
| `nomic-embed-text`, `bge-m3`, `mxbai-embed-large` | **Ollama**, on your PC | `POST http://localhost:11434/api/embed` with `{"model": ..., "input": [texts]}` → `{"embeddings": [[...], ...]}` |
| `all-MiniLM-L6-v2`, `bge-small` | `sentence-transformers` library (PyTorch) | `SentenceTransformer(name).encode(texts)` |
| hosted models | an API | similar JSON over HTTPS |

To get one: `ollama pull nomic-embed-text`.

The same interface works for all of them: **a function from a list of texts to a matrix**, one row per text, rows **normalized** to length 1 so that a dot product is the cosine.

**Important:** the question and the chunks must be embedded with the **same** model. Changing the model means re-embedding everything.

For the checks (they can't assume Ollama is running), the starter has a `LocalEmbedder` that uses TF-IDF with character n-grams from scikit-learn: weaker than a real model (it matches spelling, not meaning) but it has the same interface.

## Python you need

`httpx` is a modern HTTP client:

```python
r = httpx.post(url, json=payload, timeout=30)
r.raise_for_status()      # turn 4xx/5xx into an exception
r.json()
```

## Your quest

1. `normalize(M)`: divide each row of a NumPy matrix by its length (rows of length 0 stay 0).
2. `ollama_embed(texts, model="nomic-embed-text", url="http://localhost:11434", client=None)`: POST to `{url}/api/embed` (use `client.post` if a client is given, else `httpx.post`), raise on HTTP errors, and return the **normalized** NumPy matrix.
3. `LocalEmbedder.embed(texts)`: return `normalize` of the TF-IDF vectors (`self.vec.transform(texts).toarray()`).

Try `ollama_embed(["hello"])` yourself if Ollama is running.

**Remember:** one embedding model for questions and chunks; normalize so dot = cosine.

## Review

<details><summary>Why let chunks overlap?</summary>So a sentence cut at a chunk border still appears whole in one chunk.</details>
