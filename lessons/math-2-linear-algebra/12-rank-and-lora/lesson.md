---
title: Rank and low-rank matrices (LoRA)
xp: 50
---
# Big matrices built from thin ones

> **Warm-up:** a 4096 × 4096 matrix holds 16.8 million numbers. Could some big matrices be described with far fewer?

**In one sentence:** the rank of a matrix counts its truly different directions, and a low-rank matrix can be stored as two thin matrices multiplied together.

## 🪜 Plain words

Look at `[[1, 2], [2, 4]]`. The second row is just the first row doubled: it carries **no new information**. Only one "real" row → **rank 1**.

Take a column of numbers and a row of numbers and multiply every pair: you get a full grid, but you only needed the column and the row to make it. A big grid built like that is cheap to store.

**LoRA** uses this: instead of changing all 16.8 million numbers during fine-tuning, it learns two thin matrices whose product is the change.

## 🪜 With numbers

Column (1, 2), row (3, 0, 1) → every pair multiplied:

```
1·3  1·0  1·1      [3 0 1]
2·3  2·0  2·1  =   [6 0 2]
```

Six numbers in the grid, but made from 5. For 4096 × 4096 with "thickness" 16: 4096·16 + 16·4096 = **131,072** numbers instead of 16.8 million (under 1%).

## 🔣 The signs

| Sign | Say it | Means |
|---|---|---|
| `rank(A)` | "the rank of A" | number of truly independent rows |
| `uvᵀ` | "u v transpose" / "outer product" | column times row = a rank-1 grid: entry (i, j) = uᵢvⱼ |
| `r` | "r" | the rank / thickness of the thin matrices |
| `W₀` | "W nought" | the original frozen weights |
| `α` | "alpha" | a scaling knob |
| `ΔW` | "delta W" | the change to the weights |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">W</span> = <span class="k2">W₀</span> + <span class="k3">(α / r)</span> · <span class="k4">B</span><span class="k5">A</span></div>

| Piece | Say it | Means | Shapes for a d × k weight |
|---|---|---|---|
| <span class="k1">W</span> | "W" | the weight actually used | d × k |
| <span class="k2">W₀</span> | "W nought" | original weights, **frozen** (not trained) | d × k |
| <span class="k3">(α / r)</span> | "alpha over r" | how strongly the change counts | a number, like 32/16 = 2 |
| <span class="k4">B</span> | "B" | thin matrix, **starts at all zeros** | d × r |
| <span class="k5">A</span> | "A" | thin matrix, starts random | r × k |
| <span class="k4">B</span><span class="k5">A</span> | "B A" | their product: the change ΔW, rank ≤ r | d × k |

## 🔀 What if it were different?

<div class="wrong"><b>B starts random too</b>: on step 0, W = W₀ + noise. The model is damaged before training even starts. With B = 0, step 0 is exactly the original model.</div>
<div class="wrong"><b>AB instead of BA</b>: (r × k)(d × r) only fits if k = d, and then gives an r × r matrix: the wrong shape to add to W₀.</div>
<div class="wrong"><b>r = 4096</b>: no savings at all; you'd train as many numbers as full fine-tuning.</div>
<div class="right"><b>W₀ + (α/r)·BA</b> with small r and B = 0 at the start ✓</div>

## 🗣️ Say it out loud

"W equals W nought plus alpha over r times B A."

## 🤖 Where AI uses it

LoRA and QLoRA (LLMs 6), compressing layers, DeepSeek's MLA (keys and values squeezed through a small latent).

## 🎯 Your quest

1. `outer(u, v)`: grid with entries `uᵢvⱼ`.
2. `lora_params(d, k, r)`: `d·r + r·k`.
3. `lora_weight(W0, B, A, alpha, r)`: `W₀ + (α/r)·BA`.

**Remember:** rank = number of truly different directions; LoRA trains two thin matrices.

## Review

<details><summary>What's above the diagonal in the causal mask?</summary>−∞.</details>
<details><summary>Shape of QKᵀ for T tokens?</summary>T × T.</details>
