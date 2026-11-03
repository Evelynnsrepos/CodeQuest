---
title: Rank and low-rank matrices (LoRA)
xp: 50
---
# Big matrices built from thin ones

> **Warm-up:** a 4096 × 4096 matrix has 16.8 million numbers. Could you describe some big matrices with far fewer numbers?

**In one sentence:** a matrix's rank is how many truly independent directions it contains, and a low-rank matrix can be stored as the product of two thin matrices.

## 🔣 New symbols

| Symbol | Say it | Means |
|---|---|---|
| `rank(A)` | "the rank of A" | number of independent rows (= independent columns) |
| `B ∈ ℝ^(d×r)`, `A ∈ ℝ^(r×k)` | | two thin matrices, `r` much smaller than d and k |
| `BA` | "B A" | a d × k matrix with rank at most r |
| `uvᵀ` | "u v transpose" / "outer product" | (d × 1)(1 × k) = a d × k matrix of rank 1: entry (i, j) = `uᵢvⱼ` |
| `W₀ + (α/r)·BA` | "W nought plus alpha over r B A" | LoRA's update |

## The idea

- A row is **dependent** if it's a linear combination of others: in `[[1, 2], [2, 4]]` the second row is 2 × the first, so rank = 1. Only one "direction" of information.
- **Outer product** `uvᵀ`: every row is a multiple of `vᵀ`, so it has rank 1. Built from only `d + k` numbers instead of `d·k`.
- `BA` with inner size `r` is a **sum of r rank-1 matrices**: rank ≤ r.

**LoRA** (LLMs 6) bets that the *change* a fine-tune needs is low-rank. Freeze `W₀`, learn only `B` and `A`:

```
W = W₀ + (α / r) · B A
```

Parameters: `d·r + r·k` instead of `d·k`. For 4096 × 4096 with r = 16: `2 · 4096 · 16 = 131,072`, under 1%. `B` starts at **zero**, so at the start `W = W₀` exactly.

## 🗣️ Say it out loud

`ΔW = BA` → "delta W equals B times A" → "the change to the weights is the product of two thin matrices."

## 🧮 Worked example

`u = (1, 2)`, `v = (3, 0, 1)`: `uvᵀ = [[3, 0, 1], [6, 0, 2]]`. Row 2 = 2 × row 1 → rank 1. Six numbers stored as five.

## 🤖 Where AI uses it

LoRA and QLoRA, compressing layers, analysing what fine-tuning changed. Also "attention is low-rank" research, and DeepSeek's MLA compressing keys and values into a small latent vector.

## 🎯 Your quest

1. `outer(u, v)`: the matrix with entries `uᵢvⱼ`.
2. `lora_params(d, k, r)`: `d·r + r·k`.
3. `lora_weight(W0, B, A, alpha, r)`: `W₀ + (α/r)·BA` (use the `matmul` given).

**Remember:** rank = number of independent directions; LoRA trains two thin matrices instead of one fat one.

## Review

<details><summary>What does the causal mask contain above the diagonal?</summary>−∞, so softmax gives those positions weight 0.</details>
<details><summary>Shape of QKᵀ for T tokens?</summary>T × T.</details>
