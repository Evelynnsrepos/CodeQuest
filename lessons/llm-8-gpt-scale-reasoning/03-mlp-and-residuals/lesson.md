---
title: The MLP and residual connections
xp: 50
---
# Where the knowledge lives, and the highway around it

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

## Your quest

`matvec` and `rms_norm` (without gain) are given. Biases are left out, as in Llama.

1. `gelu(x)` using the tanh formula above.
2. `mlp_block(x, W1, W2)`: return `x + W2·gelu(W1·rms_norm(x))` (apply `gelu` to each number, add element by element).

## Review

<details><summary>LayerNorm or RMSNorm: which one subtracts the mean?</summary>LayerNorm. RMSNorm only divides by the root mean square.</details>
<details><summary>What does "causal" mean in causal attention?</summary>Each position only attends to itself and earlier positions, never future ones.</details>
