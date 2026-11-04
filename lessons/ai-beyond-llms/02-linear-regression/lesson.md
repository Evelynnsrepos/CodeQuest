---
title: Linear regression
xp: 40
---
# The simplest model that learns

> **Warm-up:** you have five flats with their sizes and rents. How would you guess the rent of a 50 m² flat?

Draw the best straight line through the points: `y ≈ a·x + b`. "Best" means smallest **mean squared error**:

```
MSE = (1/n) Σ (y_i − (a·x_i + b))²
```

You could find `a` and `b` by gradient descent (LLMs 5), but for a line there's an exact answer (setting both partial derivatives to 0):

```
a = Σ(x_i − x̄)(y_i − ȳ) / Σ(x_i − x̄)²        (covariance / variance)
b = ȳ − a·x̄
```

`x̄` and `ȳ` are the means. With many input features this becomes the **normal equation** `w = (XᵀX)⁻¹Xᵀy` (linear algebra from LLMs 4).

Why squared error? Squaring makes big misses count a lot and is smooth to differentiate. It also has a probabilistic meaning: minimizing MSE is **maximum likelihood** if the noise is Gaussian, just as minimizing cross-entropy is maximum likelihood for categories. Every model in this course is "pick the parameters that make the data most likely".

## Your quest

1. `fit_line(xs, ys)`: return `(a, b)` with the formulas above.
2. `mse(xs, ys, a, b)`.

## Review

<details><summary>Which kind of learning is LLM pretraining?</summary>Self-supervised: the next token in the text is the label.</details>
<details><summary>What usually works best on tabular data?</summary>Gradient-boosted trees (XGBoost, LightGBM).</details>
