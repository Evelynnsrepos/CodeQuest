---
title: ∇: the gradient points uphill
xp: 50
---
# All the partials in one arrow

> **Warm-up:** you're standing on a foggy hill. You can only feel the slope under your feet. Which way is the steepest way up? Which way is the steepest way down?

**In one sentence:** the gradient `∇f` is the list of all partial derivatives, and as an arrow it points in the direction where f goes **up** fastest.

## 🪜 Plain words

Last lesson gave one slope per knob. Put them all in a list: that list is the **gradient**. Read as an arrow (a vector, Math 2), it points **uphill**, the way the loss grows fastest. Its length says how steep it is.

We want the loss to go **down**, so training walks the **opposite** way: minus the gradient.

## 🪜 With numbers

f(x, y) = x² + 3y at the point (1, 2).

- ∂f/∂x = 2x = **2** (y frozen)
- ∂f/∂y = **3** (x frozen; 3y has slope 3)
- Gradient: **(2, 3)**. Uphill = right 2, up 3. Downhill = (−2, −3).

For the loss from lesson 08 (w = 1, b = 1): gradient = (−16, −8). Downhill = (+16, +8): increase both, w faster.

With **many** data points, the loss is the **average** error, so the gradient is the average of each point's gradient.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `∇` | "nabla" / "grad" / "del" | the gradient: all partials together (an upside-down triangle) | `gradient(f, point)` |
| `∇f` | "grad f" | the gradient of f | a list |
| `∇_θ L` | "grad L with respect to theta" | the gradient of the loss over all weights θ | |
| `θ` | "theta" | all the model's knobs in one list | `params` |
| `(a, b)` | | a vector (Math 2) | `[a, b]` |
| `1/n Σ` | "one over n, sum" | average (Math 1) | `sum(...) / n` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">∇f</span> = ( <span class="k2">∂f/∂x</span> , <span class="k3">∂f/∂y</span> )</div>

| Piece | Say it | Means | x² + 3y at (1, 2) |
|---|---|---|---|
| <span class="k1">∇f</span> | "grad f" | the uphill arrow | (2, 3) |
| <span class="k2">∂f/∂x</span> | "partial f partial x" | first entry: slope along x | 2 |
| <span class="k3">∂f/∂y</span> | "partial f partial y" | second entry: slope along y | 3 |

For the average squared error over n points:

<div class="formula"><span class="k1">∂L/∂w</span> = <span class="k4">1/n Σ</span> <span class="k5">2 (w·xᵢ + b − yᵢ)</span> · <span class="k6">xᵢ</span></div>

| Piece | Means |
|---|---|
| <span class="k4">1/n Σ</span> | average over all data points i = 1..n |
| <span class="k5">2 (w·xᵢ + b − yᵢ)</span> | 2 × the error on point i |
| <span class="k6">xᵢ</span> | times that point's input (for b: times 1) |

## 🔀 What if it were different?

<div class="wrong"><b>Entries in the wrong order, (3, 2)</b>: the arrow points somewhere else entirely. You'd change x by y's slope. Each entry belongs to its own knob.</div>
<div class="wrong"><b>Walk along +∇ to minimise</b>: you climb uphill; the loss grows every step.</div>
<div class="wrong"><b>Sum instead of average over data</b>: with 1,000,000 points the gradient is a million times bigger, so the same learning rate makes huge jumps. Averaging keeps it independent of dataset size.</div>
<div class="right">∇f = (2, 3), walk along −∇f to go down ✓</div>

## 🗣️ Say it out loud

`∇_θ L` → "grad of L with respect to theta" → "the list of how each weight affects the loss."

## 🤖 Where AI uses it

`loss.backward()` in PyTorch fills `.grad` on every weight: that's ∇_θ L. Gradient norms (the arrow's length) are logged in every training run, and "gradient clipping" shortens the arrow when it gets too long (Math 2 lesson 04).

## 🎯 Your quest

1. `gradient(f, point)`: list of all partial derivatives of `f(*point)` (central difference, h = 1e-5).
2. `grad_mse(w, b, xs, ys)`: `(∂L/∂w, ∂L/∂b)` for L = average of (w·xᵢ + b − yᵢ)².

**Remember:** ∇ = all the partials in a list = the uphill arrow.

## Review

<details><summary>What does ∂L/∂w mean?</summary>How the loss changes when only w moves.</details>
<details><summary>∂L/∂b for L = (wx + b − y)²?</summary>2 · (wx + b − y).</details>
