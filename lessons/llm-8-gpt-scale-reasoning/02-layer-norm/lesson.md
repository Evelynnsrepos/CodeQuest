---
title: LayerNorm and RMSNorm
minutes: 45
xp: 40
hint: layer_norm: d = len(x), mean = sum(x) / d, then var = 0 and a loop adding (v - mean) ** 2, then var = var / d
hint: layer_norm ends: out = [], for i in range(d): out.append((x[i] - mean) / math.sqrt(var + eps) * gamma[i] + beta[i]), return out
hint: rms_norm: total = 0, add v * v for every v, rms = math.sqrt(total / len(x) + eps), then out.append(x[i] / rms * gamma[i])
---
# Keeping the numbers in a healthy range

⏱️ About 45 minutes

> **Warm-up:** a vector goes through 32 layers, and each layer adds something to it. What can happen to the size of its numbers?

They can drift: grow huge or shrink, which makes training unstable. **Normalization** rescales each token's vector before a sub-layer uses it.

**LayerNorm** (GPT-2, 2016 paper by Ba et al.), for one vector `x` of width `d`:

```
mean = Σx / d
var  = Σ(x − mean)² / d
y_i  = (x_i − mean) / √(var + ε) · γ_i + β_i
```

`γ` (gain) and `β` (bias) are learned per position, starting at 1 and 0. `ε` (like `1e-5`) avoids dividing by zero.

**RMSNorm** (Llama, Mistral, Qwen) drops the mean and the bias, which is cheaper and works as well:

```
rms = √(Σx² / d + ε)
y_i = x_i / rms · γ_i
```

Note: this normalizes **across the features of one token**, not across a batch. That's the difference from BatchNorm (used in vision models), and why it works with any batch size, including 1 at inference.

## 🔬 Take the formulas apart

**LayerNorm**, for x = [2, 4, 6, 8] (d = 4):

<div class="formula">mean = <span class="k1">Σx</span> / <span class="k2">d</span></div>
Add all numbers, divide by how many: (2 + 4 + 6 + 8) / 4 = 20 / 4 = **5**.

<div class="formula">var = <span class="k1">Σ(x − mean)²</span> / d</div>
Distance from the mean, squared, averaged (the variance, LLMs 4 lesson 9): (−3)² + (−1)² + 1² + 3² = 9 + 1 + 1 + 9 = 20, / 4 = **5**.

<div class="formula">yᵢ = (<span class="k1">xᵢ − mean</span>) / <span class="k2">√(var + ε)</span> · <span class="k3">γᵢ</span> + <span class="k4">βᵢ</span></div>
1. <span class="k1">xᵢ − mean</span>: center around 0. 2 − 5 = −3.
2. <span class="k2">√(var + ε)</span>: √5 ≈ 2.236 (ε = 0.00001 is too small to matter here). −3 / 2.236 ≈ **−1.342**.
3. <span class="k3">γ</span> ("gamma", the gain) multiplies, <span class="k4">β</span> ("beta", the bias) adds. Both are learned; here γ = 1 and β = 0, so nothing changes.

Result: **[−1.342, −0.447, 0.447, 1.342]**: mean 0, spread 1.

**RMSNorm** <div class="formula">rms = √(<span class="k1">Σx²</span> / d + ε), &nbsp; yᵢ = xᵢ / rms · γᵢ</div>
No centering. 4 + 16 + 36 + 64 = 120, / 4 = 30, √30 ≈ 5.477. 2 / 5.477 ≈ **0.365**, and so on: [0.365, 0.730, 1.095, 1.461].

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `sum(x) / d` | | the mean |
| `var = var + (v - mean) ** 2` | | running total of squared distances |
| `math.sqrt(var + eps)` | | √(var + ε) |
| `gamma[i]`, `beta[i]` | | the gain and bias for position i |
| `def f(x, gamma, beta, eps=1e-5):` | | eps is 0.00001 unless given |

### 👀 Worked example: [1, 3]

mean = 2, var = ((1 − 2)² + (3 − 2)²) / 2 = 1, √1 = 1. y = [(1 − 2)/1, (3 − 2)/1] = **[−1, 1]**.

## 🎯 Your quest

`layer_norm(x, gamma, beta, eps=1e-5)`: replace `return x` with:

1. `    d = len(x)`
2. `    mean = sum(x) / d`
3. `    var = 0`
4. `    for v in x:`
5. `        var = var + (v - mean) ** 2`
6. `    var = var / d`
7. `    out = []`
8. `    for i in range(d):`
9. `        out.append((x[i] - mean) / math.sqrt(var + eps) * gamma[i] + beta[i])`
10. `    return out`

`rms_norm(x, gamma, eps=1e-5)`: replace `return x` with:

1. `    total = 0`
2. `    for v in x:`
3. `        total = total + v * v`
4. `    rms = math.sqrt(total / len(x) + eps)`
5. `    out = []`
6. `    for i in range(len(x)):`
7. `        out.append(x[i] / rms * gamma[i])`
8. `    return out`

## Review

<details><summary>Why split into heads instead of one big head?</summary>Each head gets its own softmax, so different heads can attend to different positions, at the same cost.</details>
<details><summary>What does GQA share between heads?</summary>Key/value heads, which shrinks the KV cache.</details>
