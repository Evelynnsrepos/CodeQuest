---
title: Count every parameter of GPT-2
minutes: 40
xp: 50
hint: gpt2_params: one name per table row: ln1 = 2 * d, qkv = 3 * d * d + 3 * d, proj = d * d + d, ln2 = 2 * d, up = 4 * d * d + 4 * d, down = 4 * d * d + d
hint: Then per_layer = ln1 + qkv + proj + ln2 + up + down, and return vocab * d + ctx * d + layers * per_layer + 2 * d
hint: mlp_share: mlp = (4 * d * d + 4 * d) + (4 * d * d + d), layer = 12 * d * d + 13 * d, return mlp / layer
---
# Where do 124 million parameters come from?

⏱️ About 40 minutes

> **Warm-up:** GPT-2 small has width 768 and 12 layers. Guess: are most of its parameters in attention, in the MLPs, or in the embedding table?

Count them. GPT-2 uses LayerNorm (gain and bias, `2d` each), biases on every matrix, a learned position table, and a tied output head.

| Part | Parameters |
|---|---|
| token embeddings | `vocab · d` |
| position embeddings | `ctx · d` |
| per layer: LayerNorm 1 | `2d` |
| per layer: attention Q, K, V (one `d × 3d` matrix + bias) | `3d² + 3d` |
| per layer: attention output projection | `d² + d` |
| per layer: LayerNorm 2 | `2d` |
| per layer: MLP up (`d → 4d`) + bias | `4d² + 4d` |
| per layer: MLP down (`4d → d`) + bias | `4d² + d` |
| final LayerNorm | `2d` |
| output head | 0 (tied to the token embeddings) |

One layer is `12d² + 13d`. With `d = 768`: about 7.1 M per layer, 85 M for 12 layers, plus 38.6 M for the token table. Notice the attention matrices don't depend on the number of heads: heads only split `d`.

Why it matters: parameters × bytes per parameter is the file size (LLMs 2), and **training compute ≈ 6 × parameters × tokens** (next lessons).

## 🔬 Take the table apart

`d²` means d × d. `3d² + 3d` means 3·d·d + 3·d. In Python: `3 * d * d + 3 * d`.

**Why these sizes?** A matrix from d inputs to 3d outputs has d × 3d = 3d² weights, plus one bias per output = 3d. A LayerNorm has a γ and a β per feature: 2d.

**One layer added up:**
- d² terms: 3 + 1 + 4 + 4 = **12d²**
- d terms: 2 + 3 + 1 + 2 + 4 + 1 = **13d**

So one layer = 12d² + 13d. The MLP part (up + down) = 8d² + 5d.

**Numbers, d = 768:** d² = 589,824. MLP = 8 × 589,824 + 5 × 768 = 4,718,592 + 3,840 = 4,722,432. Layer = 12 × 589,824 + 13 × 768 = 7,077,888 + 9,984 = 7,087,872. Share = 4,722,432 / 7,087,872 ≈ **0.666**: two thirds of every layer is MLP.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `qkv = 3 * d * d + 3 * d` | | one name per table row, easier to check |
| `layers * per_layer` | | every layer is the same size |
| `+ 2 * d` | | the final LayerNorm |

### 👀 Worked example: a tiny GPT

vocab 10, ctx 4, d = 2, 1 layer. Per layer: 12·4 + 13·2 = 48 + 26 = 74. Total: 10·2 + 4·2 + 1·74 + 2·2 = 20 + 8 + 74 + 4 = **106**.

## 🎯 Your quest

`gpt2_params(vocab, ctx, d, layers)`: replace `return 0` with:

1. `    ln1 = 2 * d`
2. `    qkv = 3 * d * d + 3 * d`
3. `    proj = d * d + d`
4. `    ln2 = 2 * d`
5. `    up = 4 * d * d + 4 * d`
6. `    down = 4 * d * d + d`
7. `    per_layer = ln1 + qkv + proj + ln2 + up + down`
8. `    return vocab * d + ctx * d + layers * per_layer + 2 * d`

`mlp_share(d)`: replace `return 0.0` with:

1. `    mlp = (4 * d * d + 4 * d) + (4 * d * d + d)`
2. `    layer = 12 * d * d + 13 * d`
3. `    return mlp / layer`

Check yourself: GPT-2 small (`50257, 1024, 768, 12`) is **124,439,808**.

## Review

<details><summary>What does a tied output head reuse?</summary>The token embedding table, to turn the final vector into a score per token.</details>
<details><summary>In the forward pass, which of Q, K, V get RoPE?</summary>Q and K only.</details>
