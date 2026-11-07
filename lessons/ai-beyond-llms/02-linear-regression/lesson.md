---
title: Linear regression
minutes: 45
xp: 40
hint: Two loops: the first adds up sum_x and sum_y, then mx = sum_x / n and my = sum_y / n
hint: Second loop: top = top + (xs[i] - mx) * (ys[i] - my) and bottom = bottom + (xs[i] - mx) ** 2
hint: a = top / bottom and b = my - a * mx, then return (a, b)
hint: mse: error = ys[i] - (a * xs[i] + b), total = total + error ** 2, and at the end return total / len(xs)
---
# The simplest model that learns

⏱️ About 45 minutes

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

## 🔬 Take the formulas apart

**The signs first:**

| Sign | Say it | Means |
|---|---|---|
| `xᵢ`, `yᵢ` | "x i", "y i" | the i-th point: its size and its rent. The small `i` is just a counter: point 1, point 2, ... |
| `n` | "n" | how many points there are |
| `Σ` | "sigma" (a Greek S, for **s**um) | "add this up for every point" |
| `x̄` | "x bar" | the **mean** (average) of all x: add them, divide by n |
| `(…)²` | "squared" | times itself: 3² = 9, (−2)² = 4. Always positive. |
| `(1/n) Σ` | "one over n times the sum" | add up, then divide by n: an average |

**The mean squared error, in small steps** for the line `y = 0.5·x + 1` and the points (1, 1), (2, 3), (3, 2):

1. The line's guess for each x: 0.5·1 + 1 = **1.5**, 0.5·2 + 1 = **2**, 0.5·3 + 1 = **2.5**.
2. The miss = real y minus guess: 1 − 1.5 = −0.5, 3 − 2 = 1, 2 − 2.5 = −0.5.
3. Square each miss: 0.25, 1, 0.25. (Now a miss below and a miss above both count as bad.)
4. Σ adds them: 0.25 + 1 + 0.25 = 1.5.
5. (1/n) divides by n = 3: **MSE = 0.5**.

**The best line, in small steps** for the same points:

1. Means: x̄ = (1 + 2 + 3) / 3 = **2**, ȳ = (1 + 3 + 2) / 3 = **2**.
2. How far each point is from the mean: x − x̄ = −1, 0, 1 and y − ȳ = −1, 1, 0.
3. Top, Σ(xᵢ − x̄)(yᵢ − ȳ): (−1)·(−1) + 0·1 + 1·0 = 1 + 0 + 0 = **1**. (Minus times minus is plus.)
4. Bottom, Σ(xᵢ − x̄)²: (−1)² + 0² + 1² = 1 + 0 + 1 = **2**.
5. a = top / bottom = 1 / 2 = **0.5**. That's the slope: half a unit of y for every unit of x.
6. b = ȳ − a·x̄ = 2 − 0.5·2 = **1**. So the best line is y = 0.5·x + 1, and its MSE is the 0.5 from above.

<div class="wrong"><b>Forget to square the misses</b>: −0.5 + 1 − 0.5 = 0. A line that misses every point would look perfect.</div>
<div class="right">square, then average ✓</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `n = len(xs)` | | how many points |
| `for i in range(n):` | "for i from 0 up to n" | `i` = 0, 1, ..., n − 1: lets you use `xs[i]` and `ys[i]` together |
| `sum_x = sum_x + xs[i]` | | running total |
| `(xs[i] - mx) ** 2` | "squared" | `**` is "to the power": `** 2` means squared |
| `return (a, b)` | | gives back both numbers as a pair |

## 🎯 Your quest

1. `fit_line(xs, ys)`: return `(a, b)` with the formulas above.
2. `mse(xs, ys, a, b)`.

**Part 1:** `fit_line`. Replace `return (0.0, 0.0)` with steps 1 to 6 from above as code:

1. `n = len(xs)`
2. `sum_x = 0`
3. `sum_y = 0`
4. `for i in range(n):`
5. `    sum_x = sum_x + xs[i]`
6. `    sum_y = sum_y + ys[i]`
7. `mx = sum_x / n`
8. `my = sum_y / n`
9. `top = 0`
10. `bottom = 0`
11. `for i in range(n):`
12. `    top = top + (xs[i] - mx) * (ys[i] - my)`
13. `    bottom = bottom + (xs[i] - mx) ** 2`
14. `a = top / bottom`
15. `b = my - a * mx`
16. `return (a, b)`

`mx` is x̄ and `my` is ȳ ("mean of x", "mean of y").

**Part 2:** `mse`. Replace `return 0.0` with:

1. `total = 0`
2. `for i in range(len(xs)):`
3. `    error = ys[i] - (a * xs[i] + b)`
4. `    total = total + error ** 2`
5. `return total / len(xs)`

## Review

<details><summary>Which kind of learning is LLM pretraining?</summary>Self-supervised: the next token in the text is the label.</details>
<details><summary>What usually works best on tabular data?</summary>Gradient-boosted trees (XGBoost, LightGBM).</details>
