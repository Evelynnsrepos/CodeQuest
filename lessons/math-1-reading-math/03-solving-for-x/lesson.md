---
title: Equations: solving for x
xp: 35
---
# Finding the missing number

> **Warm-up:** "I bought some apples at 2 euros each, plus a 1 euro bag, and paid 9 euros." How many apples? How did you figure it out?

**In one sentence:** an equation is a balance, and you find the unknown by doing the same thing to both sides until the unknown stands alone.

## 🪜 Plain words

Picture an old balance scale. Both sides weigh the same. If you take 1 kg off the left, you must take 1 kg off the right too, or it tips. If you halve the left, halve the right.

To find a hidden number, **undo** what was done to it, in reverse order, doing each step to **both sides**.

## 🪜 With numbers

Apples: "2 times the apples, plus 1, makes 9."

1. Undo the "plus 1": take 1 from both sides. 9 minus 1 is 8. So "2 times the apples is 8."
2. Undo the "times 2": divide both sides by 2. 8 divided by 2 is 4.
3. **4 apples.** Check: 2 times 4 is 8, plus 1 is 9 ✓.

## 🔣 The signs

| Sign | Say it | Means |
|---|---|---|
| `x` | "x" | the unknown: the box whose number we're looking for |
| `=` | "equals" | the balance point: both sides are the same |
| "solve for x" | | get `x` alone on one side |
| `⇒` | "so" / "which means" | the next line follows from this one |
| `?` | | sometimes used for the unknown |

**Opposites** that undo each other: plus ↔ minus, times ↔ divided by.

## 🔬 Take the formula apart

The apple equation:

<div class="formula"><span class="k1">2</span><span class="k2">x</span> <span class="k3">+ 1</span> = <span class="k4">9</span></div>

| Piece | Say it | Means | In our example |
|---|---|---|---|
| <span class="k1">2</span> | "two" | price per apple | 2 |
| <span class="k2">x</span> | "x" | the unknown number of apples | ? (turns out 4) |
| <span class="k1">2</span><span class="k2">x</span> | "two x" | 2 **times** x (invisible times sign) | |
| <span class="k3">+ 1</span> | "plus one" | the bag fee | |
| `=` | "equals" | balance point | |
| <span class="k4">9</span> | "nine" | what you paid | 9 |

Solving it, one step per line (the `⇒` means "so"):

```
2x + 1 = 9
⇒ 2x = 8        (minus 1 on both sides)
⇒ x = 4         (divided by 2 on both sides)
```

The general version, for **`ax + b = c`** (a, b, c are known numbers):

| Piece | Say it | Means |
|---|---|---|
| `a` | "a" | the number multiplying x |
| `x` | "x" | the unknown |
| `ax` | "a x" | a times x |
| `+ b` | "plus b" | a number added |
| `= c` | "equals c" | the result |

Undo `+ b` (subtract b), then undo `· a` (divide by a):

<div class="formula"><span class="k2">x</span> = (<span class="k4">c</span> <span class="k3">− b</span>) <span class="k1">/ a</span></div>

| Piece | Say it | Means | Apples (a=2, b=1, c=9) |
|---|---|---|---|
| <span class="k2">x</span> = | "x equals" | x now stands alone: solved | |
| (<span class="k4">c</span> | "c" | the result we know | 9 |
| <span class="k3">− b</span>) | "minus b" | undo the adding first (brackets: do this first) | 9 − 1 = 8 |
| <span class="k1">/ a</span> | "divided by a" | then undo the multiplying | 8 / 2 = 4 |

## 🔀 What if the formula were different?

<div class="wrong"><b>x = c − b / a</b> (no brackets): divide happens first, so 9 − 1/2 = 8.5 apples. Half an apple!</div>
<div class="wrong"><b>x = (c + b) / a</b> (undid the wrong way): (9 + 1) / 2 = 5 apples. Check: 2·5 + 1 = 11, not 9. Always undo with the <i>opposite</i> operation.</div>
<div class="wrong"><b>x = (c − b) · a</b>: (9 − 1) · 2 = 16 apples. Undoing "times 2" needs "divided by 2".</div>
<div class="right"><b>x = (c − b) / a</b>: (9 − 1) / 2 = 4 ✓, and the check 2·4 + 1 = 9 works.</div>

## 🗣️ Say it out loud

`x = (c − b) / a` → "x equals c minus b, all divided by a."

## 🤖 Where AI uses it

Rearranging formulas: "how much context fits in my VRAM?" is solving the VRAM formula for the number of tokens (LLMs 2). "How many tokens for this compute budget?" is solving `C = 6ND` for D.

## 🎯 Your quest

1. `solve(a, b, c)`: return `x` for `ax + b = c`.
2. `check(a, b, c, x)`: `True` if `a·x + b` equals `c` (within `1e-9`).
3. `max_tokens(budget, model_size, per_token)`: solve `model_size + per_token · tokens = budget` for `tokens`.

**Remember:** do the same thing to both sides, undo in reverse order.

## Review

<details><summary>What's the opposite of "times 3"?</summary>Divided by 3.</details>
<details><summary>What does ≤ mean?</summary>Less than or equal to.</details>
