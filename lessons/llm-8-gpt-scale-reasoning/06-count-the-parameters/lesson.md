---
title: Count every parameter of GPT-2
xp: 50
---
# Where do 124 million parameters come from?

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

## Your quest

1. `gpt2_params(vocab, ctx, d, layers)`: the total from the table.
2. `mlp_share(d)`: the fraction of **one layer's** parameters that are in the MLP (both matrices with their biases).

Check yourself: GPT-2 small (`50257, 1024, 768, 12`) is **124,439,808**.

## Review

<details><summary>What does a tied output head reuse?</summary>The token embedding table, to turn the final vector into a score per token.</details>
<details><summary>In the forward pass, which of Q, K, V get RoPE?</summary>Q and K only.</details>
