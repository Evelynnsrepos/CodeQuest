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

## Your quest

The data follows `y = 3x + 1` with a little noise.

1. `loss(w, b, data)`: the mean squared error.
2. `gradients(w, b, data)`: return `(dw, db)`, the averages of `2·e·x` and `2·e`.
3. `train(data, learning_rate, steps)`: start at `w = 0, b = 0`, apply the update `steps` times, and return `(w, b)`.

Watch the loss fall as the program prints it.

## Review

<details><summary>What does a 95% confidence interval that includes 0.5 say about a win rate?</summary>You can't tell the two models apart with this many prompts.</details>
<details><summary>What is the derivative of (w·x + b − y)² with respect to w?</summary>2·(w·x + b − y)·x, by the chain rule.</details>
