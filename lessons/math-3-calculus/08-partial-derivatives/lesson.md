---
title: ∂: partial derivatives (many knobs)
xp: 50
---
# Turn one knob, freeze the rest

> **Warm-up:** a shower has a hot knob and a cold knob. If you only turn the hot knob a little, how much warmer does the water get? (You're ignoring the cold knob for now.)

**In one sentence:** a partial derivative is the slope with respect to **one** input while every other input is frozen, and it's written with a curly `∂`.

## 🪜 Plain words

Real models have millions of knobs (weights). The loss depends on all of them at once. To learn, we ask about each knob **separately**: "If I nudge only this one, holding all others still, does the loss go up or down?"

That's all a partial derivative is: an ordinary derivative (lesson 03) where you pretend every other letter is just a fixed number.

## 🪜 With numbers

A one-neuron model: prediction = w·x + b. Loss = (prediction − target)².

Example: x = 2, target y = 7, knobs w = 1, b = 1.

- Prediction: 1·2 + 1 = **3**. Error: 3 − 7 = **−4**. Loss: (−4)² = **16**.
- Nudge only **w**: the prediction moves by x = 2 per unit of w. Slope of loss = 2 · error · 2 = **−16**.
- Nudge only **b**: the prediction moves by 1 per unit of b. Slope of loss = 2 · error · 1 = **−8**.

Both negative → increasing w or b **lowers** the loss. And w matters twice as much (because x = 2).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `∂` | "partial" / "del" / "curly d" | like `d`, but for one of several inputs | |
| `∂L/∂w` | "partial L partial w" / "d L d w" | slope of L when only w moves | `partial(L, point, i)` |
| `L(w, b)` | "L of w and b" | a function with two inputs | `def L(w, b):` |
| `x`, `y` | "x", "y" | the data: **fixed** while training | |
| `w`, `b` | "w", "b" | the knobs we change | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">∂L / ∂w</span> = <span class="k2">2</span> · ( <span class="k3">w·x + b − y</span> ) · <span class="k4">x</span> &nbsp;&nbsp;&nbsp; <span class="k5">∂L / ∂b</span> = <span class="k2">2</span> · ( <span class="k3">w·x + b − y</span> ) · <span class="k6">1</span></div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k1">∂L / ∂w</span> | "partial L partial w" | loss slope, only w moving | −16 |
| <span class="k2">2</span> | "two" | from the power rule on (…)² (lesson 04) | 2 |
| <span class="k3">w·x + b − y</span> | "the error" | prediction minus target | −4 |
| <span class="k4">x</span> | "times x" | chain rule: how fast the prediction moves when w moves | 2 |
| <span class="k5">∂L / ∂b</span> | "partial L partial b" | loss slope, only b moving | −8 |
| <span class="k6">1</span> | "times one" | the prediction moves 1-for-1 with b | 1 |

## 🔀 What if it were different?

<div class="wrong"><b>Forget the · x for w</b>: −8 for w. You'd treat w and b as equally important, but w's effect is scaled by the input. With x = 100 you'd be off by 100×.</div>
<div class="wrong"><b>Error the other way round, (y − prediction)</b>: +16 and +8. The signs flip, so training would push w and b <b>down</b>, the loss would grow, and the model would get worse every step.</div>
<div class="wrong"><b>Let b move too while measuring w</b>: you'd mix both effects into one number and couldn't tell which knob to turn.</div>
<div class="right">∂L/∂w = −16, ∂L/∂b = −8 ✓</div>

## 🗣️ Say it out loud

"Partial L partial w equals two times the error times x."

## 🤖 Where AI uses it

Every weight in every model gets its own partial derivative on every training step. A 7B model computes 7 billion of them each step (with backprop, lesson 11, they cost about as much as two forward passes).

## 🎯 Your quest

1. `partial(f, point, i, h=1e-5)`: numeric partial derivative of `f(*point)` with respect to input number `i` (central difference, only `point[i]` moves).
2. `loss_partials(w, b, x, y)`: `(∂L/∂w, ∂L/∂b)` for L = (wx + b − y)², using the formulas above.

**Remember:** ∂ = slope for one knob, all others frozen.

## Review

<details><summary>Product rule?</summary>(fg)' = f'g + fg'.</details>
<details><summary>Why is (f · g)' not f' · g'?</summary>Both things change; you need both strips: f'g and fg'.</details>
