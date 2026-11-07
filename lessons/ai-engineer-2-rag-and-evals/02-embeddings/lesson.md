---
title: Embeddings: real and local
minutes: 40
xp: 60
hint: normalize: M = np.asarray(M, dtype=float), lengths = np.linalg.norm(M, axis=1, keepdims=True), then lengths[lengths == 0] = 1 and return M / lengths
hint: ollama_embed: if client is not None: post = client.post, else: post = httpx.post
hint: ollama_embed: r = post(url + "/api/embed", json=payload, timeout=60), r.raise_for_status(), return normalize(r.json()["embeddings"])
hint: LocalEmbedder.embed: return normalize(self.vec.transform(texts).toarray())
---
# Text in, vector out

⏱️ About 40 minutes

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

`httpx` is a modern HTTP client (it sends web requests):

| You write | Say it | What it does |
|---|---|---|
| `np.asarray(M, dtype=float)` | | turns a list of lists into a NumPy matrix of decimals |
| `np.linalg.norm(M, axis=1, keepdims=True)` | | the length of each row (AE 1, lesson 02) |
| `lengths[lengths == 0] = 1` | | wherever a length is 0, use 1 instead. Then 0 / 1 = 0, and you never divide by zero. |
| `M / lengths` | | every row divided by its length |
| `post = client.post` | | stores the **function itself** (no brackets) in a name, to call it later |
| `post(url, json=payload, timeout=60)` | | sends the request. `json=` turns the dictionary into JSON for you. |
| `r.raise_for_status()` | | turns an HTTP error (4xx, 5xx) into a Python error |
| `r.json()["embeddings"]` | | the answer's JSON, and the list of vectors inside it |
| `list(texts)` | | makes sure it's a real list, which JSON needs |

### 👀 Worked example: normalizing

`[[3, 4], [0, 0]]`:

1. Row lengths: √(3² + 4²) = √25 = 5, and 0.
2. The 0 becomes 1.
3. Divide: (3/5, 4/5) = **(0.6, 0.8)**, and (0/1, 0/1) = **(0, 0)**.

Now (0.6, 0.8) has length 1, so its dot product with another length-1 vector is their cosine.

## 🎯 Your quest

1. `normalize(M)`: divide each row of a NumPy matrix by its length (rows of length 0 stay 0).
2. `ollama_embed(texts, model="nomic-embed-text", url="http://localhost:11434", client=None)`: POST to `{url}/api/embed` (use `client.post` if a client is given, else `httpx.post`), raise on HTTP errors, and return the **normalized** NumPy matrix.
3. `LocalEmbedder.embed(texts)`: return `normalize` of the TF-IDF vectors (`self.vec.transform(texts).toarray()`).

Try `ollama_embed(["hello"])` yourself if Ollama is running.

**Part 1:** `normalize`. Replace `return M` with:

1. `M = np.asarray(M, dtype=float)`
2. `lengths = np.linalg.norm(M, axis=1, keepdims=True)`
3. `lengths[lengths == 0] = 1`
4. `return M / lengths`

**Part 2:** `ollama_embed`. Replace its `return` line with:

1. `if client is not None:`
2. `    post = client.post`
3. `else:`
4. `    post = httpx.post`
5. `payload = {"model": model, "input": list(texts)}`
6. `r = post(url + "/api/embed", json=payload, timeout=60)`
7. `r.raise_for_status()`
8. `return normalize(r.json()["embeddings"])`

**Part 3:** `LocalEmbedder.embed`. Replace its `return` line with (8 spaces, it's inside a class):

1. `return normalize(self.vec.transform(texts).toarray())`

**Remember:** one embedding model for questions and chunks; normalize so dot = cosine.

## Review

<details><summary>Why let chunks overlap?</summary>So a sentence cut at a chunk border still appears whole in one chunk.</details>
