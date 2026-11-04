---
title: A vector store in NumPy
xp: 60
---
# Search by meaning, fast

> **Warm-up:** you have 100,000 chunk vectors and one question vector. How do you find the 5 closest?

A **vector store** keeps the chunk vectors and their metadata, and answers "the `k` most similar to this vector". With normalized vectors, similarity is a dot product, so one matrix-vector multiply scores **all** chunks at once:

```python
scores = self.vectors @ q          # (n,) one score per chunk
top = np.argsort(-scores)[:k]      # indexes of the k best
```

For 100,000 × 768 numbers that's well under a second in NumPy. Real vector databases (**Qdrant**, **Chroma**, **pgvector** in PostgreSQL, **LanceDB**, **FAISS**) add approximate search for millions of vectors (an index called HNSW), saving to disk, filters on metadata, and updates. Their API looks like what you're building: `add`, `search(vector, k, filter)`.

**Filters:** "only search notes tagged `nix`" is a metadata filter applied before ranking.

## Your quest

Complete `VectorStore`:

1. `add(items, vectors)`: `items` is a list of dicts (with at least `"id"`), `vectors` a 2-D array with one row each. Append both (`np.vstack`).
2. `search(q, k=3, where=None)`: return the best `k` items as a list of `(item, score)` pairs, best first. `where` is an optional dict: only items whose fields equal all those values are considered.
3. `save(path)` / `VectorStore.load(path)`: write the vectors with `np.save(path + ".npy", ...)` and the items as JSON to `path + ".json"`; `load` is a `classmethod` that rebuilds the store.

**Remember:** normalized vectors → one matrix multiply scores everything.

## Review

<details><summary>Why must questions and chunks use the same embedding model?</summary>Different models put meaning in different directions, so their vectors can't be compared.</details>
