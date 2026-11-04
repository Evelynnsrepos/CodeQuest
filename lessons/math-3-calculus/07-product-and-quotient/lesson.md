---
title: Product and quotient rules
xp: 45
---
# When two changing things multiply

> **Warm-up:** a rectangle is 4 m wide and 3 m tall. Width grows 1 m per second, height grows 0.5 m per second. How fast is the area growing right now?

**In one sentence:** for two things multiplied, the slope is "first's slope × second, plus first × second's slope"; for a division there's a matching rule with a minus and a square.

## 🪜 Plain words

The area grows for two reasons at once: the width grows (adding a strip as tall as the height), **and** the height grows (adding a strip as wide as the width). Add both strips.

Warm-up: width growth 1 × height 3 = 3, plus width 4 × height growth 0.5 = 2. Total: **5 m² per second**.

## 🪜 With numbers

x² · (x + 1) at x = 2. First f = x²: value 4, slope 2x = 4. Second g = x + 1: value 3, slope 1.

- f' · g = 4 · 3 = 12
- f · g' = 4 · 1 = 4
- Sum: **16**.

Check: x²(x + 1) = x³ + x², derivative 3x² + 2x = 12 + 4 = 16 ✓.

Division: x² / (x + 1) at x = 2: ( 4·3 − 4·1 ) / 3² = 8/9 ≈ **0.889**.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `f · g` | "f times g" | two functions multiplied | `f(x) * g(x)` |
| `f / g` | "f over g" | divided | `f(x) / g(x)` |
| `f'`, `g'` | "f prime", "g prime" | their slopes | |
| `g²` | "g squared" | g times g | `g ** 2` |

## 🔬 Take the formulas apart

<div class="formula">( f · g )' = <span class="k1">f'</span> · <span class="k2">g</span> + <span class="k3">f</span> · <span class="k4">g'</span></div>

| Piece | Say it | Means | x²(x + 1) at 2 |
|---|---|---|---|
| <span class="k1">f'</span> · <span class="k2">g</span> | "f prime times g" | first one changes, second held still | 4 · 3 = 12 |
| + | "plus" | both effects count | |
| <span class="k3">f</span> · <span class="k4">g'</span> | "f times g prime" | second one changes, first held still | 4 · 1 = 4 |

<div class="formula">( f / g )' = ( <span class="k1">f'</span> · <span class="k2">g</span> − <span class="k3">f</span> · <span class="k4">g'</span> ) / <span class="k5">g²</span></div>

| Piece | Means | x² / (x + 1) at 2 |
|---|---|---|
| <span class="k1">f'</span> · <span class="k2">g</span> | top grows → result grows | 4 · 3 = 12 |
| − <span class="k3">f</span> · <span class="k4">g'</span> | bottom grows → result **shrinks** (so: minus) | − 4 · 1 = −4 |
| / <span class="k5">g²</span> | divide by bottom squared | / 9 → 8/9 |

## 🔀 What if it were different?

<div class="wrong"><b>(f · g)' = f' · g'</b>: 4 · 1 = 4 instead of 16. The most common beginner mistake: slopes don't multiply like that for products (that's only the chain rule's thing).</div>
<div class="wrong"><b>Quotient with + instead of −</b>: 16/9 ≈ 1.78 instead of 0.89. A growing bottom makes a fraction smaller, so it must subtract.</div>
<div class="wrong"><b>Quotient divided by g instead of g²</b>: 8/3 ≈ 2.67. Three times too big.</div>
<div class="right">product 16, quotient 8/9 ✓</div>

## 🗣️ Say it out loud

"f g prime equals f prime g plus f g prime." For division: "low d-high minus high d-low, over low squared" (an old classroom rhyme: low = bottom, high = top).

## 🤖 Where AI uses it

Gates in LSTMs and GLU/SwiGLU layers multiply two signals (`gate · value`), so their gradients use the product rule. Softmax is a quotient (eˣⁱ / Σeˣʲ), and its famous gradient `p − y` (Math 5) comes from the quotient rule.

## 🎯 Your quest

Both functions get **values** (not functions): `f`, `df`, `g`, `dg` at the point.

1. `d_product(f, df, g, dg)`.
2. `d_quotient(f, df, g, dg)`.

**Remember:** product: f'g + fg'. Quotient: (f'g − fg') / g².

## Review

<details><summary>Slope of (3x + 1)² at x = 2?</summary>2 · 7 · 3 = 42.</details>
<details><summary>Chain rule in four words?</summary>Outside slope times inside slope.</details>
