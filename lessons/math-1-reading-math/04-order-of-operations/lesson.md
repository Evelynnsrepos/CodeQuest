---
title: Order of operations
xp: 25
---
# Which part do you calculate first?

> **Warm-up:** what is "2 plus 3 times 4"? Is it 20 or 14? Try both ways.

**In one sentence:** math has a fixed order for calculating, and brackets let you change it.

## 🪜 Plain words

If two people calculate the same line in a different order, they get different answers. So everyone agrees on an order: **brackets first, then powers, then times and divide, then plus and minus.** Brackets are like saying "do this bit first, I insist".

## 🪜 With numbers

"2 plus 3 times 4": times comes before plus, so first 3 times 4 is 12, then 2 plus 12 is **14**.

"(2 plus 3) times 4": the brackets come first, so 2 plus 3 is 5, then 5 times 4 is **20**.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `( )` | "brackets" / "parentheses" | do this part first | `( )` |
| `·` or `×` | "times" | multiply | `*` |
| `/` or a fraction bar | "divided by" / "over" | divide | `/` |
| a small raised number like `²` | "squared" | a power (lesson 7): `4²` = 4 times 4 | `** 2` |

The order, remembered as **BEDMAS**:

1. **B**rackets, innermost first
2. **E**xponents (powers)
3. **D**ivision and **M**ultiplication, left to right
4. **A**ddition and **S**ubtraction, left to right

**The big trap: a fraction bar is an invisible pair of brackets** around its whole top and its whole bottom.

## 🔬 Take the formula apart

**`(x + 1)² / 2x`** with `x = 3`, written with a fraction bar on paper:

```
 (x + 1)²
──────────
    2x
```

<div class="formula"><span class="k1">(x + 1)</span><span class="k2">²</span> <span class="k3">/</span> <span class="k4">2x</span></div>

| Piece | Say it | Means | With x = 3 |
|---|---|---|---|
| <span class="k1">(x + 1)</span> | "x plus one, in brackets" | add first, because of the brackets | 3 + 1 = 4 |
| <span class="k2">²</span> | "squared" | times itself | 4 · 4 = 16 |
| <span class="k3">/</span> (or the fraction bar) | "divided by" | top **group** divided by bottom **group** | |
| <span class="k4">2x</span> | "two x" | 2 times x (invisible times sign); all of it is the bottom | 2 · 3 = 6 |
| whole thing | | 16 divided by 6 | ≈ 2.667 |

In Python you must type the invisible brackets yourself: `(x + 1) ** 2 / (2 * x)`.

## 🔀 What if the formula were different?

<div class="wrong"><b>x + 1² / 2 · x</b> (all brackets forgotten): 1² = 1, then 1 / 2 = 0.5, then 0.5 · 3 = 1.5, then 3 + 1.5 = <b>4.5</b>.</div>
<div class="wrong"><b>(x + 1)² / 2 · x</b> (bottom bracket forgotten): 16 / 2 = 8, then 8 · 3 = <b>24</b>. The x jumped from the bottom to the top!</div>
<div class="wrong"><b>x + 1² / (2x)</b> (top bracket forgotten): only the 1 gets squared and divided: 3 + 1/6 ≈ <b>3.17</b>.</div>
<div class="right"><b>(x + 1)² / (2x)</b>: 16 / 6 ≈ <b>2.667</b> ✓</div>

Three missing brackets, three different wrong answers. That's why the order rules exist.

## 🗣️ Say it out loud

`(x + 1)² / 2x` → "x plus one, squared, divided by two x."

## 🤖 Where AI uses it

The attention score is `q·k / √d`: the **whole** `q·k` is divided by `√d`. Brackets in the wrong place are one of the most common bugs when turning papers into code.

## 🎯 Your quest

Write each with the right brackets, for any `x` (and `y`):

1. `p(x)` = `(x + 1)² / 2x` (the whole `2x` is the bottom)
2. `q(x, y)` = `(x − y) / (x + y)`
3. `r(x)` = `3x² − 2x + 1` (the square belongs only to x: `3 * x ** 2`)

**Remember:** a fraction bar puts invisible brackets around its top and its bottom.

## Review

<details><summary>Solve 3x − 2 = 10.</summary>Add 2: 3x = 12. Divide by 3: x = 4.</details>
<details><summary>What does 2x mean?</summary>2 times x.</details>
