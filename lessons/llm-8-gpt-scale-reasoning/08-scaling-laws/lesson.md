---
title: Scaling laws and compute-optimal training
minutes: 45
xp: 60
hint: train_flops: return 6 * N * D
hint: chinchilla_optimal: N = math.sqrt(C / 120), D = 20 * N, return (N, D)
hint: predicted_loss: return 1.69 + 406.4 / N ** 0.34 + 410.7 / D ** 0.28
---
# Bigger model or more data?

⏱️ About 45 minutes

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

## 🔬 Take the formulas apart

**Chinchilla's rule of thumb:** D = 20·N (20 tokens per parameter) and C = 6·N·D (LLMs 4, lesson 5). Put the first into the second:

1. C = 6 · N · (20 · N) = 120 · N²
2. Divide both sides by 120: N² = C / 120
3. Take the square root: <span class="k1">N = √(C / 120)</span>

Numbers, C = 10²¹: C / 120 ≈ 8.33 × 10¹⁸, √ ≈ 2.9 × 10⁹. So **N ≈ 2.9B** parameters and D = 20 × 2.9B ≈ **58B** tokens.

**The loss law** <div class="formula">L = <span class="k1">E</span> + <span class="k2">A / N^α</span> + <span class="k3">B / D^β</span></div>
- <span class="k1">E = 1.69</span>: the floor no model can beat (the text's own randomness).
- <span class="k2">A / N^α</span>: the penalty for a small model. `N^α` ("N to the alpha") with α = 0.34: a power with a decimal. 2.9B^0.34 ≈ 1649, and 406.4 / 1649 ≈ **0.246**.
- <span class="k3">B / D^β</span>: the penalty for too little data, β = 0.28. 58B^0.28 is about 1032, and 410.7 / 1032 ≈ **0.398**.
- L ≈ 1.69 + 0.246 + 0.398 ≈ **2.335**.

Bigger N or D makes each penalty smaller, but never below E. Same budget with a 10× bigger model and 10× fewer tokens: the data penalty grows more than the model penalty shrinks → 2.562, worse.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `math.sqrt(C / 120)` | | √(C / 120) |
| `N ** 0.34` | "N to the power 0.34" | powers with decimals work too |
| `406.4 / N ** 0.34` | | `**` is done before `/`, so this is 406.4 / (N^0.34) |
| `return (N, D)` | | two numbers together |

### 👀 Worked example: a smaller budget

C = 1.2 × 10¹⁹ → C / 120 = 10¹⁷ → √ ≈ 3.16 × 10⁸. A 316M-parameter model on 20 × 316M ≈ 6.3B tokens.

## 🎯 Your quest

`train_flops(N, D)`: replace `return 0` with `    return 6 * N * D`

`chinchilla_optimal(C)`: replace `return (0, 0)` with:

1. `    N = math.sqrt(C / 120)`
2. `    D = 20 * N`
3. `    return (N, D)`

`predicted_loss(N, D)`: replace `return 0.0` with `    return 1.69 + 406.4 / N ** 0.34 + 410.7 / D ** 0.28`

## Review

<details><summary>What loss should a fresh model with vocabulary V start at?</summary>About ln V.</details>
<details><summary>Why warm up the learning rate?</summary>Adam's moment estimates are unreliable in the first steps; a big LR then can blow up training.</details>
