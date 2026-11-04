---
title: Hinton's Forward-Forward algorithm
xp: 45
---
# Learning without a backward pass

> **Warm-up:** backprop needs to store every layer's activations and send error signals backwards through the whole network. Does your brain plausibly do that?

Probably not, and that question drove Geoffrey Hinton's **Forward-Forward (FF) algorithm** (*"The Forward-Forward Algorithm: Some Preliminary Investigations"*, 2022). It replaces the forward + backward pass with **two forward passes**:

- a **positive** pass on real data (e.g. an image with its *correct* label written into it), and
- a **negative** pass on fake data (e.g. the same image with a *wrong* label).

Each layer has its own local objective. It measures its **goodness**, the sum of its squared activities:

```
G = Σⱼ hⱼ²
P(positive) = σ(G − θ)          θ: a threshold, σ: sigmoid
```

and trains to make `G` **high for positive** and **low for negative** data, using only its own input and output. A common per-layer loss:

```
loss = softplus(θ − G_pos) + softplus(G_neg − θ)        softplus(x) = log(1 + eˣ)
```

Before passing activities to the next layer, FF **normalizes** them to unit length. Otherwise the next layer could just read off the previous layer's goodness (the vector's length) and learn nothing new; normalizing keeps only the *direction*, the actual features.

| | Backprop | Forward-Forward |
|---|---|---|
| Passes per example | 1 forward + 1 backward | 2 forward (positive, negative) |
| Error signal | global, chain rule through all layers | local, per layer |
| Must store activations for backward | yes | no |
| Needs negative data | no | yes, and choosing it is hard |
| Results so far | state of the art everywhere, every LLM | works on small tasks (MNIST, CIFAR), behind backprop |

FF is interesting research (biological plausibility, low-power analog hardware, learning while streaming) but every model you'll use or fine-tune is trained with backprop. That's why this course taught backprop first.

## Your quest

1. `goodness(h)`: the sum of squares.
2. `softplus(x)`: `math.log(1 + math.exp(x))`. (For large `x` this overflows; return `x` itself when `x > 30`, since the difference is negligible.)
3. `ff_loss(h_pos, h_neg, theta)`: the per-layer loss above.
4. `normalize(h)`: divide by the vector's length (return `h` unchanged if the length is 0).

## Review

<details><summary>How many bytes per parameter does full fine-tuning with AdamW need?</summary>About 16 (BF16 weights and grads, FP32 master weights, Adam's m and v), plus activations.</details>
<details><summary>Why is QLoRA possible on 12 GB?</summary>The frozen base model is stored in 4 bits and only small added matrices are trained at full precision.</details>
