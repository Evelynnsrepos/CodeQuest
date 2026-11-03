---
title: LayerNorm and RMSNorm
xp: 40
---
# Keeping the numbers in a healthy range

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

## Your quest

1. `layer_norm(x, gamma, beta, eps=1e-5)`
2. `rms_norm(x, gamma, eps=1e-5)`

## Review

<details><summary>Why split into heads instead of one big head?</summary>Each head gets its own softmax, so different heads can attend to different positions, at the same cost.</details>
<details><summary>What does GQA share between heads?</summary>Key/value heads, which shrinks the KV cache.</details>
