---
title: Checkpoint: train a neuron from scratch
xp: 90
---
# Everything in one program

> **Warm-up:** list the steps of training, in order, without looking. (Forward, loss, gradient, update, repeat.)

You now know every piece of the training loop. In this checkpoint you'll build it yourself, and add the professional safety net: a **gradient check**.

## 🪜 The plan

1. **Gradient check:** before trusting a hand-written slope, compare it with the central difference (lesson 03). If they disagree, there's a bug.
2. **Train:** a sigmoid neuron (lesson 11) on several data points. The loss is the **average** of each point's loss, so the gradient is the average of each point's gradient (lesson 09). Update with gradient descent (lesson 10).

## 🔬 The formulas you need (all from this course)

<div class="formula">relative error = <span class="k1">| yours − numeric |</span> / <span class="k2">max(1, | numeric |)</span></div>

| Piece | Say it | Means |
|---|---|---|
| <span class="k1">\| yours − numeric \|</span> | "absolute value of yours minus numeric" | how far apart (Math 1 lesson 06) |
| <span class="k2">max(1, \| numeric \|)</span> | "max of one and …" | divide by the size, but never by something tiny |

<div class="formula"><span class="k3">w</span> ← <span class="k3">w</span> − <span class="k4">η</span> · <span class="k5">1/n Σ 2(aᵢ − yᵢ) · aᵢ(1 − aᵢ) · xᵢ</span></div>

| Piece | Means |
|---|---|
| <span class="k3">w</span> ← <span class="k3">w</span> − | gradient descent update (lesson 10) |
| <span class="k4">η</span> | learning rate |
| <span class="k5">1/n Σ …</span> | the average over all points of lesson 11's ∂L/∂w (for b: drop the · xᵢ) |

## 🔀 What if it were different?

<div class="wrong"><b>Gradient check with plain difference, no dividing</b>: for a slope of 10,000, a difference of 0.01 is tiny but would look like an error; for a slope of 0.0001 it would be huge but look fine.</div>
<div class="wrong"><b>Update w before computing b's gradient</b>: b's gradient would use the new w: not the true gradient at the current point. Compute all gradients first, then update.</div>
<div class="right">check first, then compute all gradients, then update all weights ✓</div>

## 🎯 Your quest

`sigmoid` is given.

1. `grad_check(f, df, x)`: relative error between `df(x)` and the central difference of `f` at `x` (h = 1e-5).
2. `avg_loss(w, b, xs, ys)`: average of `(σ(w·x + b) − y)²`.
3. `train(xs, ys, lr, steps)`: start at w = 0, b = 0, run gradient descent on `avg_loss`, return `(w, b)`.

Next: Math 4, probability: what the model's outputs actually **mean**.

## Review

<details><summary>What does ∫ₐᵇ f(x) dx mean?</summary>The area under f from a to b.</details>
<details><summary>Chain rule?</summary>Outside slope (at the inside's value) times inside slope.</details>
<details><summary>Which way does training step?</summary>Against the gradient: θ − η∇L.</details>
