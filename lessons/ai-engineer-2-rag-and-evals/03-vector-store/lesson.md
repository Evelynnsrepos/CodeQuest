---
title: A vector store in NumPy
minutes: 45
xp: 60
hint: add: self.items.extend(items), then new = np.asarray(vectors, dtype=float) and self.vectors = np.vstack([self.vectors, new])
hint: search: build idx, the positions that pass the filter: ok = True, and set ok = False when any field in where doesn't match
hint: search: scores = self.vectors[idx] @ np.asarray(q, dtype=float), order = np.argsort(-scores)[:k], then build (item, score) pairs
hint: save: np.save(path + ".npy", self.vectors) and json.dump(self.items, f). load: vectors = np.load(...), store = cls(vectors.shape[1]), store.add(json.load(f), vectors)
---
# Search by meaning, fast

⏱️ About 45 minutes

> **Warm-up:** you have 100,000 chunk vectors and one question vector. How do you find the 5 closest?

A **vector store** keeps the chunk vectors and their metadata, and answers "the `k` most similar to this vector". With normalized vectors, similarity is a dot product, so one matrix-vector multiply scores **all** chunks at once:

```python
scores = self.vectors @ q          # (n,) one score per chunk
top = np.argsort(-scores)[:k]      # indexes of the k best
```

For 100,000 × 768 numbers that's well under a second in NumPy. Real vector databases (**Qdrant**, **Chroma**, **pgvector** in PostgreSQL, **LanceDB**, **FAISS**) add approximate search for millions of vectors (an index called HNSW), saving to disk, filters on metadata, and updates. Their API looks like what you're building: `add`, `search(vector, k, filter)`.

**Filters:** "only search notes tagged `nix`" is a metadata filter applied before ranking.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `self.items.extend(items)` | | adds every item of one list to the end of another |
| `np.vstack([A, B])` | "vertical stack" | puts the rows of B under the rows of A |
| `self.items[i].get(field)` | | the item's value for that field, or `None` |
| `self.vectors[idx]` | | with a list of positions: only those rows |
| `np.argsort(-scores)` | | the positions sorted by score, **biggest first** (the minus flips the order) |
| `[:k]` | | the first k of them |
| `float(x)` | | a NumPy number → a plain Python number |
| `with open(path, "w", encoding="utf-8") as f:` | | opens a file for writing and closes it when done |
| `json.dump(data, f)` / `json.load(f)` | | writes data as JSON / reads it back |
| `@classmethod` and `cls` | | a method you call on the class itself (`VectorStore.load(...)`); `cls(...)` makes a new store |

### 👀 Worked example: search with a filter

Items a (nix), b (git), c (nix) with vectors (1, 0), (0, 1), (0.71, 0.71). Search q = (0, 1), k = 1, `where={"tag": "nix"}`:

1. The filter keeps positions 0 and 2 (b is "git").
2. Scores: a: 1·0 + 0·1 = **0**. c: 0.71·0 + 0.71·1 = **0.71**.
3. `np.argsort(-scores)` → c first. `[:1]` keeps only c.
4. Result: `[(c, 0.71)]`. Without the filter, b would have won with 1.0.

## 🎯 Your quest

Complete `VectorStore`:

1. `add(items, vectors)`: `items` is a list of dicts (with at least `"id"`), `vectors` a 2-D array with one row each. Append both (`np.vstack`).
2. `search(q, k=3, where=None)`: return the best `k` items as a list of `(item, score)` pairs, best first. `where` is an optional dict: only items whose fields equal all those values are considered.
3. `save(path)` / `VectorStore.load(path)`: write the vectors with `np.save(path + ".npy", ...)` and the items as JSON to `path + ".json"`; `load` is a `classmethod` that rebuilds the store.

**Part 1:** `add`. Replace `pass` with (8 spaces, inside the class):

1. `self.items.extend(items)`
2. `new = np.asarray(vectors, dtype=float)`
3. `self.vectors = np.vstack([self.vectors, new])`

**Part 2:** `search`. Replace `return []` with:

1. `idx = []`
2. `for i in range(len(self.items)):`
3. `    ok = True`
4. `    if where:`
5. `        for field in where:`
6. `            if self.items[i].get(field) != where[field]:`
7. `                ok = False`
8. `    if ok:`
9. `        idx.append(i)`
10. `if len(idx) == 0:`
11. `    return []`
12. `scores = self.vectors[idx] @ np.asarray(q, dtype=float)`
13. `order = np.argsort(-scores)[:k]`
14. `out = []`
15. `for o in order:`
16. `    out.append((self.items[idx[o]], float(scores[o])))`
17. `return out`

`o` is a position in the **filtered** list, so line 16 uses `idx[o]` to find the real item.

**Part 3:** `save`. Replace `pass` with:

1. `np.save(path + ".npy", self.vectors)`
2. `with open(path + ".json", "w", encoding="utf-8") as f:`
3. `    json.dump(self.items, f)`

`load`: replace `return cls(1)` with:

1. `vectors = np.load(path + ".npy")`
2. `store = cls(vectors.shape[1])`
3. `with open(path + ".json", encoding="utf-8") as f:`
4. `    store.add(json.load(f), vectors)`
5. `return store`

**Remember:** normalized vectors → one matrix multiply scores everything.

## Review

<details><summary>Why must questions and chunks use the same embedding model?</summary>Different models put meaning in different directions, so their vectors can't be compared.</details>
