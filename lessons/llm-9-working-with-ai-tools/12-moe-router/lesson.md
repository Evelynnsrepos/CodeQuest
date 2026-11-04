---
title: The MoE router and load balancing
xp: 60
---
# Pick 2 experts out of 64, and keep them all busy

> **Warm-up:** Qwen3-30B-A3B has 30B parameters but only ~3B work per token. Who decides which 3B?

**In one sentence:** a small router scores every expert for each token, keeps the top k, softmaxes their scores into mixing weights, and a load-balancing loss stops it from sending everything to the same few experts.

## 🪜 Plain words

- The feed-forward part of each layer is split into **E experts** (separate small MLPs).
- The **router** is one matrix: scores = W_g · x, one score per expert.
- Keep the **top k** scores, softmax just those → weights g that add to 1.
- Output = g₁ · expert₁(x) + g₂ · expert₂(x) + …

Compute follows the **active** experts; memory needs **all** of them (LLMs 2).

Left alone, the router gets lazy and sends most tokens to a favourite expert, which then learns everything while others starve. The **load-balancing loss** punishes that: it's smallest when every expert gets an equal share.

## 🪜 With numbers

Scores for 4 experts: (2, 1, 0.5, −1), k = 2 → experts 0 and 1, softmax(2, 1) = **(0.731, 0.269)**.

Load balance, E = 4. f = share of tokens each expert got, P = router's average probability for it:

- Balanced: f = P = (0.25, 0.25, 0.25, 0.25): 4 · Σ fP = 4 · 0.25 = **1** (the minimum)
- Skewed: f = (0.5, 0.3, 0.1, 0.1), P = (0.4, 0.3, 0.2, 0.1): 4 · 0.32 = **1.28**
- Collapsed: f = P = (1, 0, 0, 0): **4**

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `W_g` | "W g" | router weights | |
| `TopK( )` | "top k" | keep the k biggest | `sorted(...)[:k]` |
| `gᵢ` | "g i" | mixing weight of expert i | |
| `FFNᵢ(x)` | "F F N i of x" | expert i's output | |
| `E` | "E" | number of experts | |
| `fᵢ`, `Pᵢ` | "f i", "P i" | token share, mean router probability | |
| `α` | "alpha" | how strong the balancing push is (small, e.g. 0.01) | |

## 🔬 Take the formulas apart

<div class="formula"><span class="k1">g</span> = softmax( <span class="k2">TopK</span>( <span class="k3">W_g x</span> ) ), &nbsp; <span class="k4">y</span> = Σ<sub>i ∈ TopK</sub> <span class="k1">gᵢ</span> · <span class="k5">FFNᵢ(x)</span></div>

<div class="formula"><span class="k6">L_balance</span> = α · <span class="k2">E</span> · Σᵢ <span class="k3">fᵢ</span> · <span class="k4">Pᵢ</span></div>

| Piece | Means | Example |
|---|---|---|
| <span class="k3">W_g x</span> | one score per expert | (2, 1, 0.5, −1) |
| <span class="k2">TopK</span> | keep the best k | experts 0, 1 |
| <span class="k1">g</span> | their softmax weights | (0.731, 0.269) |
| <span class="k6">L_balance</span> | E · Σ fP, scaled by α | 1 balanced, 4 collapsed |

## 🔀 What if it were different?

<div class="alt"><b>Softmax over all experts, then take the top 2</b>: weights 0.61 and 0.22. They don't add to 1, and that is fine: it's a real design used by Switch Transformer, GShard and Qwen's MoE models. The router then also learns how much to trust the chosen experts at all. It just gives different numbers from Mixtral's "top 2 first, then softmax", which is what this lesson builds, so the check expects that one.</div>
<div class="wrong"><b>No balancing loss</b>: a few experts get everything; the "30B" model behaves like a much smaller one.</div>
<div class="wrong"><b>Only use f (not P) in the loss</b>: f comes from a hard top-k choice and has no gradient; P is what lets training push the router.</div>
<div class="right">softmax of the top-k scores; α·E·Σ fP is 1 when balanced ✓</div>

## 🎯 Your quest

1. `route(scores, k)`: return a list of `(expert_index, weight)` for the top k, highest score first.
2. `moe_output(scores, k, expert_outputs)`: `expert_outputs[i]` is expert i's output vector; mix the top k with their weights.
3. `balance_loss(f, P, alpha=1.0)`.

**Remember:** route to the top k, mix by softmax, keep everyone busy.

## Review

<details><summary>Expected tokens per pass for α = 0.8, k = 4?</summary>About 3.36.</details>
