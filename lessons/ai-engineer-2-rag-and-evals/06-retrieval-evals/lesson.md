---
title: Measuring retrieval
minutes: 40
xp: 60
hint: recall_at_k: hits = 0, for q, right in golden: if right in results[q][:k]: hits = hits + 1. Then return hits / len(golden)
hint: mrr: if right in results[q]: position = results[q].index(right) + 1 and total = total + 1 / position
hint: bm25_results: texts in the same order as ids = list(notes), bm = BM25(texts), then for each question turn bm.rank(q) positions back into ids
---
# Is the right chunk in the top 3?

⏱️ About 40 minutes

> **Warm-up:** you changed the chunk size from 300 to 500 words. Did retrieval get better or worse? How would you know?

You can't improve what you don't measure. A **retrieval eval** needs a **golden set**: real questions, each with the id of the chunk (or document) that answers it. Write 30–100 by hand from real use; it's the most valuable hour of a RAG project. Then for each retriever setting, compute:

- **recall@k**: share of questions whose right answer is anywhere in the top k. If it's not retrieved, the LLM can't use it, so this caps the whole system.
- **MRR** ("mean reciprocal rank"): average of 1 / (rank of the right answer), counting 0 if missing. 1 = always first; rewards putting it at the top.

Compare settings on the **same** golden set: keyword only, embeddings only, hybrid, hybrid + rerank. The `NOTES` and `GOLDEN` in the starter are a small real-shaped example.

## Python you need

`BM25` is **given** (lesson 04), with a new method: `bm.rank(question)` returns every document's position, best first.

| You write | Say it | What it does |
|---|---|---|
| `for q, right in golden:` | | each golden item is a pair (question, right id) |
| `results[q][:k]` | | the first k ids returned for that question |
| `results[q].index(right)` | | the position of the right id, counted from 0. `+ 1` turns it into a rank counted from 1. |
| `ids = list(notes)` | | the note ids, in order |
| `ids[i]` | | turns a position back into its id |

## 🧮 Worked example
Four golden questions. The right chunk came back at rank 1, rank 3, not at all, and rank 2.

- **recall@3** = questions with the right chunk in the top 3 ÷ all questions = 3 ÷ 4 = **0.75**
- **MRR** = (1/1 + 1/3 + 0 + 1/2) ÷ 4 = 1.833 ÷ 4 = **0.458**

MRR means "mean reciprocal rank". The **reciprocal** of a number is 1 divided by it: rank 1 → 1/1 = 1, rank 3 → 1/3 = 0.333, rank 2 → 1/2 = 0.5. A miss counts as 0. Then take the mean (average).

## 🎯 Your quest

1. `recall_at_k(results, golden, k)`: `results` maps each question to its ranked list of ids; `golden` is a list of `(question, right_id)`.
2. `mrr(results, golden)`.
3. `bm25_results(notes, golden)`: rank the note ids for every golden question with the `BM25` class (given, from lesson 04); return the `results` dict.

The check makes sure your numbers match and that BM25 gets recall@3 ≥ 0.6 on this set. Print the questions where the right note is **not first**: they use different words than the note ("keyboard shortcut" vs "keybindings", "refresh rate" vs "144"). With 12 notes BM25 still finds them in the top 3; with 5,000 real notes those are the questions it loses. That's what embeddings and hybrid search fix.

**Part 1:** `recall_at_k`. Replace `return 0.0` with:

1. `hits = 0`
2. `for q, right in golden:`
3. `    if right in results[q][:k]:`
4. `        hits = hits + 1`
5. `return hits / len(golden)`

**Part 2:** `mrr`. Replace `return 0.0` with:

1. `total = 0.0`
2. `for q, right in golden:`
3. `    if right in results[q]:`
4. `        position = results[q].index(right) + 1`
5. `        total = total + 1 / position`
6. `return total / len(golden)`

**Part 3:** `bm25_results`. Replace `return {}` with:

1. `ids = list(notes)`
2. `texts = []`
3. `for i in ids:`
4. `    texts.append(notes[i])`
5. `bm = BM25(texts)`
6. `results = {}`
7. `for q, right in golden:`
8. `    ranked = []`
9. `    for i in bm.rank(q):`
10. `        ranked.append(ids[i])`
11. `    results[q] = ranked`
12. `return results`

**Remember:** a golden set first, then change one thing at a time.

## Review

<details><summary>Why fuse rankings instead of scores?</summary>Scores from different searches are on different scales; ranks are comparable.</details>
