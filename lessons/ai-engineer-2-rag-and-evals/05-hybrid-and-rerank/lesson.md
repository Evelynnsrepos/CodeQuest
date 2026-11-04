---
title: Hybrid search and reranking
xp: 60
---
# Best of both, then a second look

> **Warm-up:** keyword search ranks a note 1st, embedding search ranks it 9th. Their scores are on totally different scales. How do you combine them?

**Hybrid search** runs both searches and merges the **rankings**, not the scores (scores aren't comparable). The standard method is **Reciprocal Rank Fusion** (RRF):

**RRF(d) = Σ over rankings 1 / (k + rank(d))**, with ranks starting at 1 and **k = 60**.

A document that's near the top in either list gets a good total; one that's high in both wins. The `k = 60` keeps a single 1st place from dominating.

**Reranking** is the second look: take the top ~20 candidates from the cheap searches, and score each **(question, chunk) pair** with a slower, smarter model, a **cross-encoder** (e.g. `bge-reranker-v2-m3`, which reads both texts together), or an LLM asked "how relevant is this, 0 to 10?". Then keep the best 3–5 for the prompt. Cheap search for **recall** (don't miss it), expensive rerank for **precision** (put the best first).

## 🧮 Worked example

Keyword search ranks `["p", "q"]`, embedding search ranks `["q", "r"]`. With k = 60:

| id | from list 1 | from list 2 | RRF total |
|---|---|---|---|
| q | 1 / (60 + 2) = 0.0161 | 1 / (60 + 1) = 0.0164 | **0.0325** |
| p | 1 / (60 + 1) = 0.0164 | not there: 0 | 0.0164 |
| r | not there: 0 | 1 / (60 + 2) = 0.0161 | 0.0161 |

So the merged order is **q, p, r**: q was near the top in both lists, so it wins even though it was first in only one.

## Your quest

1. `rrf(rankings, k=60)`: `rankings` is a list of lists of ids (best first). Return all ids sorted by RRF score, best first (ties: by id, alphabetically).
2. `rerank(query, candidates, scorer, top=3)`: `scorer(query, text)` returns a number; `candidates` are dicts with `"text"`. Return the `top` candidates, best score first.
3. `overlap_scorer(query, text)`: a simple stand-in reranker: the share of the query's distinct lowercase words that appear in the text.

**Remember:** fuse ranks, not scores; rerank a short list.

## Review

<details><summary>What does BM25's k₁ control?</summary>Saturation: how quickly extra repeats of a word stop adding score.</details>
