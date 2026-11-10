---
title: RAG, looking things up instead of retraining
minutes: 50
xp: 45
hint: chunk: for start in range(0, len(words), size - overlap): and inside it chunks.append(" ".join(words[start:start + size]))
hint: chunk, still in the loop: if start + size >= len(words): break
hint: retrieve: q = embed(question), left = list(chunks), picked = [], then for turn in range(k):
hint: Inside: if len(left) == 0: break, then best = None and best_score = -1, then for c in left: score = cosine(q, embed(c))
hint: if score > best_score: best = c and best_score = score. After the inner loop: picked.append(best) and left.remove(best). At the end: return picked
---
# Retrieval-Augmented Generation

⏱️ About 50 minutes

> **Warm-up:** you want your model to answer questions about your 300 pages of notes. They don't fit in the context window, and the model was never trained on them. What could you do?

Look up the relevant parts at question time and put only those in the prompt. That's **RAG**:

```
once, ahead of time (indexing):
    split documents into chunks → embed each chunk → store the vectors
for every question (retrieval + generation):
    embed the question → find the most similar chunks → put them in the prompt → ask the model
```

The pieces:

- **Chunking.** Pieces of a few hundred tokens, usually with some **overlap** so a sentence cut at a border still appears whole in one chunk. Too small loses context; too big wastes the window and dilutes the match.
- **Embedding model.** A separate, small model that turns text into a vector so that similar meaning gives similar direction (LLMs 1, lesson 11). Examples: `nomic-embed-text`, `bge-m3`, `Qwen3-Embedding`. LM Studio serves them on `/v1/embeddings`. Questions and chunks must use the **same** embedding model.
- **Retrieval.** Cosine similarity between the question vector and every chunk vector; take the top `k`. With many chunks, a **vector database** (Chroma, Qdrant, pgvector…) does this fast. Production systems often add keyword search (BM25) and a **reranker** model.
- **The prompt.** "Answer using only these excerpts: … Question: …". Asking the model to cite which excerpt it used makes answers checkable.

RAG gives a model **knowledge** without training it, and the knowledge can be updated by editing files. In Module 6 you'll compare it with fine-tuning, and boot.dev's *Learn Retrieval Augmented Generation* course goes much deeper.

Here we use a toy embedding: a vector of word counts. It only matches *exact words*, which shows exactly why real embedding models (which match *meaning*) are better.

## 🔬 Take the formula apart: cosine similarity

`cosine` is given, but here is what it measures. You met it in LLMs 1, lesson 11. Each text becomes a **vector**: a list of numbers, here "how often does each word appear".

<div class="formula">cos(a, b) = <span class="k1">(a · b)</span> <span class="k2">/</span> <span class="k3">(|a| · |b|)</span></div>

1. <span class="k1">a · b</span>, the **dot product**: for every word, multiply its count in `a` by its count in `b`, then add it all up. Words that only one text has give 0 × something = 0.
2. <span class="k3">|a|</span>, the **length** of `a`: square every count, add them, take the square root (`√`, "which number times itself gives this?").
3. <span class="k2">/</span>: divide. This takes out "how long is the text", so only "how similar are the words" is left.

Numbers: question `{"cats": 1, "purr": 1}`, chunk `{"cats": 1, "purr": 1, "softly": 1}`.

- a · b = 1×1 (cats) + 1×1 (purr) = **2**. "softly" isn't in the question, so it adds 0.
- |a| = √(1² + 1²) = √2 ≈ 1.41. |b| = √(1² + 1² + 1²) = √3 ≈ 1.73.
- cos = 2 / (1.41 × 1.73) = 2 / 2.45 ≈ **0.82**.

The result is between 0 (no shared words) and 1 (same words in the same mix). Higher = more similar.

<div class="wrong">❌ Without dividing: a long chunk that says "cats" ten times would win just because it's long.</div>
<div class="right">✅ With dividing by the lengths: what counts is the <b>mix</b> of words, not the amount.</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `text.split()` | | cuts at spaces: a list of words |
| `range(0, 10, 3)` | "range from 0 to 10 in steps of 3" | counts 0, 3, 6, 9 (stops before 10) |
| `words[2:6]` | "words from 2 up to 6" | a **slice**: the words at positions 2, 3, 4, 5. A slice past the end just stops at the end. |
| `" ".join(list)` | "space-join" | glues the words back together with spaces |
| `break` | | leaves the loop right now |
| `list(chunks)` | | a **copy** of the list, so removing from it doesn't touch the original |
| `range(k)` | | counts 0, 1, … k−1: runs the loop k times |
| `left.remove(x)` | | takes `x` out of the list |
| `best = None` | | "nothing picked yet" |

### 👀 Worked example 1: overlapping chunks

`text = "a b c d e f g h i j"` (10 words, positions 0 to 9), `size = 4`, `overlap = 1`. The step is `size - overlap` = 3.

```python
def chunk(text, size, overlap):
    words = text.split()
    chunks = []
    for start in range(0, len(words), size - overlap):
        chunks.append(" ".join(words[start:start + size]))
        if start + size >= len(words):
            break
    return chunks
```

1. `start` = 0: `words[0:4]` → `a b c d`. 0 + 4 = 4, not ≥ 10, keep going.
2. `start` = 3: `words[3:7]` → `d e f g`. The `d` is in both: that's the overlap. 3 + 4 = 7, keep going.
3. `start` = 6: `words[6:10]` → `g h i j`. 6 + 4 = 10 ≥ 10: this chunk reached the end, `break`.
4. Result: `["a b c d", "d e f g", "g h i j"]`.

Without the `break`, `start` = 9 would add a fourth chunk `j`, which is already inside the third one. This is exactly your first function.

### 👀 Worked example 2: picking the top 2 by repeating "best so far"

Scores for three chunks: `cats purr softly` 0.82, `dogs bark loudly` 0.0, `cats and dogs play` 0.35. `k = 2`.

- Turn 1: go through all three, keep the highest → `cats purr softly`. Add it to `picked`, remove it from `left`.
- Turn 2: go through the two that are left → `cats and dogs play`. Add it, remove it.
- Result: `["cats purr softly", "cats and dogs play"]`, best first.

`best_score` starts at -1, lower than any cosine, so the first chunk always beats it. `>` (not `>=`) keeps the **first** chunk when two scores are equal.

## 🎯 Your quest

**Part 1:** `chunk(text, size, overlap)`. Between `chunks = []` and `return chunks`, add:

1. `for start in range(0, len(words), size - overlap):`
2. `    chunks.append(" ".join(words[start:start + size]))`
3. `    if start + size >= len(words):`
4. `        break`

**Part 2:** `retrieve(question, chunks, k)`. Replace `return []` with:

1. `q = embed(question)`
2. `left = list(chunks)`
3. `picked = []`
4. `for turn in range(k):`
5. `    if len(left) == 0:`
6. `        break`
7. `    best = None`
8. `    best_score = -1`
9. `    for c in left:`
10. `        score = cosine(q, embed(c))`
11. `        if score > best_score:`
12. `            best = c`
13. `            best_score = score`
14. `    picked.append(best)`
15. `    left.remove(best)`
16. `return picked`

Lines 5 and 6 stop early if you ask for more chunks than there are. `embed` and `cosine` are given.

Run it: the two HITs should be the chunks about the KV cache.

## Review

<details><summary>Protocol error vs tool failure in MCP: how is each reported?</summary>Protocol errors are JSON-RPC errors (like -32601 Method not found). Tool failures are normal results with isError true, so the model can read them.</details>
<details><summary>What does the official Python SDK use to build a tool's schema?</summary>The function's name, docstring and type hints.</details>
<details><summary>Why pin MCP server versions?</summary>Unpinned npx/uvx runs fetch the newest release, so a compromised update would run automatically.</details>
<details><summary>What is cos(a, b) when a and b share no words?</summary>0. The dot product a · b adds only 0s, and 0 divided by anything is 0.</details>
