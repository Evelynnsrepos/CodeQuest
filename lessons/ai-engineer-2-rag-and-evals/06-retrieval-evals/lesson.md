---
title: Measuring retrieval
xp: 60
---
# Is the right chunk in the top 3?

> **Warm-up:** you changed the chunk size from 300 to 500 words. Did retrieval get better or worse? How would you know?

You can't improve what you don't measure. A **retrieval eval** needs a **golden set**: real questions, each with the id of the chunk (or document) that answers it. Write 30–100 by hand from real use; it's the most valuable hour of a RAG project. Then for each retriever setting, compute:

- **recall@k**: share of questions whose right answer is anywhere in the top k. If it's not retrieved, the LLM can't use it, so this caps the whole system.
- **MRR** ("mean reciprocal rank"): average of 1 / (rank of the right answer), counting 0 if missing. 1 = always first; rewards putting it at the top.

Compare settings on the **same** golden set: keyword only, embeddings only, hybrid, hybrid + rerank. The `NOTES` and `GOLDEN` in the starter are a small real-shaped example.

## Your quest

1. `recall_at_k(results, golden, k)`: `results` maps each question to its ranked list of ids; `golden` is a list of `(question, right_id)`.
2. `mrr(results, golden)`.
3. `bm25_results(notes, golden)`: rank the note ids for every golden question with the `BM25` class (given, from lesson 04); return the `results` dict.

The check makes sure your numbers match and that BM25 gets recall@3 ≥ 0.6 on this set. Print the questions where the right note is **not first**: they use different words than the note ("keyboard shortcut" vs "keybindings", "refresh rate" vs "144"). With 12 notes BM25 still finds them in the top 3; with 5,000 real notes those are the questions it loses. That's what embeddings and hybrid search fix.

**Remember:** a golden set first, then change one thing at a time.

## Review

<details><summary>Why fuse rankings instead of scores?</summary>Scores from different searches are on different scales; ranks are comparable.</details>
