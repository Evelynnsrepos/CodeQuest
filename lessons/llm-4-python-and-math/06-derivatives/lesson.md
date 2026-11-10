---
title: Derivatives as slope
minutes: 60
xp: 35
hint: numeric_derivative: h = 1e-5 and then return (f(x + h) - f(x - h)) / (2 * h)
hint: df: use the rules term by term. 3x² gives 3 × 2x = 6x. −4x gives −4. +7 gives 0.
hint: df: return 6 * x - 4
hint: minimum_x: solve 6x − 4 = 0. Add 4 to both sides, then divide by 6. In Python: minimum_x = 2 / 3
---
# Which way is downhill?

⏱️ About 60 minutes

> **Warm-up:** you're standing on a hillside in thick fog and want to get down. You can only feel the ground right under your feet. What do you do?

You feel which way the ground slopes and step that way. Training does exactly that, and the slope is the **derivative**.

The derivative `f'(x)` is how fast `f` changes when `x` changes a tiny bit:

```
f'(x) ≈ (f(x + h) − f(x − h)) / (2h)       for a tiny h, like 0.00001
```

This **central difference** is a numerical estimate. It's how you *check* derivatives in practice (gradient checking), but it's far too slow to train with: one model has billions of weights.

Calculus gives exact formulas instead. The ones you need most:

| f(x) | f'(x) |
|---|---|
| `c` (a constant) | `0` |
| `xⁿ` | `n·xⁿ⁻¹` (so `x²` → `2x`) |
| `eˣ` | `eˣ` |
| `ln x` | `1/x` |
| `a·f(x) + b·g(x)` | `a·f'(x) + b·g'(x)` |
| `f(x)·g(x)` | `f'(x)·g(x) + f(x)·g'(x)` (product rule) |

Reading a derivative: `f'(x) > 0` means "increasing `x` increases `f`", so to make `f` *smaller* you move `x` the other way. `f'(x) = 0` means flat: a minimum, maximum or saddle.

Watch 3Blue1Brown's *Essence of Calculus*, chapters 1–4, alongside this.

## 🔬 Take the formula apart: the slope estimate

<div class="formula">f'(x) ≈ (<span class="k1">f(x + h)</span> − <span class="k2">f(x − h)</span>) / <span class="k3">(2h)</span></div>

- `f'(x)` ("f prime of x") is the **derivative**: the slope of `f` at the point `x`.
- `h` is a tiny step, like 0.00001 (Python: `1e-5`, "1 times ten to the minus 5").
- <span class="k1">f(x + h)</span>: the height a tiny step to the right.
- <span class="k2">f(x − h)</span>: the height a tiny step to the left.
- Subtract them: how much the height changed. <span class="k3">Divide by 2h</span>, the width between the two points.

That's "rise over run", the slope you know from a ramp: how much up per step to the side.

Numbers for `f(x) = x²` at `x = 3`, with a big h = 0.1 so you can follow it: f(3.1) = 9.61, f(2.9) = 8.41. (9.61 − 8.41) / 0.2 = 1.2 / 0.2 = **6**. And the exact rule below says 2x = 6. ✅

## 🔬 Take the rules apart

`xⁿ` means "x times itself n times". `x²` = x × x, `x³` = x × x × x.

| Rule | In words | Example |
|---|---|---|
| `c` → `0` | a constant never changes, so its slope is 0 | `7` → `0` |
| `xⁿ` → `n·xⁿ⁻¹` | bring the small number down in front, then make it one smaller | `x²` → `2·x¹` = `2x`; `x³` → `3x²` |
| `x` → `1` | that's `x¹`: 1 in front, `x⁰` = 1 | `x` → `1` |
| `a·f(x)` → `a·f'(x)` | a number in front just stays in front | `3x²` → `3 × 2x` = `6x` |
| `f + g` → `f' + g'` | do each part separately and add | |

Now `f(x) = 3x² − 4x + 7`, part by part:

1. `3x²` → 3 × 2x = **6x**
2. `−4x` → −4 × 1 = **−4**
3. `+7` → **0**

So `f'(x) = 6x − 4`.

**The lowest point.** At the bottom of a valley the ground is flat: slope 0. Solve `6x − 4 = 0` step by step:

1. Add 4 to both sides: `6x = 4`.
2. Divide both sides by 6: `x = 4/6 = 2/3` ≈ 0.667.

Check: f'(0) = −4 (negative: going right goes **down**), f'(2) = 8 (positive: going right goes **up**). So the bottom is between 0 and 2. ✅

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `def numeric_derivative(f, x):` | | `f` is a **function** passed in as an input. You call it with `f(...)` like any function. |
| `1e-5` | "one e minus five" | 0.00001 |
| `f(x + h)` | | runs the function at x + h |
| `(2 * h)` | | brackets, so the division is by the whole `2h` |
| `x ** 2` | "x to the power 2" | x² in Python |
| `2 / 3` | | 0.666…; Python works out the fraction for you |

### 👀 Worked example: a different function

`g(x) = 5x² + 2x`. Rules: `5x²` → 10x, `2x` → 2. So `g'(x) = 10x + 2`.

```python
def dg(x):
    return 10 * x + 2
```

Lowest point: 10x + 2 = 0 → 10x = −2 → x = −2/10 = **−0.2**.

## 🎯 Your quest

`numeric_derivative(f, x)`: replace `return 0` with:

1. `    h = 1e-5`
2. `    return (f(x + h) - f(x - h)) / (2 * h)`

`df(x)`: replace `return 0` with `    return 6 * x - 4`

`minimum_x`: change `None` to `2 / 3`.

The program prints the numeric and exact slope side by side. They should agree.

## Review

<details><summary>Roughly how many FLOPs does training take?</summary>About 6 × parameters × training tokens.</details>
<details><summary>What does the Chinchilla rule say?</summary>For a fixed compute budget, the best model uses about 20 training tokens per parameter.</details>
<details><summary>What is the derivative of x³ + 2x?</summary>3x² + 2: bring the 3 down and make it 2, and 2x gives 2.</details>
