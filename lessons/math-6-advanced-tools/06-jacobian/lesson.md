---
title: The Jacobian: derivatives of many outputs
xp: 60
---
# A table of every slope

> **Warm-up:** in Math 3 you took partial derivatives of a function with one output (a loss). What if the function has several outputs, like a layer of a network?

**In one sentence:** the Jacobian of a function with several inputs and several outputs is the table of every partial derivative: row i, column j says how much output i changes when input j nudges.

## 🪜 Plain words

A network layer takes a vector in and gives a vector out. To train it, backprop needs to know how **each output** reacts to **each input**. That's a table: one row per output, one column per input. The **gradient** (Math 3 lesson 09) is the special case with one output (one row).

The chain rule becomes **matrix multiplication**: the Jacobian of "f, then g" is (Jacobian of g) × (Jacobian of f). That's literally what backprop multiplies through the layers.

## 🪜 With numbers

f(x, y) = ( x·y , x + y² ) at (x, y) = (2, 3):

| | ∂/∂x | ∂/∂y |
|---|---|---|
| output 1: x·y | y = **3** | x = **2** |
| output 2: x + y² | **1** | 2y = **6** |

J = [[3, 2], [1, 6]]. Check by nudging x by 0.001: outputs go from (6, 11) to (6.003, 11.001): changes 3 × and 1 × the nudge ✓.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `∂fᵢ/∂xⱼ` | "partial f i by x j" | slope of output i in input j | `(f(x + h) - f(x - h)) / (2h)` |
| `J` | "J" or "the Jacobian" | the table of all of them | list of rows |
| `Jᵢⱼ` | "J i j" | row i, column j | `J[i][j]` |
| `J_g · J_f` | "J g times J f" | chain rule for vector functions | `matmul(Jg, Jf)` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">J</span><sub><span class="k2">i</span><span class="k3">j</span></sub> = ∂<span class="k4">f<sub>i</sub></span> / ∂<span class="k5">x<sub>j</sub></span> &nbsp;&nbsp; <span class="k1">J</span><sub>g∘f</sub> = <span class="k6">J<sub>g</sub>(f(x))</span> · <span class="k1">J<sub>f</sub>(x)</span></div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k2">i</span> | "i" | which output (row) | 2 (x + y²) |
| <span class="k3">j</span> | "j" | which input (column) | 2 (y) |
| <span class="k4">fᵢ</span> | "f i" | the i-th output | x + y² |
| <span class="k5">xⱼ</span> | "x j" | the j-th input | y |
| <span class="k1">Jᵢⱼ</span> | "J i j" | its slope | 2y = 6 |
| <span class="k6">J_g(f(x))</span> | "J g at f of x" | the next layer's table, evaluated where f landed | |

## 🔀 What if it were different?

<div class="wrong"><b>Swap rows and columns</b>: [[3, 1], [2, 6]]. Multiplying it by a nudge (1, 0) of x predicts output changes (3, 2) instead of (3, 1). Wrong, and the chain-rule products stop lining up.</div>
<div class="wrong"><b>Multiply in the wrong order</b> (J_f · J_g): the shapes often don't even fit (a 3×2 times a 2×5 vs a 2×5 times a 3×2), and when they do, the answer is wrong. The last function's table goes on the left.</div>
<div class="right">J = [[3, 2], [1, 6]] at (2, 3) ✓</div>

## 🗣️ Say it out loud

"J i j is partial f i by partial x j; the Jacobian of g after f is J g at f of x times J f."

## 🤖 Where AI uses it

Backprop multiplies Jacobians (in practice, vector-Jacobian products, so the giant tables never get built). Normalizing flows, robustness checks ("how much can a small input change move the output?") and physics-informed networks use Jacobians directly. PyTorch has `torch.autograd.functional.jacobian`.

## 🎯 Your quest

1. `jacobian(f, x, h=1e-5)`: `f` takes a list and returns a list; build J with **central differences** for each input j.
2. `matmul(A, B)`.
3. `chain_jacobian(f, g, x)`: `matmul(jacobian(g, f(x)), jacobian(f, x))`.

**Remember:** rows = outputs, columns = inputs; chain = multiply, last function on the left.

## Review

<details><summary>How does LoRA use the low-rank idea?</summary>It trains the weight update as a product of two thin matrices, rank r, instead of a full matrix.</details>
