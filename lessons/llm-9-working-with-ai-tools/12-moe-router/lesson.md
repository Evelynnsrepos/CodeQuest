---
title: The MoE router and load balancing
minutes: 55
xp: 60
hint: route, top k: top = [], for step in range(k): best = None, then for i in range(len(scores)): if i not in top: if best is None or scores[i] > scores[best]: best = i. Then top.append(best)
hint: route, softmax: m = scores[top[0]], then for i in top: e = math.exp(scores[i] - m), es.append(e) and total = total + e
hint: route, the pairs: for j in range(len(top)): out.append((top[j], es[j] / total))
hint: moe_output: out = [0.0] * len(expert_outputs[0]), then for i, g in route(scores, k): for j in range(len(out)): out[j] = out[j] + g * expert_outputs[i][j]
hint: balance_loss: total = 0, for i in range(len(f)): total = total + f[i] * P[i]. Then return alpha * len(f) * total
---
# Pick 2 experts out of 64, and keep them all busy

⏱️ About 55 minutes

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
| `TopK( )` | "top k" | keep the k biggest | the loop in `route` |
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

## 🔬 The formulas, one small step at a time

**Softmax of the top 2 scores (2, 1).** Softmax turns scores into weights that add up to 1, and a bigger score gets more weight.

1. `e` is a fixed number, about 2.718. `eˣ` ("e to the x") is e multiplied by itself x times. In Python: `math.exp(x)`.
2. First subtract the biggest score from each score: 2 − 2 = 0 and 1 − 2 = −1. (This keeps the numbers small. It does not change the answer.)
3. e⁰ = **1** (anything to the power 0 is 1). e⁻¹ = 1 / 2.718 = **0.368**.
4. Add them: 1 + 0.368 = 1.368.
5. Divide each by that total: 1 / 1.368 = **0.731** and 0.368 / 1.368 = **0.269**. Together: 1.

**The mix `y = Σ gᵢ · FFNᵢ(x)`.** `Σ` (the Greek letter sigma) means "add up, for every i underneath it". `i ∈ TopK` means "i is one of the chosen experts". With expert 0's output (1, 0) and expert 1's output (0, 1):

- 0.731 × (1, 0) = (0.731, 0)
- 0.269 × (0, 1) = (0, 0.269)
- add them: **(0.731, 0.269)**

**The balance loss `α · E · Σ fᵢ · Pᵢ`.** For the skewed example, f = (0.5, 0.3, 0.1, 0.1) and P = (0.4, 0.3, 0.2, 0.1):

1. Multiply each pair: 0.5 × 0.4 = 0.20, 0.3 × 0.3 = 0.09, 0.1 × 0.2 = 0.02, 0.1 × 0.1 = 0.01.
2. Σ adds them: 0.20 + 0.09 + 0.02 + 0.01 = 0.32.
3. Times E (4 experts): 4 × 0.32 = 1.28. Times α = 1: **1.28**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `for step in range(k):` | "k times" | repeats the lines under it k times. `step` itself isn't used. |
| `best = None` | | "no best found yet" |
| `if i not in top:` | | skips experts you already picked |
| `best is None or scores[i] > scores[best]` | | true for the first candidate, or for one with a higher score |
| `math.exp(x)` | "e to the x" | needs `import math` at the top (already there) |
| `out.append((i, w))` | | the double brackets: the inner `( )` makes a **pair** that is added as one item |
| `[0.0] * 3` | "a list of three zeros" | `[0.0, 0.0, 0.0]` |
| `for i, g in route(scores, k):` | | each item is a pair (expert, weight); Python unpacks it |
| `out[j] = out[j] + g * v` | | adds a weighted value into position j |
| `len(f)` | | the number of experts, E |

### 👀 Worked example: the 2 highest marks

```python
marks = [6, 9, 4, 8]
top = []
for step in range(2):
    best = None
    for i in range(len(marks)):
        if i not in top:
            if best is None or marks[i] > marks[best]:
                best = i
    top.append(best)
print(top)
```

Round 1 (`top` is empty):

1. `i` = 0: `best` is None → `best` = 0 (mark 6).
2. `i` = 1: 9 > 6 → `best` = 1. `i` = 2: 4 > 9? No. `i` = 3: 8 > 9? No.
3. `top` = `[1]`.

Round 2: `i` = 1 is skipped (already in `top`). The best of 6, 4, 8 is 8 at position 3 → `top` = `[1, 3]`. Highest first.

## 🎯 Your quest

1. `route(scores, k)`: return a list of `(expert_index, weight)` for the top k, highest score first.
2. `moe_output(scores, k, expert_outputs)`: `expert_outputs[i]` is expert i's output vector; mix the top k with their weights.
3. `balance_loss(f, P, alpha=1.0)`.

**Part 1:** `route`. Replace `return []` with:

1. `top = []`
2. `for step in range(k):`
3. `    best = None`
4. `    for i in range(len(scores)):`
5. `        if i not in top:`
6. `            if best is None or scores[i] > scores[best]:`
7. `                best = i`
8. `    top.append(best)`
9. `m = scores[top[0]]`
10. `es = []`
11. `total = 0`
12. `for i in top:`
13. `    e = math.exp(scores[i] - m)`
14. `    es.append(e)`
15. `    total = total + e`
16. `out = []`
17. `for j in range(len(top)):`
18. `    out.append((top[j], es[j] / total))`
19. `return out`

Line 9: `top[0]` is the expert with the highest score, so `m` is the biggest score (step 2 of the softmax).

**Part 2:** `moe_output`. Replace `return []` with:

1. `out = [0.0] * len(expert_outputs[0])`
2. `for i, g in route(scores, k):`
3. `    for j in range(len(out)):`
4. `        out[j] = out[j] + g * expert_outputs[i][j]`
5. `return out`

**Part 3:** `balance_loss`. Replace `return 0` with:

1. `total = 0`
2. `for i in range(len(f)):`
3. `    total = total + f[i] * P[i]`
4. `return alpha * len(f) * total`

**Remember:** route to the top k, mix by softmax, keep everyone busy.

## Review

<details><summary>Expected tokens per pass for α = 0.8, k = 4?</summary>About 3.36.</details>
