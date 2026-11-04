---
title: Limits: where is it heading?
xp: 40
---
# Sneaking up on a number

> **Warm-up:** what is 0 ÷ 0? Try `0/0` in Python. Now what if you never actually reach 0, but get closer and closer?

**In one sentence:** a limit is the value a function **heads towards** as the input gets closer and closer to some point, even if you can't plug that point in.

## 🪜 Plain words

Imagine walking towards a wall, each step half the distance that's left. You never touch it, but you can say exactly **where you're heading**: the wall.

Some formulas break at one exact point (they'd divide by zero), but are perfectly fine right next to it. The limit asks: "If I sneak up really close, what number do the outputs settle on?"

For the limit to exist, sneaking up from the **left** and from the **right** must lead to the **same** number.

## 🪜 With numbers

Take `(x² − 1) / (x − 1)`. At x = 1 it's 0 ÷ 0: broken. But next to 1:

| x | 0.9 | 0.99 | 0.999 | 1 | 1.001 | 1.01 | 1.1 |
|---|---|---|---|---|---|---|---|
| output | 1.9 | 1.99 | 1.999 | 💥 | 2.001 | 2.01 | 2.1 |

From both sides it heads to **2**. So the limit is 2.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `lim` | "the limit" | where it is heading | (try smaller and smaller steps) |
| `x → 1` | "x goes to 1" / "x approaches 1" | x gets closer and closer to 1, but **never equals** 1 | `1 + h` with tiny `h` |
| `x → 1⁺` / `x → 1⁻` | "from the right" / "from the left" | only from above / only from below | `1 + h` / `1 - h` |
| `h → 0` | "h goes to zero" | a step that shrinks towards nothing | `h = 1e-6` |
| `∞` | "infinity" | bigger than any number; not a real number you can plug in | `float("inf")` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">lim</span><sub><span class="k2">x → 1</span></sub> &nbsp;<span class="k3">(x² − 1) / (x − 1)</span> = <span class="k4">2</span></div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k1">lim</span> | "the limit" | "where is this heading?" | |
| <span class="k2">x → 1</span> (written small underneath) | "as x goes to 1" | sneak up on 1 from both sides | x = 0.999, 1.001 |
| <span class="k3">(x² − 1) / (x − 1)</span> | "x squared minus one, over x minus one" | the function we're watching | 1.999, 2.001 |
| = <span class="k4">2</span> | "equals two" | the number it settles on | 2 |

## 🔀 What if it were different?

<div class="wrong"><b>Just plug in x = 1</b>: 0 / 0 → Python raises <code>ZeroDivisionError</code>. The limit's whole point is that you <b>don't</b> plug the point in.</div>
<div class="wrong"><b>Only check one side</b>: for <code>|x| / x</code> near 0, from the right you get +1, from the left −1. If you only checked the right, you'd wrongly say "the limit is 1". The two sides disagree, so there is <b>no</b> limit.</div>
<div class="wrong"><b>Use a step that's too big</b> (x = 1.5): output 2.5. That's where the function <i>is</i> at 1.5, not where it's <i>heading</i> at 1.</div>
<div class="right">sneak up from both sides with tiny steps → both say 2 ✓</div>

## 🗣️ Say it out loud

"The limit as x goes to 1 of x squared minus 1 over x minus 1 equals 2."

## 🤖 Where AI uses it

The derivative (next lesson) is defined as a limit, and the derivative is how every neural network learns. Limits also explain why softmax with temperature → 0 becomes "always pick the top token" (LLMs 1).

## 🎯 Your quest

1. `table(f, a, hs)`: list of `f(a + h)` for each `h` in `hs`.
2. `estimate_limit(f, a)`: the average of `f(a + 1e-6)` and `f(a - 1e-6)`.
3. `has_limit(f, a)`: `True` if `f(a + 1e-6)` and `f(a - 1e-6)` differ by less than `1e-3`.

**Remember:** a limit is where you're heading, from both sides, without arriving.

## Review

<details><summary>What does Δ mean?</summary>The change: after minus before.</details>
<details><summary>Loss 2.0 at step 0, 1.0 at step 500: rate?</summary>−1 / 500 = −0.002 per step.</details>
