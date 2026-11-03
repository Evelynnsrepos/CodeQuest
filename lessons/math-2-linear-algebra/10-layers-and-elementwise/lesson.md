---
title: Neural network layers in matrix form
xp: 50
---
# y = σ(Wx + b), and the ⊙ sign

> **Warm-up:** with what you know now, describe in words what one layer of a neural network does.

**In one sentence:** a layer multiplies by a weight matrix, adds a bias, and applies a bending function to each number; `⊙` multiplies two lists position by position.

## 🪜 Plain words

1. Every neuron makes a weighted sum of the inputs (matrix times vector).
2. Every neuron adds its own offset (the **bias**).
3. Every number goes through a small **bending** function, like "negative becomes 0" (ReLU).

Why bend? Without it, two layers in a row could be squashed into a single matrix, so a deep network would be no smarter than one layer.

## 🪜 With numbers

Weights `[[1, −1], [2, 0]]`, input (3, 5), bias (0, −4):

1. Weighted sums: 1·3 − 1·5 = −2; 2·3 + 0·5 = 6 → (−2, 6)
2. Add bias: (−2 + 0, 6 − 4) = (−2, 2)
3. ReLU (negatives → 0): **(0, 2)**

Position-by-position multiply: (1, 2, 3) ⊙ (4, 5, 6) = (4, 10, 18). A list, not one number.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `Wx + b` | "W x plus b" | weighted sums plus biases | |
| `σ(…)` on a list | "sigma of …" | apply σ to each number | `[sigma(v) for v in vec]` |
| `ReLU(x) = max(0, x)` | "rel-you" | negatives become 0 | `max(0, x)` |
| `a ⊙ b` | "a Hadamard b" / "element-wise times" | multiply position by position → a list | `[x*y for x, y in zip(a, b)]` |
| `a · b` | "a dot b" | multiply and **add up** → one number | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">h</span> = <span class="k2">σ</span>( <span class="k3">W</span><span class="k4">x</span> <span class="k5">+ b</span> )</div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k1">h</span> | "h" | the layer's output (a list) | (0, 2) |
| <span class="k2">σ</span>( ) | "sigma of" | bend each number (here ReLU) | (−2, 2) → (0, 2) |
| <span class="k3">W</span> | "W" | weights: d_out × d_in, one row per neuron | `[[1, −1], [2, 0]]` |
| <span class="k4">x</span> | "x" | the input list; <span class="k3">W</span><span class="k4">x</span> = weighted sums | (3, 5) → (−2, 6) |
| <span class="k5">+ b</span> | "plus b" | one bias per neuron | (0, −4) |

Llama's MLP gate: `W₂( SiLU(W₁x) ⊙ W₃x )`: one branch decides **how much** (gate), the other **what**, combined with ⊙.

## 🔀 What if it were different?

<div class="wrong"><b>σ(W)x + b</b> (bend the weights, not the sums): a different and useless computation; the bend must act on each neuron's total.</div>
<div class="wrong"><b>No σ at all</b>: two layers W₂(W₁x) = (W₂W₁)x, just one matrix. The network can only draw straight lines.</div>
<div class="wrong"><b>Using · instead of ⊙ in the gate</b>: you'd get one number instead of a list, and the layer output would collapse.</div>
<div class="right"><b>σ(Wx + b)</b> = (0, 2) ✓</div>

## 🗣️ Say it out loud

"h equals sigma of W x plus b."

## 🤖 Where AI uses it

Every MLP, every projection, the output head, SwiGLU gates.

## 🎯 Your quest

1. `relu_layer(W, b, x)`: `ReLU(Wx + b)`.
2. `hadamard(a, b)`: `a ⊙ b`.
3. `layer_params(d_in, d_out)`: weights + biases.

**Remember:** `·` gives one number, `⊙` gives a list.

## Review

<details><summary>What is Iₙx?</summary>x.</details>
<details><summary>Why QKᵀ and not QK?</summary>So the shapes fit: (T × d)(d × T) = T × T.</details>
