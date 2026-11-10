---
title: Checkpoint: RAG over your notes, measured
minutes: 45
xp: 120
hint: First remove the # in front of the three lines BM = ..., EMB = ..., DOC_VECS = ... under TEXTS: they build both searchers once
hint: rank_bm25: for i in BM.rank(question): out.append(IDS[i]). rank_embed: scores = DOC_VECS @ EMB.embed([question])[0], then np.argsort(-scores, kind="stable")
hint: rank_hybrid: return rrf([rank_bm25(question), rank_embed(question)])
hint: report: for each name in methods, count hits in the top 3 and add 1 / (ranked.index(right) + 1) for the MRR
---
# A retriever you can defend with numbers

⏱️ About 45 minutes

> **Warm-up:** what three numbers would you show someone to prove your RAG system works?

(Retrieval recall@k and MRR on a golden set; the share of answers with valid citations; and, with a validated judge, answer quality.)

Build a **hybrid** retriever over the starter's `NOTES` and measure it against keyword search and embeddings alone on `GOLDEN`. `BM25`, `LocalEmbedder` and `rrf` from this course are given in the starter, so you can focus on putting them together.

## Your quest

1. `rank_bm25(question)` and `rank_embed(question)`: full rankings of the note ids (best first). For embeddings, fit one `LocalEmbedder` on `TEXTS` (once, outside the function) and rank by the dot product with the question's embedding.
2. `rank_hybrid(question)`: `rrf([rank_bm25(question), rank_embed(question)])`.
3. `report()`: a dict with, for each method `"bm25"`, `"embed"` and `"hybrid"`, a dict `{"recall@3": ..., "mrr": ...}` over `GOLDEN`.

The check wants hybrid recall@3 ≥ 0.9, and at least as good as the better of the other two.

**On your own machine:** swap `LocalEmbedder` for `ollama_embed` with `nomic-embed-text` (lesson 02), point it at your real notes, and write 30 golden questions from things you actually look up. That's a real, measurable RAG system, and the core of the AI engineer 3 capstone.

### How to answer

`BM25` (with `rank`), `LocalEmbedder` and `rrf` are given: your code from lessons 02, 04 to 06. First, under `TEXTS`, remove the `# ` in front of these three lines, so both searchers are built once:

1. `BM = BM25(TEXTS)`
2. `EMB = LocalEmbedder(TEXTS)`
3. `DOC_VECS = EMB.embed(TEXTS)`

`rank_bm25`: replace `return IDS` with:

1. `out = []`
2. `for i in BM.rank(question):`
3. `    out.append(IDS[i])`
4. `return out`

`rank_embed`: replace `return IDS` with:

1. `scores = DOC_VECS @ EMB.embed([question])[0]`
2. `out = []`
3. `for i in np.argsort(-scores, kind="stable"):`
4. `    out.append(IDS[i])`
5. `return out`

`EMB.embed([question])` makes a matrix with one row; `[0]` takes that row. `kind="stable"` keeps the note order on ties.

`rank_hybrid`: replace `return IDS` with:

1. `return rrf([rank_bm25(question), rank_embed(question)])`

`report`: replace `return {}` with:

1. `out = {}`
2. `methods = {"bm25": rank_bm25, "embed": rank_embed, "hybrid": rank_hybrid}`
3. `for name in methods:`
4. `    rank = methods[name]`
5. `    hits = 0`
6. `    total = 0.0`
7. `    for q, right in GOLDEN:`
8. `        ranked = rank(q)`
9. `        if right in ranked[:3]:`
10. `            hits = hits + 1`
11. `        total = total + 1 / (ranked.index(right) + 1)`
12. `    out[name] = {"recall@3": hits / len(GOLDEN), "mrr": total / len(GOLDEN)}`
13. `return out`

Line 2 stores the three **functions themselves** in a dictionary (no brackets after their names), so line 8 can call whichever one this round is about.

## Review

<details><summary>Name four things a trace span records.</summary>The step, the tool and its arguments, the result or error, and how long it took.</details>
<details><summary>What do cheap search and reranking each optimize?</summary>Cheap search: recall (don't miss the right chunk). Reranking: precision (put the best first).</details>
