---
title: The chain rule, and the gradient every LLM trains with
xp: 50
---
# Derivatives of nested functions

> **Warm-up:** a model is a function inside a function inside a function, hundreds deep. If you know how each piece changes, how do you get how the whole thing changes?

Multiply. The **chain rule**: if `y = f(g(x))`, then

```
dy/dx = f'(g(x)) · g'(x)          ("outer derivative at the inner value, times inner derivative")
```

Intuition: if `g` doubles any change in `x`, and `f` triples any change in `g`, the whole thing sextuples it. **Backpropagation** (Module 5) is nothing but the chain rule applied systematically from the loss back through every layer.

**Example 1: the sigmoid** `σ(z) = 1 / (1 + e⁻ᶻ)`, a classic activation that squashes any number into (0, 1). Write it as `σ(z) = u⁻¹` with `u = 1 + e⁻ᶻ`:

```
dσ/du = −u⁻²        du/dz = −e⁻ᶻ
dσ/dz = −u⁻² · (−e⁻ᶻ) = e⁻ᶻ / (1 + e⁻ᶻ)²  = σ(z) · (1 − σ(z))
```

That last neat form is why sigmoid was popular: its derivative reuses its own output.

**Example 2: softmax + cross-entropy**, the loss of every LLM. For logits `z`, probabilities `p = softmax(z)` and the true next token `t`, the loss is `L = −log p_t`. Working the chain rule through softmax (a page of algebra, worth doing once on paper) gives a stunningly simple result:

```
∂L/∂zᵢ = pᵢ − yᵢ          where y is 1 for the true token and 0 elsewhere ("one-hot")
```

In words: the gradient **pushes up the true token's logit** by how much probability it was missing, and **pushes down every other logit** by exactly the probability it wrongly received. Every training step of every LLM starts with this vector.

## Your quest

1. `sigmoid(z)` and `dsigmoid(z)` (use the neat form).
2. `ce_grad(logits, target)`: return `softmax(logits)` with 1 subtracted at position `target`.

The check compares both with numerical derivatives, so you'll see the calculus is right.

## Review

<details><summary>Which direction does the gradient point?</summary>The direction of steepest increase. Gradient descent steps the opposite way.</details>
<details><summary>What goes wrong with a learning rate that's too large?</summary>Steps overshoot the minimum; the loss bounces or explodes.</details>
