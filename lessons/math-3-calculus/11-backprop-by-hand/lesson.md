---
title: Backpropagation by hand
xp: 70
---
# The chain rule, run backwards

> **Warm-up:** a neuron does `z = w·x + b`, then `a = σ(z)`, then the loss is `(a − y)²`. Three machines in a row. How many slopes do you need to multiply to get ∂L/∂w?

**In one sentence:** backpropagation runs the network forward to get every intermediate value, then walks backwards multiplying local slopes (the chain rule) to get the gradient of every weight.

## 🪜 Plain words

**Forward pass:** compute and **remember** each machine's output.

**Backward pass:** start at the loss and go back one machine at a time. At each machine, multiply by its local slope. When you reach a weight, you have its gradient.

Why backwards? Because the later slopes are shared by every earlier weight, so you compute them once and reuse them. That's what makes training a billion weights possible.

## 🪜 With numbers

w = 0.5, b = 0, x = 2, target y = 1.

**Forward:**
- z = 0.5 · 2 + 0 = **1**
- a = σ(1) = **0.7311**
- L = (0.7311 − 1)² = **0.0723**

**Backward:**
- ∂L/∂a = 2(a − y) = 2 · (−0.2689) = **−0.5379**
- ∂a/∂z = a(1 − a) = 0.7311 · 0.2689 = **0.1966** (lesson 05)
- ∂z/∂w = x = **2**, ∂z/∂b = **1**
- ∂L/∂w = −0.5379 · 0.1966 · 2 = **−0.2115**
- ∂L/∂b = −0.5379 · 0.1966 · 1 = **−0.1058**

Negative → increasing w and b lowers the loss (a gets closer to 1). Makes sense!

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `z` | "z" | the weighted sum before the bend (the "pre-activation") | `z = w*x + b` |
| `a` | "a" | the output after the bend (the "activation") | `a = sigmoid(z)` |
| `σ` | "sigma" | sigmoid (lesson 05) | |
| `∂L/∂a` | "partial L partial a" | how the loss reacts to a | `dL_da` |
| `·` | "times" | the chain rule multiplies | `*` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">∂L/∂w</span> = <span class="k2">∂L/∂a</span> · <span class="k3">∂a/∂z</span> · <span class="k4">∂z/∂w</span> = <span class="k2">2(a − y)</span> · <span class="k3">a(1 − a)</span> · <span class="k4">x</span></div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k2">2(a − y)</span> | "two times a minus y" | loss machine's slope (power rule) | −0.5379 |
| <span class="k3">a(1 − a)</span> | "a times one minus a" | sigmoid machine's slope | 0.1966 |
| <span class="k4">x</span> | "x" | weighted-sum machine's slope for w | 2 |
| <span class="k1">∂L/∂w</span> | "partial L partial w" | all three multiplied | −0.2115 |

For b, the last piece is **1** instead of x: −0.1058. The first two pieces are **shared**: computed once, used twice.

## 🔀 What if it were different?

<div class="wrong"><b>Skip the sigmoid's slope a(1 − a)</b>: −0.5379 · 2 = −1.0758. Five times too big; you'd overshoot. Forgetting one machine in the chain is the classic hand-written-backprop bug.</div>
<div class="wrong"><b>Use z instead of a in the loss slope, 2(z − y)</b>: 2(1 − 1) = 0. The model thinks it's perfect and stops learning while a is still 0.73.</div>
<div class="wrong"><b>Use a(1 − a) with a = z = 1</b>: 1 · 0 = 0. Same problem: no learning. Each slope must use the value its own machine produced.</div>
<div class="right">∂L/∂w = −0.2115, ∂L/∂b = −0.1058 ✓ (matches the numeric check)</div>

## 🗣️ Say it out loud

"d L d w equals d L d a, times d a d z, times d z d w."

## 🤖 Where AI uses it

`loss.backward()` does exactly this for every operation in the model, automatically ("autograd"). The forward values it remembers are the **activations**, which is why training needs far more memory than inference, and why "activation checkpointing" recomputes some of them instead.

## 🎯 Your quest

`sigmoid` is given.

1. `forward(w, b, x, y)`: return `(z, a, L)`.
2. `backward(w, b, x, y)`: return `(∂L/∂w, ∂L/∂b)`.

**Remember:** forward and remember; backward and multiply.

## Review

<details><summary>Gradient descent update?</summary>θ ← θ − η∇L(θ).</details>
<details><summary>What happens if η is far too big?</summary>You overshoot, the loss grows and can explode to NaN.</details>
