---
title: Attention in five lines of NumPy
minutes: 45
xp: 60
hint: softmax: shifted = x - x.max(axis=-1, keepdims=True), e = np.exp(shifted), return e / e.sum(axis=-1, keepdims=True)
hint: attention: d = Q.shape[-1] and scores = Q @ K.swapaxes(-1, -2) / np.sqrt(d)
hint: Causal part: if causal: n = scores.shape[-1], mask = np.triu(np.ones((n, n), dtype=bool), k=1), scores = np.where(mask, -np.inf, scores)
hint: Last line: return softmax(scores) @ V
---
# The heart of a transformer, vectorized

⏱️ About 45 minutes

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

## 🔬 The formula, step by step

**softmax( Q Kᵀ / √d ) V**, read from the inside out:

| Piece | Say it | Means |
|---|---|---|
| `Kᵀ` | "K transposed" | K with rows and columns swapped |
| `Q Kᵀ` | "Q times K transposed" | every query dotted with every key: a score table, one row per token |
| `√d` | "the square root of d" | d is the number of columns. √64 = 8, because 8 × 8 = 64. |
| `softmax` | | turns each row of scores into weights that add up to 1 |
| `… V` | "times V" | mixes the value rows with those weights |

**Softmax of one row** (1, 2, 3):

1. Subtract the biggest number (3): (−2, −1, 0). This stops `exp` from overflowing, and the answer stays the same.
2. `exp` of each (e to the power of it, e ≈ 2.718): e⁻² = 0.135, e⁻¹ = 0.368, e⁰ = 1.
3. Add them: 0.135 + 0.368 + 1 = 1.503.
4. Divide each by 1.503: **(0.090, 0.245, 0.665)**. They add up to 1.

**The causal mask** for 3 tokens, `np.triu(np.ones((3, 3), dtype=bool), k=1)`:

```
[[False,  True,  True],
 [False, False,  True],
 [False, False, False]]
```

`True` marks "a later token". `np.where(mask, -np.inf, scores)` puts −∞ there, and e^(−∞) = 0, so after softmax those weights are exactly 0. Token 1 sees only itself, token 2 sees tokens 1 and 2, and so on.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `x.max(axis=-1, keepdims=True)` | | the biggest number of each row, kept as a column. `-1` means "the last axis". |
| `np.exp(x)` | | e to the power of each number |
| `e.sum(axis=-1, keepdims=True)` | | each row's total |
| `Q.shape[-1]` | | the size of the last axis: d |
| `K.swapaxes(-1, -2)` | | swaps the last two axes: the transpose, and it works for batches too |
| `np.sqrt(d)` | | √d |
| `np.where(mask, a, b)` | | "where the mask is True take a, else b", for every position |

## 🎯 Your quest

1. `softmax(x)`: stable softmax over the **last** axis.
2. `attention(Q, K, V, causal=False)`: the formula above, with the optional causal mask. Must work for shapes `(n, d)` and `(batch, n, d)`.

**Part 1:** `softmax`. Replace `return x` with:

1. `shifted = x - x.max(axis=-1, keepdims=True)`
2. `e = np.exp(shifted)`
3. `return e / e.sum(axis=-1, keepdims=True)`

**Part 2:** `attention`. Replace `return V` with:

1. `d = Q.shape[-1]`
2. `scores = Q @ K.swapaxes(-1, -2) / np.sqrt(d)`
3. `if causal:`
4. `    n = scores.shape[-1]`
5. `    mask = np.triu(np.ones((n, n), dtype=bool), k=1)`
6. `    scores = np.where(mask, -np.inf, scores)`
7. `return softmax(scores) @ V`

**Remember:** attention is two matrix multiplications and a softmax.

## Review

<details><summary>What does axis=0 mean in X.mean(axis=0)?</summary>Squash down the rows: one result per column.</details>
