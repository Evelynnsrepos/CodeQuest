---
title: The MLP and residual connections
minutes: 45
xp: 50
hint: gelu: return 0.5 * x * (1 + math.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * x ** 3)))
hint: mlp_block: hidden = matvec(W1, rms_norm(x)), then h = [] and h.append(gelu(v)) for every v in hidden
hint: Then y = matvec(W2, h), and the residual: out.append(x[i] + y[i]) for every i. return out
---
# Where the knowledge lives, and the highway around it

⏱️ About 45 minutes

> **Warm-up:** if each of 32 layers *replaced* the token's vector with its own output, what would happen to information from layer 1 by layer 32? And to the gradient flowing back to layer 1?

Both would fade. The fix is the **residual connection** (from ResNet, 2015): each sub-layer **adds** its result to the vector instead of replacing it.

```
x = x + attention(norm(x))
x = x + mlp(norm(x))
```

This is the **pre-norm** layout used by GPT-2 onwards and Llama: normalize the *input* to each sub-layer, keep the "residual stream" `x` itself untouched. Because of the `+`, the gradient of the output with respect to `x` always contains a plain `1` (chain rule!), so gradients reach the first layers even in very deep stacks.

**The MLP** (feed-forward network) works on each token separately:

```
mlp(x) = W2 · gelu(W1 · x)
```

`W1` widens the vector (usually 4× wider; Llama 3 8B: 4096 → 14336), `W2` brings it back. About two thirds of a transformer's parameters are in the MLPs, and research suggests much of the stored factual knowledge is too.

**GELU** is a smooth version of ReLU: `gelu(x) ≈ 0.5·x·(1 + tanh(√(2/π)·(x + 0.044715·x³)))`. Llama uses **SwiGLU** instead: `W2 · (silu(W1·x) * (W3·x))`, which has a third matrix (that's where 14336 comes from).

## 🔬 Take the formulas apart

**GELU** <div class="formula">gelu(x) ≈ <span class="k1">0.5 · x</span> · (1 + <span class="k2">tanh</span>(<span class="k3">√(2/π)</span> · (x + 0.044715 · x³)))</div>
Don't be scared by the numbers; it's one curve:
- <span class="k2">tanh</span> squashes into −1…1 (LLMs 5, lesson 4), so (1 + tanh(…)) is between 0 and 2.
- <span class="k1">0.5 · x</span> times that: for big positive x it's about 0.5 · x · 2 = **x**; for big negative x it's about 0.5 · x · 0 = **0**. Like ReLU, but smooth around 0.
- <span class="k3">√(2/π)</span> ≈ 0.798 and 0.044715 are fixed numbers that make it match the exact GELU closely.

Numbers: gelu(2) ≈ **1.955** (almost 2), gelu(0) = **0**, gelu(−2) ≈ **−0.045** (almost 0).

**The block** <div class="formula">out = <span class="k1">x</span> + <span class="k2">W2 · gelu(W1 · rms_norm(x))</span></div>
Read inside out: normalize, widen with W1 (2 → 4 here), gelu on each number, narrow with W2 (4 → 2), then **add** <span class="k1">x</span> back: that `+ x` is the residual connection.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `math.tanh(...)`, `math.sqrt(2 / math.pi)` | | tanh, and √(2/π) |
| `x ** 3` | "x cubed" | x · x · x |
| `matvec(W1, rms_norm(x))` | (both given) | normalize, then multiply by W1 |
| `h.append(gelu(v))` | | gelu on each number separately |
| `x[i] + y[i]` | | add element by element: the residual |

### 👀 Worked example: the residual, with simple numbers

x = [1, −1], and the MLP part gives y ≈ [0.841, 0.819]. out = [1 + 0.841, −1 + 0.819] = **[1.841, −0.181]**, the number the program prints. The input survives in the output: that's what keeps information (and gradients) flowing through 32 layers.

## 🎯 Your quest

`gelu(x)`: replace `return x` with:

`    return 0.5 * x * (1 + math.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * x ** 3)))`

`mlp_block(x, W1, W2)`: replace `return x` with:

1. `    hidden = matvec(W1, rms_norm(x))`
2. `    h = []`
3. `    for v in hidden:`
4. `        h.append(gelu(v))`
5. `    y = matvec(W2, h)`
6. `    out = []`
7. `    for i in range(len(x)):`
8. `        out.append(x[i] + y[i])`
9. `    return out`

It prints `block: [1.8412, -0.1815]`.

## Review

<details><summary>LayerNorm or RMSNorm: which one subtracts the mean?</summary>LayerNorm. RMSNorm only divides by the root mean square.</details>
<details><summary>What does "causal" mean in causal attention?</summary>Each position only attends to itself and earlier positions, never future ones.</details>
