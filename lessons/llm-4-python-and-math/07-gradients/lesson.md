---
title: Gradients and gradient descent
xp: 40
---
# Many weights, one direction

> **Warm-up:** a model has billions of weights, not one `x`. How do you find "downhill" when there are billions of directions?

With **partial derivatives**: the slope along one variable while all others stay fixed. For `f(x, y) = x² + 3y²`:

```
∂f/∂x = 2x          (treat y as a constant)
∂f/∂y = 6y          (treat x as a constant)
```

Collect all partial derivatives into one vector and you have the **gradient**, `∇f = [∂f/∂x, ∂f/∂y]`. It points in the direction of **steepest increase**. So the steepest way *down* is `−∇f`, and that gives the most important algorithm in machine learning:

```
gradient descent:
repeat:
    w = w − learning_rate · ∇loss(w)
```

The **learning rate** is the step size. Too small: painfully slow. Too large: you overshoot the valley and bounce around or explode. You'll see all three behaviours in this lesson's output.

In a real model `w` is the vector of all the weights and `loss` measures how wrong the predictions are (next lessons). Backpropagation (Module 5) is just a fast way of computing this gradient for billions of weights at once.

## Your quest

1. `numeric_gradient(f, point)`: for each coordinate `i`, nudge only that coordinate by `+h` and `−h` (`h = 1e-5`) and take the central difference. Return the list of partial derivatives. `p = list(point)` copies a list so you can change one entry.
2. `gradient_descent(f, start, learning_rate, steps)`: starting from `start`, take `steps` steps of `point = point − learning_rate · gradient`, and return the final point.

## Review

<details><summary>Write the central difference formula.</summary>f'(x) ≈ (f(x + h) − f(x − h)) / (2h)</details>
<details><summary>What is the derivative of xⁿ?</summary>n·xⁿ⁻¹</details>
<details><summary>What does f'(x) = 0 tell you?</summary>The function is flat there: a minimum, maximum or saddle point.</details>
