---
title: Functions: f(x)
xp: 35
---
# A machine with an input slot

> **Warm-up:** you already write Python functions. What do you think `f(g(x))` might mean?

**In one sentence:** a math function is a rule that turns each input into exactly one output, just like a Python function.

## 🪜 Plain words

Picture a machine: you drop a number in the top, it does something, and a number comes out of the bottom. Same input, always same output. You can also connect machines: the output of the first one falls straight into the second.

## 🪜 With numbers

- The "double" machine: put in 5, get 10.
- The "add 3" machine: put in 2, get 5.
- Connect them, "add 3" first, then "double": 2 → 5 → 10.
- The other order, "double" first, then "add 3": 2 → 4 → 7. **Different!** Order matters.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `f` | "f" | the name of a function (a machine) | `def f(x):` |
| `f(x)` | "f of x" | what comes out when x goes in. **Not** "f times x"! | `f(x)` |
| `f(x) = x² + 1` | "f of x equals x squared plus one" | defines the machine | `def f(x): return x**2 + 1` |
| `f(g(x))` | "f of g of x" | put x into g, then the result into f | `f(g(x))` |
| `f ∘ g` | "f after g" | the combined machine | `lambda x: f(g(x))` |
| `f: ℝ → ℝ` | "f goes from reals to reals" | takes a number, gives a number | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">f</span>(<span class="k2">g</span>(<span class="k3">x</span>))</div>

| Piece | Say it | Means | With f = square, g = add 3, x = 2 |
|---|---|---|---|
| <span class="k3">x</span> | "x" | the input | 2 |
| <span class="k2">g</span>( … ) | "g of" | the **inner** machine: runs **first** | g(2) = 5 |
| <span class="k1">f</span>( … ) | "f of" | the **outer** machine: runs **second**, on g's output | f(5) = 25 |

Read nested brackets from the **inside out**, like nested Python calls.

## 🔀 What if the formula were different?

<div class="wrong"><b>g(f(x))</b> (order swapped): square first, then add 3: 2 → 4 → 7. Not 25.</div>
<div class="wrong"><b>f · g · x</b> (reading the brackets as "times"): makes no sense: f and g are machines, not numbers.</div>
<div class="right"><b>f(g(x))</b>: 2 → 5 → 25 ✓</div>

## 🗣️ Say it out loud

`y = σ(w·x + b)` → "y equals sigma of w times x plus b" → "compute w times x plus b, then put that into the machine σ."

## 🤖 Where AI uses it

A neural network **is** machines connected in a row: `output = layer₃(layer₂(layer₁(x)))`. The chain rule (Math 3) is how training finds out how each machine affects the final output.

## 🎯 Your quest

1. `compose(f, g)`: return a **new function** that computes `f(g(x))`.
2. `pipeline(fs, x)`: apply the functions in the list `fs` to `x` in order (`fs[0]` first) and return the result.

**Remember:** brackets after a function name mean "put this in", and nested ones run from the inside out.

## Review

<details><summary>Slope from (0, 1) to (2, 5)?</summary>(5 − 1) / (2 − 0) = 2.</details>
<details><summary>What does b mean in y = mx + b?</summary>The starting value: where the line crosses the y-axis.</details>
