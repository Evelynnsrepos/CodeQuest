---
title: Attention as matrix math
xp: 60
---
# The famous formula, read and built

> **Warm-up:** this is the formula from the transformer paper: `softmax(QKᵀ / √d + M) V`. Which signs do you already recognise?

**In one sentence:** attention scores every token against every token with one matrix product, turns each row of scores into weights, and mixes the tokens' information with those weights.

## 🪜 Plain words

Every token asks a question (its **query**), offers a label (its **key**) and has some information to give (its **value**).

1. Compare every question with every label → a table of scores.
2. Make the scores a sensible size (divide).
3. Hide the future: a token may not look at tokens that come after it.
4. Turn each row of scores into percentages that add to 100%.
5. Each token's new vector = the mix of all values, by those percentages.

## 🪜 With numbers (2 tokens)

Scores after dividing: row 1 = (1, 3), row 2 = (2, 0).

- Token 1 can't see token 2 (future), so its row becomes (1, hidden) → 100% on itself.
- Token 2 sees both: percentages from (2, 0) ≈ (88%, 12%).
- Token 2's output = 0.88 × value₁ + 0.12 × value₂.

## 🔣 The signs

| Sign | Say it | Means |
|---|---|---|
| `Q`, `K`, `V` | "Q, K, V" | queries, keys, values: T rows (tokens) × d columns |
| `Kᵀ` | "K transpose" | flipped so shapes fit |
| `QKᵀ` | "Q K transpose" | T × T table: row i, column j = query i · key j |
| `√d` | "root d" | square root of the vector size |
| `M` | "the mask" | 0 where allowed, `−∞` where token i must not see token j |
| `−∞` | "minus infinity" | so small that e^(−∞) = 0 |
| softmax by row | | each row → percentages adding to 1 |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">softmax</span>( <span class="k2">QKᵀ</span> <span class="k3">/ √d</span> <span class="k4">+ M</span> ) <span class="k5">V</span></div>

| Piece | Say it | Means | Shape (T tokens) |
|---|---|---|---|
| <span class="k2">QKᵀ</span> | "Q K transpose" | score of every query against every key | T × T |
| <span class="k3">/ √d</span> | "divided by root d" | shrink the scores (d = 64 → divide by 8) | T × T |
| <span class="k4">+ M</span> | "plus M" | add −∞ above the diagonal: the future becomes invisible | T × T |
| <span class="k1">softmax</span>( ) | "softmax of" | each **row** → weights that add to 1 | T × T |
| <span class="k5">V</span> | "times V" | mix the value rows with those weights | (T × T)(T × d) = T × d |

## 🔀 What if it were different?

<div class="wrong"><b>No / √d</b>: with d = 128, scores get ~11× bigger, softmax puts ~100% on one token, and training gradients vanish.</div>
<div class="wrong"><b>No mask M</b>: during training the model can peek at the very token it should predict. It gets a perfect score by cheating and learns nothing useful.</div>
<div class="wrong"><b>softmax over columns instead of rows</b>: each token's weights no longer add to 1; outputs get scaled wrongly.</div>
<div class="wrong"><b>QK instead of QKᵀ</b>: (T × d)(T × d): shapes don't fit.</div>
<div class="right"><b>softmax(QKᵀ/√d + M) V</b> ✓</div>

## 🗣️ Say it out loud

"Softmax of Q K transpose over root d plus M, times V."

## 🤖 Where AI uses it

The heart of every transformer. The T × T table is why long context costs so much: 128K tokens = 16 billion scores per head per layer (FlashAttention computes it in a memory-smart order).

## 🎯 Your quest

`matmul`, `transpose`, `softmax` are given. Use `float("-inf")` for −∞.

1. `causal_mask(T)`: T × T, `0.0` where `j ≤ i`, `-inf` where `j > i`.
2. `attention(Q, K, V, causal)`: the steps above; add the mask only when `causal` is True. d = number of columns of Q.

**Remember:** QKᵀ = every query against every key; softmax goes row by row.

## Review

<details><summary>a · b vs a ⊙ b?</summary>Dot gives one number; ⊙ gives a list.</details>
<details><summary>Why do layers need a bending function?</summary>Otherwise stacked layers collapse into one matrix.</details>
