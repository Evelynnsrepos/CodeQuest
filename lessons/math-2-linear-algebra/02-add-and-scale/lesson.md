---
title: Adding and scaling vectors
xp: 35
---
# Arrows you can stack and stretch

> **Warm-up:** you walk 3 steps east and 1 north. Then 1 east and 2 north. Where are you compared to the start?

**In one sentence:** add vectors position by position, and multiply a vector by a number by multiplying every entry.

## 🪜 Plain words

Walking one arrow and then another is **adding** them: the east steps add up, the north steps add up, separately.

Making an arrow twice as long (same direction) is **scaling** it: every entry doubles. Multiplying by a negative number turns it around.

## 🪜 With numbers

- East: 3 + 1 = 4. North: 1 + 2 = 3. So (3, 1) + (1, 2) = **(4, 3)**.
- Twice (3, 1): 2 times 3 = 6, 2 times 1 = 2 → **(6, 2)**.
- 0.5 of (2, 4) plus 2 of (1, −1): (1, 2) + (2, −2) = **(3, 0)**.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| **v** + **w** | "v plus w" | add position by position | `[a + b for a, b in zip(v, w)]` |
| c**v** | "c times v" (c is a plain number) | multiply every entry by c | `[c * a for a in v]` |
| **v** − **w** | "v minus w" | subtract position by position | |
| a₁**v**₁ + a₂**v**₂ | "a one v one plus a two v two" | a **linear combination**: scale several vectors, then add | |

⚠️ In plain Python, `[1, 2] + [3, 4]` gives `[1, 2, 3, 4]` (glues lists!) and `2 * [1, 2]` gives `[1, 2, 1, 2]`. Math needs the loops above.

## 🔬 Take the formula apart

<div class="formula"><span class="k1">a</span>·<span class="k2">v</span> <span class="k3">+</span> <span class="k4">b</span>·<span class="k5">w</span></div>

| Piece | Say it | Means | a=0.5, v=(2,4), b=2, w=(1,−1) |
|---|---|---|---|
| <span class="k1">a</span> | "a" | a plain number: how much of v | 0.5 |
| <span class="k2">v</span> | "v" | the first vector | (2, 4) |
| <span class="k1">a</span>·<span class="k2">v</span> | "a times v" | each entry of v times a | (1, 2) |
| <span class="k4">b</span>·<span class="k5">w</span> | "b times w" | each entry of w times b | (2, −2) |
| <span class="k3">+</span> | "plus" | add position by position | (1+2, 2−2) = (3, 0) |

## 🔀 What if it were different?

<div class="wrong"><b>Gluing instead of adding</b> (Python list +): (2, 4) + (1, −1) becomes (2, 4, 1, −1): four numbers, a totally different thing.</div>
<div class="wrong"><b>Scaling only the first entry</b>: 2·(3, 1) = (6, 1). The arrow changes direction instead of just getting longer.</div>
<div class="right">0.5·(2, 4) + 2·(1, −1) = (3, 0) ✓</div>

## 🗣️ Say it out loud

`x + attention(x)` → "x plus attention of x" → "add what attention found to the token's vector, entry by entry" (a residual connection).

## 🤖 Where AI uses it

Residual connections, the training step `θ − η∇L` (a scaled vector subtracted), attention's output (a weighted mix of vectors), `king − man + woman ≈ queen`.

## 🎯 Your quest

1. `add(v, w)`
2. `scale(c, v)`
3. `lin_comb(coeffs, vectors)`: `coeffs[0]·vectors[0] + coeffs[1]·vectors[1] + …`

**Remember:** vector math goes position by position.

## Review

<details><summary>Python index of v₃?</summary>v[2].</details>
<details><summary>What does x ∈ ℝ⁷⁶⁸ say?</summary>x is a list of 768 numbers.</details>
