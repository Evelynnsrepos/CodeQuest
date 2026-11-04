---
title: Attention in five lines of NumPy
xp: 60
---
# The heart of a transformer, vectorized

> **Warm-up:** in LLMs 8 you computed attention with lists and loops. Which parts were matrix multiplications?

Attention (LLMs 8, lesson 01) in matrix form:

**Attention(Q, K, V) = softmax( Q Kᵀ / √d ) V**

- `Q` (queries), `K` (keys), `V` (values): one row per token, `d` columns.
- `Q @ K.T`: every query dotted with every key, a `(tokens × tokens)` score table.
- `/ √d`: keeps scores from growing with `d` (Math 2, lesson 11).
- **causal mask**: a token may not look at later tokens, so set scores above the diagonal to `-inf` before softmax (they become 0).
- `softmax` **per row**, then `@ V`: each token's output is a weighted mix of the value rows.

## NumPy you need

```python
x - x.max(axis=-1, keepdims=True)   # stable softmax: subtract each row's max
np.exp(x); x.sum(axis=-1, keepdims=True)
np.triu(np.ones((n, n), dtype=bool), k=1)   # True above the diagonal
scores = np.where(mask, -np.inf, scores)
```

`axis=-1` means "the last axis", so the same code works for one sequence `(n, d)` or a batch `(b, n, d)`. Use `K.swapaxes(-1, -2)` instead of `.T` for batches.

## Your quest

1. `softmax(x)`: stable softmax over the **last** axis.
2. `attention(Q, K, V, causal=False)`: the formula above, with the optional causal mask. Must work for shapes `(n, d)` and `(batch, n, d)`.

**Remember:** attention is two matrix multiplications and a softmax.

## Review

<details><summary>What does axis=0 mean in X.mean(axis=0)?</summary>Squash down the rows: one result per column.</details>
