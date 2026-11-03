---
title: Order of operations
xp: 25
---
# Which part do you calculate first?

> **Warm-up:** what is `2 + 3 · 4`? Is it 20 or 14?

**In one sentence:** math has a fixed order for calculating, and brackets let you change it.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `( )` | "brackets" / "parentheses" | do this part first | `( )` |
| `·` or `×` | "times" | multiply | `*` |
| `a / b` or a fraction bar | "a over b" | divide | `a / b` |
| `−` | "minus" | subtract | `-` |

## The idea

The order, from first to last (remember **"BEDMAS"**: Brackets, Exponents, Division and Multiplication, Addition and Subtraction):

1. **B**rackets, innermost first
2. **E**xponents (powers like `x²`)
3. **D**ivision and **M**ultiplication, left to right
4. **A**ddition and **S**ubtraction, left to right

So `2 + 3 · 4 = 2 + 12 = 14`. Python follows the same order.

**The trap: fraction bars are invisible brackets.** In a written fraction, everything on top is one group and everything below is another:

```
 x + 1
───────   means   (x + 1) / (2 * x)     NOT   x + 1 / 2 * x
  2x
```

The same goes for exponents: `e^(x+1)` means `math.exp(x + 1)`.

## 🗣️ Say it out loud

`(x + 1)² / 2x` → "x plus one, squared, divided by two x." Each comma is a group.

## 🧮 Worked example

`(x + 1)² / 2x` with `x = 3`:

1. Brackets: `x + 1 = 4`
2. Exponent: `4² = 16`
3. Bottom group: `2x = 6`
4. Divide: `16 / 6 ≈ 2.667`

Without the hidden brackets, `x + 1 ** 2 / 2 * x` in Python gives `3 + 1 / 2 * 3 = 4.5`. Wrong!

## 🤖 Where AI uses it

The attention score is `q·k / √d`: the whole dot product is divided, not just `k`. Putting brackets in the wrong place is one of the most common bugs when turning papers into code.

## 🎯 Your quest

Write each with the right brackets, for any `x` (and `y`):

1. `p(x)` = `(x + 1)² / 2x`
2. `q(x, y)` = `(x − y) / (x + y)` (written as one fraction)
3. `r(x)` = `3x² − 2x + 1`

**Remember:** a fraction bar puts invisible brackets around its top and its bottom.

## Review

<details><summary>How do you write 2πr in Python?</summary>2 * math.pi * r</details>
<details><summary>What's 10 − 2 · 3?</summary>4 (multiplication first).</details>
