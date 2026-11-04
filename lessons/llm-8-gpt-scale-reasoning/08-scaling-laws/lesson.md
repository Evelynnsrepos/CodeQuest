---
title: Scaling laws and compute-optimal training
xp: 60
---
# Bigger model or more data?

> **Warm-up:** you have a fixed GPU budget. Is it better to train a 10B model on 20B tokens or a 1B model on 200B tokens?

**Scaling laws** answer this. Kaplan et al. (OpenAI, 2020) found that loss falls as a smooth **power law** in parameters `N`, data `D` and compute `C`, over many orders of magnitude. Hoffmann et al. (DeepMind, 2022, the **Chinchilla** paper) refit it and found models of that time were too big for their data. Their fit:

```
L(N, D) = E + A / N^α + B / D^β
E = 1.69, A = 406.4, B = 410.7, α = 0.34, β = 0.28
```

`E` is the irreducible loss (the entropy of text itself); the other terms shrink as the model and data grow.

Training compute is about **`C ≈ 6·N·D`** FLOPs: 2 per parameter per token for the forward pass, 4 for the backward pass. Minimizing `L` under a fixed `C` gives roughly **20 tokens per parameter**, so with `D = 20N`: `C = 120·N²`, `N = √(C / 120)`.

**Possibly outdated / contested:**

- A 2024 replication (Besiroglu et al.) refit Chinchilla's data and got different constants; the "≈ 20 tokens per parameter" conclusion held up roughly, the exact numbers didn't.
- Chinchilla-optimal minimizes *training* cost. Models you'll run millions of times are deliberately **over-trained** to be small and cheap at inference: Llama 3 8B saw about 15 T tokens, nearly 1,900 tokens per parameter. That's why small modern models are so good.
- Scaling laws predict loss, not specific abilities; some skills appear suddenly on benchmarks ("emergence"), though part of that is an artefact of all-or-nothing metrics.

## Your quest

1. `train_flops(N, D)`: `6·N·D`.
2. `chinchilla_optimal(C)`: return `(N, D)` with `N = √(C / 120)` and `D = 20·N`.
3. `predicted_loss(N, D)`: the formula with the constants above.

## Review

<details><summary>What loss should a fresh model with vocabulary V start at?</summary>About ln V.</details>
<details><summary>Why warm up the learning rate?</summary>Adam's moment estimates are unreliable in the first steps; a big LR then can blow up training.</details>
