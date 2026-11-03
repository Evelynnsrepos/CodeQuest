---
title: Checkpoint: a tiny network in matrices
xp: 80
---
# Put it all together

> **Warm-up:** 4 examples with 3 features each go into a layer with 5 neurons, then a layer with 2 outputs. Write down every shape.

(Inputs 4 × 3. First weights 5 × 3. Hidden 4 × 5. Second weights 2 × 5. Output 4 × 2.)

## 🪜 Plain words

A **two-layer network** on a whole batch: send every example through layer 1 (weighted sums, plus bias, bend), then through layer 2 (weighted sums, plus bias). Each example is a row, so all examples go at once with matrix products.

## 🔬 Take the formula apart

<div class="formula"><span class="k1">H</span> = ReLU( <span class="k2">X</span> <span class="k3">W₁ᵀ</span> <span class="k4">+ b₁</span> ), &nbsp; <span class="k5">OUT</span> = <span class="k1">H</span> <span class="k6">W₂ᵀ</span> + b₂</div>

| Piece | Say it | Means | Shape |
|---|---|---|---|
| <span class="k2">X</span> | "X" | the batch: one example per row | batch × d_in |
| <span class="k3">W₁ᵀ</span> | "W one transpose" | layer-1 weights (stored out × in, flipped to fit) | d_in × d_hidden |
| <span class="k4">+ b₁</span> | "plus b one" | one bias per neuron, added to **every** row | d_hidden |
| ReLU( ) | "rel-you of" | negatives → 0 | |
| <span class="k1">H</span> | "H" | hidden layer output | batch × d_hidden |
| <span class="k6">W₂ᵀ</span> | "W two transpose" | layer-2 weights, flipped | d_hidden × d_out |
| <span class="k5">OUT</span> | "out" | final outputs | batch × d_out |

## 🔀 What if it were different?

<div class="wrong"><b>X W₁</b> (no transpose): (batch × 3)(5 × 3): shapes don't fit.</div>
<div class="wrong"><b>ReLU after layer 2 too</b>: outputs could never be negative; fine for some tasks, wrong for others (like logits).</div>
<div class="wrong"><b>No ReLU in the middle</b>: the two layers collapse into one matrix W₂W₁.</div>
<div class="right">ReLU(XW₁ᵀ + b₁) W₂ᵀ + b₂ ✓</div>

## 🎯 Your quest

`matmul` and `transpose` are given.

1. `mlp_batch(X, W1, b1, W2, b2)`: return OUT.
2. `mlp_flops(batch, d_in, d_hidden, d_out)`: FLOPs of the two matrix products (`2·m·n·p` each).
3. `shapes(batch, d_in, d_hidden, d_out)`: `(X, W1, H, W2, OUT)` shapes as `(rows, cols)`.

Next: Math 3, calculus: how to find out which way to change all these weights.

## Review

<details><summary>What does power iteration find?</summary>The eigenvector with the biggest stretch.</details>
<details><summary>Shape of (m × n)(n × p)?</summary>m × p.</details>
<details><summary>LoRA trainable numbers for d × k at rank r?</summary>d·r + r·k.</details>
