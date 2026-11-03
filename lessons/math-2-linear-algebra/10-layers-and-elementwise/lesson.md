---
title: Neural network layers in matrix form
xp: 50
---
# y = σ(Wx + b), and the ⊙ sign

> **Warm-up:** write out what one layer of a neural network does, in one line of math, using what you've learned.

**In one sentence:** a layer multiplies by a weight matrix, adds a bias vector and applies a function to each entry; `⊙` multiplies two vectors entry by entry.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `Wx + b` | "W x plus b" | an **affine** (linear + shift) map | `add(matvec(W, x), b)` |
| `σ(·)` applied to a vector | "sigma of …" | apply σ to **each entry** | `[sigma(v) for v in vec]` |
| `ReLU(x) = max(0, x)` | "rel-you" | negatives become 0 | `max(0, x)` |
| `a ⊙ b` | "a Hadamard b" / "element-wise product" | `(a₁b₁, a₂b₂, …)`: a **vector**, not a sum | `[x * y for x, y in zip(a, b)]` |
| `W ∈ ℝ^(d_out × d_in)` | | one row per output | |

Don't confuse `a · b` (dot product: one number) with `a ⊙ b` (element-wise: a vector).

## The idea

```
h = σ(W x + b)
     │  │   └ bias: one number per output, shifts it
     │  └ input vector (d_in)
     └ weights (d_out × d_in): row i = weights of output neuron i
```

- **Parameters** of a layer: `d_out · d_in` weights + `d_out` biases.
- **Why σ?** Without it, two layers `W₂(W₁x)` = `(W₂W₁)x` collapse into one matrix (lesson 8: brackets don't matter). The non-linear bend is what lets deep networks learn curves.
- **Gates with ⊙:** Llama's MLP is `W₂(SiLU(W₁x) ⊙ W₃x)`: one branch decides "how much" (gate), the other "what", multiplied entry by entry.

## 🗣️ Say it out loud

`h = ReLU(Wx + b)` → "h is ReLU of W x plus b" → "compute every neuron's weighted sum plus bias, then zero out the negatives."

## 🧮 Worked example

`W = [[1, −1], [2, 0]]`, `x = (3, 5)`, `b = (0, −4)`:

1. `Wx = (1·3 − 1·5, 2·3 + 0·5) = (−2, 6)`
2. `+ b = (−2, 2)`
3. ReLU: `(0, 2)`

## 🤖 Where AI uses it

Every MLP, every projection, LoRA adapters, the output head (`logits = W_out · h`), SwiGLU gating with ⊙.

## 🎯 Your quest

1. `relu_layer(W, b, x)`: `ReLU(Wx + b)`.
2. `hadamard(a, b)`: `a ⊙ b`.
3. `layer_params(d_in, d_out)`: number of weights + biases.

**Remember:** `·` gives one number, `⊙` gives a vector.

## Review

<details><summary>What is Iₙx?</summary>x: the identity changes nothing.</details>
<details><summary>Why is attention QKᵀ and not QK?</summary>Q and K are both T × d; transposing K makes the shapes fit, giving T × T scores.</details>
