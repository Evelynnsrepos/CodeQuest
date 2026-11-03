---
title: Attention as matrix math
xp: 60
---
# The whole attention formula, read and built

> **Warm-up:** here's the formula from the transformer paper. Before reading on, which parts can you already say out loud? `Attention(Q, K, V) = softmax(QKᵀ / √d + M) V`

**In one sentence:** attention scores every query against every key with one matrix product, turns each row into weights with softmax, and mixes the value vectors with those weights.

## 🔣 New symbols

| Symbol | Say it | Means |
|---|---|---|
| `X ∈ ℝ^(T×d)` | "X is T by d" | T tokens, each a d-vector, one per row |
| `Q = XW_Q` | "Q equals X W Q" | each token's query (same for K, V) |
| `QKᵀ` | "Q K transpose" | T × T table: entry (i, j) = `qᵢ · kⱼ` |
| `/ √d` | "over root d" | divide every score (keeps them a sensible size) |
| `M` | "the mask" | T × T: 0 where allowed, `−∞` where token i must not see token j (j > i) |
| `softmax(…)` on a matrix | | softmax **each row** separately |
| `· V` | "times V" | each output row = weighted sum of value rows |
| `−∞` | "minus infinity" | `e^(−∞) = 0`, so that position gets weight 0 |

## The idea, in 4 steps

```
1. S = Q Kᵀ / √d          scores        (T × T)
2. S = S + M              hide future    (T × T)
3. A = softmax(S) by row  weights        (T × T, each row sums to 1)
4. out = A V              mix values     (T × d)
```

Shapes check: `(T × d)(d × T) = T × T`, then `(T × T)(T × d) = T × d`. Same shape as the input, so blocks can be stacked.

## 🗣️ Say it out loud

"Softmax of Q K transpose over root d plus M, times V." → "Score every token against every token, hide the future, turn scores into weights per row, and take the weighted mix of the values."

## 🧮 Worked example (T = 2)

Scores after `/√d`: `[[1, 3], [2, 0]]`. Mask (causal): `[[0, −∞], [0, 0]]`.

- Row 1: `[1, −∞]` → softmax `[1, 0]`: token 1 only sees itself.
- Row 2: `[2, 0]` → softmax `[0.88, 0.12]`.

## 🤖 Where AI uses it

This **is** the core of every transformer. FlashAttention computes exactly this, just in a memory-smart order. The `T × T` table is why long contexts are expensive: 128K tokens means 16 billion scores per head per layer.

## 🎯 Your quest

`matmul`, `transpose` and `softmax` are given. Use `float("-inf")` for −∞ (`math.exp(-inf)` is 0.0).

1. `causal_mask(T)`: T × T, `0.0` where `j ≤ i`, `-inf` where `j > i`.
2. `attention(Q, K, V, causal)`: the 4 steps; add the mask only when `causal` is `True`. `d` is the number of columns of Q.

**Remember:** QKᵀ = every query against every key; softmax goes row by row.

## Review

<details><summary>What's the difference between a · b and a ⊙ b?</summary>The dot product gives one number; ⊙ multiplies entry by entry and gives a vector.</details>
<details><summary>Why do neural networks need activation functions between layers?</summary>Without them, stacked matrices collapse into one linear map.</details>
