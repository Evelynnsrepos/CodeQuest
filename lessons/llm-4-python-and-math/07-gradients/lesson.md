---
title: Gradients and gradient descent
minutes: 60
xp: 40
hint: numeric_gradient: for i in range(len(point)): then up = list(point) and down = list(point)
hint: Still in the loop: up[i] = up[i] + h, down[i] = down[i] - h, grad.append((f(up) - f(down)) / (2 * h))
hint: gradient_descent: for step in range(steps): grad = numeric_gradient(f, point) and new_point = []
hint: Then for i in range(len(point)): new_point.append(point[i] - learning_rate * grad[i]). After that inner loop: point = new_point
---
# Many weights, one direction

⏱️ About 60 minutes

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

## 🔬 Take the formulas apart

**Partial derivative** <div class="formula"><span class="k1">∂f</span>/<span class="k2">∂x</span></div>
- `∂` is a curly d, said "partial". `∂f/∂x` reads "partial f by partial x".
- It means: the slope of `f` when **only x moves**. Every other letter is frozen, as if it were a plain number.

For `f(x, y) = x² + 3y²`:

1. Move only x, freeze y. `x²` → `2x` (lesson 6). `3y²` is now a constant → `0`. So **∂f/∂x = 2x**.
2. Move only y, freeze x. `x²` → `0`. `3y²` → `3 × 2y` = `6y`. So **∂f/∂y = 6y**.

At the point (1, 1): ∂f/∂x = 2, ∂f/∂y = 6.

**Gradient** <div class="formula"><span class="k1">∇f</span> = [<span class="k2">∂f/∂x</span>, <span class="k3">∂f/∂y</span>]</div>
`∇` is an upside-down triangle, said "nabla" or "grad". It's just the **list** of all partial derivatives. At (1, 1): ∇f = **[2, 6]**. It points uphill, the steepest way.

**One step downhill** <div class="formula"><span class="k1">w</span> = <span class="k1">w</span> − <span class="k2">learning_rate</span> · <span class="k3">∇loss(w)</span></div>
- <span class="k1">w</span>: where you are (all the weights).
- <span class="k3">∇loss(w)</span>: the uphill direction there.
- <span class="k2">learning_rate</span>: how big a step. The minus sign turns "uphill" into "downhill".

Numbers: f(x) = x², start at x = 10, learning rate 0.25. Slope = 2x = 20. New x = 10 − 0.25 × 20 = 10 − 5 = **5**. Next: slope 10, x = 5 − 2.5 = **2.5**. It halves each step, heading for the bottom at 0.

<div class="wrong">❌ learning rate 1.5: x = 10 − 1.5 × 20 = −20. You jumped over the valley and landed higher up. It gets worse each step.</div>
<div class="right">✅ learning rate 0.25: each step lands lower, closer to 0.</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `x, y = p` | "x and y from p" | in the given `bowl`: takes the two entries of the list `p` into two names |
| `up = list(point)` | | a **copy**. Changing `up` leaves `point` as it was. |
| `up[i] = up[i] + h` | | changes **only** entry `i` of the copy |
| `f(up)` | | the height at the nudged point |
| `for step in range(steps):` | | repeats `steps` times. `step` itself isn't used. |
| `point = new_point` | | from now on, `point` means the new list |

### 👀 Worked example: one nudge at a time

`f(p) = p[0]² + 3·p[1]²` at point `[1.0, 1.0]`, with a big h = 0.1 to follow along:

1. `i` = 0: up = [1.1, 1.0] → f = 1.21 + 3 = 4.21. down = [0.9, 1.0] → f = 0.81 + 3 = 3.81. (4.21 − 3.81) / 0.2 = **2**.
2. `i` = 1: up = [1.0, 1.1] → f = 1 + 3.63 = 4.63. down = [1.0, 0.9] → 1 + 2.43 = 3.43. (4.63 − 3.43) / 0.2 = **6**.
3. Gradient: **[2, 6]**, the same as ∂f/∂x = 2x and ∂f/∂y = 6y above.

## 🎯 Your quest

`numeric_gradient(f, point)`: between `grad = []` and `return grad`, add:

1. `    for i in range(len(point)):`
2. `        up = list(point)`
3. `        down = list(point)`
4. `        up[i] = up[i] + h`
5. `        down[i] = down[i] - h`
6. `        grad.append((f(up) - f(down)) / (2 * h))`

`gradient_descent(f, start, learning_rate, steps)`: between `point = list(start)` and `return point`, add:

1. `    for step in range(steps):`
2. `        grad = numeric_gradient(f, point)`
3. `        new_point = []`
4. `        for i in range(len(point)):`
5. `            new_point.append(point[i] - learning_rate * grad[i])`
6. `        point = new_point`

Look at the output: lr 0.01 is still far away after 30 steps, lr 0.1 gets close, and lr 0.4 explodes in y: y is the steep direction (slope 6y), so each step overshoots further than the last.

## Review

<details><summary>Write the central difference formula.</summary>f'(x) ≈ (f(x + h) − f(x − h)) / (2h)</details>
<details><summary>What is the derivative of xⁿ?</summary>n·xⁿ⁻¹</details>
<details><summary>What does f'(x) = 0 tell you?</summary>The function is flat there: a minimum, maximum or saddle point.</details>
<details><summary>f(x, y) = 4x + y². What is ∂f/∂y?</summary>2y. Freeze x, so 4x is a constant and gives 0.</details>
