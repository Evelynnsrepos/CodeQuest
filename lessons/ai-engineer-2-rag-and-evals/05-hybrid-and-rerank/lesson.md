---
title: Hybrid search and reranking
minutes: 45
xp: 60
hint: rrf, the scores: for ranking in rankings: rank = 1, then for doc in ranking: score[doc] = score.get(doc, 0) + 1 / (k + rank) and rank = rank + 1
hint: rrf, the order: ids = sorted(score) puts them alphabetically, then pick the highest score len(ids) times (best-so-far, strict >)
hint: rerank: scores = [] with one scorer(query, c["text"]) per candidate, then pick the best position top times, then return those candidates
hint: overlap_scorer: q and t as sets of lowercase words, if len(q) == 0: return 0.0, then count the words of q that are in t and divide by len(q)
---
# Best of both, then a second look

⏱️ About 45 minutes

> **Warm-up:** keyword search ranks a note 1st, embedding search ranks it 9th. Their scores are on totally different scales. How do you combine them?

**Hybrid search** runs both searches and merges the **rankings**, not the scores (scores aren't comparable). The standard method is **Reciprocal Rank Fusion** (RRF):

**RRF(d) = Σ over rankings 1 / (k + rank(d))**, with ranks starting at 1 and **k = 60**.

A document that's near the top in either list gets a good total; one that's high in both wins. The `k = 60` keeps a single 1st place from dominating.

**Reranking** is the second look: take the top ~20 candidates from the cheap searches, and score each **(question, chunk) pair** with a slower, smarter model, a **cross-encoder** (e.g. `bge-reranker-v2-m3`, which reads both texts together), or an LLM asked "how relevant is this, 0 to 10?". Then keep the best 3–5 for the prompt. Cheap search for **recall** (don't miss it), expensive rerank for **precision** (put the best first).

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `score.get(doc, 0) + 1 / (k + rank)` | | the score so far (0 the first time) plus this list's share |
| `sorted(score)` | | the dictionary's keys in alphabetical order |
| `if doc not in out:` | | skips ids that are already placed |
| `best is None or score[doc] > score[best]` | | best-so-far. Because `ids` is alphabetical and `>` is strict, a tie keeps the alphabetically first id. |
| `if best is None: break` | | no candidates left: stop early |
| `set(query.lower().split())` | | the distinct lowercase words |

## 🧮 Worked example
Keyword search ranks `["p", "q"]`, embedding search ranks `["q", "r"]`. With k = 60:

| id | from list 1 | from list 2 | RRF total |
|---|---|---|---|
| q | 1 / (60 + 2) = 0.0161 | 1 / (60 + 1) = 0.0164 | **0.0325** |
| p | 1 / (60 + 1) = 0.0164 | not there: 0 | 0.0164 |
| r | not there: 0 | 1 / (60 + 2) = 0.0161 | 0.0161 |

So the merged order is **q, p, r**: q was near the top in both lists, so it wins even though it was first in only one.

And `overlap_scorer("delete old generations", "delete old nix generations with nix-collect-garbage")`: the query has 3 distinct words, all 3 are in the text → 3 / 3 = **1.0**. Against "nix flakes pin inputs": 0 / 3 = **0**.

## 🎯 Your quest

1. `rrf(rankings, k=60)`: `rankings` is a list of lists of ids (best first). Return all ids sorted by RRF score, best first (ties: by id, alphabetically).
2. `rerank(query, candidates, scorer, top=3)`: `scorer(query, text)` returns a number; `candidates` are dicts with `"text"`. Return the `top` candidates, best score first.
3. `overlap_scorer(query, text)`: a simple stand-in reranker: the share of the query's distinct lowercase words that appear in the text.

**Part 1:** `rrf`. Replace `return []` with:

1. `score = {}`
2. `for ranking in rankings:`
3. `    rank = 1`
4. `    for doc in ranking:`
5. `        score[doc] = score.get(doc, 0) + 1 / (k + rank)`
6. `        rank = rank + 1`
7. `ids = sorted(score)`
8. `out = []`
9. `for step in range(len(ids)):`
10. `    best = None`
11. `    for doc in ids:`
12. `        if doc not in out:`
13. `            if best is None or score[doc] > score[best]:`
14. `                best = doc`
15. `    out.append(best)`
16. `return out`

**Part 2:** `rerank`. Replace `return candidates[:top]` with:

1. `scores = []`
2. `for c in candidates:`
3. `    scores.append(scorer(query, c["text"]))`
4. `picked = []`
5. `for step in range(top):`
6. `    best = None`
7. `    for i in range(len(candidates)):`
8. `        if i not in picked:`
9. `            if best is None or scores[i] > scores[best]:`
10. `                best = i`
11. `    if best is None:`
12. `        break`
13. `    picked.append(best)`
14. `out = []`
15. `for i in picked:`
16. `    out.append(candidates[i])`
17. `return out`

**Part 3:** `overlap_scorer`. Replace `return 0.0` with:

1. `q = set(query.lower().split())`
2. `t = set(text.lower().split())`
3. `if len(q) == 0:`
4. `    return 0.0`
5. `shared = 0`
6. `for w in q:`
7. `    if w in t:`
8. `        shared = shared + 1`
9. `return shared / len(q)`

**Remember:** fuse ranks, not scores; rerank a short list.

## Review

<details><summary>What does BM25's k₁ control?</summary>Saturation: how quickly extra repeats of a word stop adding score.</details>
