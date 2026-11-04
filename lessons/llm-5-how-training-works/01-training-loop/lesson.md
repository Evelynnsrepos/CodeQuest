---
title: The training loop, by hand
xp: 40
---
# Guess, measure, nudge, repeat

> **Warm-up:** in LLMs 4 you used gradient descent to find the bottom of a bowl. What would the "bowl" be if you wanted a model to fit some data?

The **loss**: one number measuring how wrong the model is on the data. Training is gradient descent on the loss, with the model's weights as the variables. Every training run, from this lesson to Llama 3, is this loop:

```
1. forward pass:  predictions = model(inputs)
2. loss:          L = how wrong the predictions are
3. backward pass: gradient of L with respect to every weight
4. update:        w = w − learning_rate · gradient
5. repeat
```

Start with the smallest possible model, a line `ŷ = w·x + b`, and the **mean squared error** loss:

```
L = (1/n) Σ (ŷᵢ − yᵢ)²
```

With the chain rule (LLMs 4, lesson 8) you get exact gradients. For one example, `L = (w·x + b − y)²`, so with `e = ŷ − y`:

```
∂L/∂w = 2·e·x        ∂L/∂b = 2·e
```

Averaged over all examples, those are the two numbers that tell you which way to nudge `w` and `b`.

This is **linear regression**, and it's already "machine learning": the program finds `w` and `b` from data instead of you writing them. A neural network is the same loop with more layers and a smarter way of computing the gradient (next lessons).

<svg viewBox="0 0 520 250" width="100%" style="max-width:520px" role="img" aria-label="The training loop: guess with the current weights, measure the loss, backpropagate the gradients, nudge the weights, repeat"><defs><marker id="ah3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker></defs><rect x="190" y="15" width="140" height="50" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="260.0" y="38.0" font-size="14" fill="currentColor" text-anchor="middle">1. Guess</text><text x="260.0" y="54.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">forward pass</text><rect x="360" y="100" width="140" height="50" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="430.0" y="123.0" font-size="14" fill="currentColor" text-anchor="middle">2. Measure</text><text x="430.0" y="139.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">loss: how wrong?</text><rect x="190" y="185" width="140" height="50" rx="8" fill="#e5484d" fill-opacity=".14" stroke="#e5484d" stroke-width="2"/><text x="260.0" y="208.0" font-size="14" fill="currentColor" text-anchor="middle">3. Blame</text><text x="260.0" y="224.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">backward: gradients</text><rect x="20" y="100" width="140" height="50" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="90.0" y="123.0" font-size="14" fill="currentColor" text-anchor="middle">4. Nudge</text><text x="90.0" y="139.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">w ← w − lr · grad</text><line x1="332" y1="50" x2="400" y2="98" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah3)"/><line x1="420" y1="152" x2="332" y2="205" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah3)"/><line x1="188" y1="205" x2="110" y2="152" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah3)"/><line x1="100" y1="98" x2="188" y2="50" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah3)"/><text x="260" y="128" font-size="13" fill="currentColor" text-anchor="middle" font-weight="bold">repeat</text><text x="260" y="146" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">thousands of times</text></svg>

## Your quest

The data follows `y = 3x + 1` with a little noise.

1. `loss(w, b, data)`: the mean squared error.
2. `gradients(w, b, data)`: return `(dw, db)`, the averages of `2·e·x` and `2·e`.
3. `train(data, learning_rate, steps)`: start at `w = 0, b = 0`, apply the update `steps` times, and return `(w, b)`.

Watch the loss fall as the program prints it.

## Review

<details><summary>What does a 95% confidence interval that includes 0.5 say about a win rate?</summary>You can't tell the two models apart with this many prompts.</details>
<details><summary>What is the derivative of (w·x + b − y)² with respect to w?</summary>2·(w·x + b − y)·x, by the chain rule.</details>
