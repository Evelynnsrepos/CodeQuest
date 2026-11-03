---
title: Checkpoint: a tiny network in matrices
xp: 80
---
# Put it all together

> **Warm-up:** without looking, write down the shapes: input batch X (4 examples, 3 features), first layer to 5 hidden units, second layer to 2 outputs. What shape is every matrix and every result?

(X: 4 × 3. W₁: 5 × 3, so `XW₁ᵀ`: 4 × 5. W₂: 2 × 5, so the output is 4 × 2.)

This checkpoint uses everything from this course: vectors, dot products, matrix products, transpose, layers, element-wise operations, shapes and FLOPs.

A **two-layer MLP** on a whole batch at once (PyTorch convention: weights stored as out × in, examples as rows):

```
H   = ReLU(X W₁ᵀ + b₁)        bias added to every row
OUT = H W₂ᵀ + b₂
```

🗣️ "H is ReLU of X times W one transpose plus b one; the output is H times W two transpose plus b two."

## 🎯 Your quest

`matmul` and `transpose` are given.

1. `mlp_batch(X, W1, b1, W2, b2)`: return OUT (a list of rows).
2. `mlp_flops(batch, d_in, d_hidden, d_out)`: FLOPs of the two matrix products only (`2·m·n·p` each, lesson 8).
3. `shapes(batch, d_in, d_hidden, d_out)`: return the tuple of shapes `(X, W1, H, W2, OUT)`, each as `(rows, cols)`.

Next up: Math 3, calculus: how to find out which way to change all these weights.

## Review

<details><summary>What does power iteration find?</summary>The eigenvector with the largest |eigenvalue|.</details>
<details><summary>Shape of (m × n)(n × p)?</summary>m × p.</details>
<details><summary>How many trainable numbers in LoRA for d × k with rank r?</summary>d·r + r·k.</details>
