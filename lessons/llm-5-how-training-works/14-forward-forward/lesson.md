---
title: Hinton's Forward-Forward algorithm
minutes: 40
xp: 45
hint: goodness: total = 0, for x in h: total = total + x * x, return total
hint: softplus: if x > 30: return x. After the if: return math.log(1 + math.exp(x))
hint: ff_loss: return softplus(theta - goodness(h_pos)) + softplus(goodness(h_neg) - theta)
hint: normalize: length = math.sqrt(goodness(h)), if length == 0: return h, then out = [], for x in h: out.append(x / length), return out
---
# Learning without a backward pass

⏱️ About 40 minutes

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

## 🔬 Take the formulas apart

**Goodness** <div class="formula">G = <span class="k1">Σⱼ</span> <span class="k2">hⱼ²</span></div>
<span class="k2">hⱼ</span> is the activity of neuron j. Square each one and <span class="k1">add them up</span>. For real = [2, 1.5, 0, 1]: 4 + 2.25 + 0 + 1 = **7.25**.

**Softplus** <div class="formula">softplus(x) = log(1 + eˣ)</div>
A smooth version of "max(0, x)": very negative x → almost 0, big x → almost x.
- x = −5: e⁻⁵ ≈ 0.0067, log(1.0067) ≈ **0.0067** (almost 0).
- x = 0: log(1 + 1) = log 2 ≈ **0.693**.
- x = 40: e⁴⁰ is huge and log(1 + e⁴⁰) ≈ 40. Python's `math.exp` overflows for very big x, so you return x itself when x > 30.

**The layer's loss** <div class="formula">loss = softplus(<span class="k1">θ − G_pos</span>) + softplus(<span class="k2">G_neg − θ</span>)</div>
- θ ("theta") is the threshold, here 2.
- <span class="k1">θ − G_pos</span>: negative when the real example's goodness is **above** θ (good!) → small loss.
- <span class="k2">G_neg − θ</span>: negative when the fake example's goodness is **below** θ (good!) → small loss.

Numbers: G_pos = 7.25, G_neg = 0.3.
1. softplus(2 − 7.25) = softplus(−5.25) ≈ 0.005
2. softplus(0.3 − 2) = softplus(−1.7) ≈ 0.168
3. loss ≈ **0.173**. Swap them and it's about 7.1: the layer would be badly wrong.

**Normalize** <div class="formula">h / |h|, &nbsp; |h| = √G</div>
Divide by the length (LLMs 4, lesson 3), which is √(goodness). real: √7.25 ≈ 2.693, so [2/2.693, 1.5/2.693, 0, 1/2.693] ≈ **[0.743, 0.557, 0.0, 0.371]**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `x * x` | | x squared |
| `if x > 30: return x` | | the early exit for big numbers |
| `math.log(1 + math.exp(x))` | | log(1 + eˣ) |
| `goodness(h_pos)` | | your own function, used inside another |
| `if length == 0:` | "if length equals 0" | `==` compares; a single `=` would store |

### 👀 Worked example: goodness of [3, 4]

```python
total = 0
for x in [3, 4]:
    total = total + x * x     # 9, then 25
print(total)                  # 25: the goodness
print(math.sqrt(total))       # 5.0: the length, used to normalize → [0.6, 0.8]
```

## 🎯 Your quest

`goodness(h)`: replace `return 0` with:

1. `    total = 0`
2. `    for x in h:`
3. `        total = total + x * x`
4. `    return total`

`softplus(x)`: replace `return 0` with:

1. `    if x > 30:`
2. `        return x`
3. `    return math.log(1 + math.exp(x))`

`ff_loss(h_pos, h_neg, theta)`: replace `return 0` with `    return softplus(theta - goodness(h_pos)) + softplus(goodness(h_neg) - theta)`

`normalize(h)`: replace `return h` with:

1. `    length = math.sqrt(goodness(h))`
2. `    if length == 0:`
3. `        return h`
4. `    out = []`
5. `    for x in h:`
6. `        out.append(x / length)`
7. `    return out`

## Review

<details><summary>How many bytes per parameter does full fine-tuning with AdamW need?</summary>About 16 (BF16 weights and grads, FP32 master weights, Adam's m and v), plus activations.</details>
<details><summary>Why is QLoRA possible on 12 GB?</summary>The frozen base model is stored in 4 bits and only small added matrices are trained at full precision.</details>
