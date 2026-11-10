---
title: Embeddings, meaning as numbers
minutes: 30
xp: 25
hint: dot: total = total + a[i] * b[i]. length: total = total + x * x, then return math.sqrt(total).
hint: cosine: dot(a, b) divided by (length(a) * length(b)). closest: score = cosine(query, items[name]).
distractor: total = total + a[i] + b[i]
distractor: return total * total
distractor: return dot(a, b) * (length(a) * length(b))
---
# Embeddings

⏱️ About 30 minutes · 🧩 5 gaps, 3 decoys

> **Warm-up:** "kitten" and "puppy" are different words. Why do they still feel close?

**In one sentence:** an **embedding** is a list of numbers for a piece of text, made so that similar meanings get similar numbers; we compare them with **cosine similarity**.

## 💡 The idea

Imagine giving each word three scores: *is it cute?*, *is it an animal?*, *is it a machine?*

- kitten → `[0.9, 0.8, 0.1]`
- puppy → `[0.8, 0.9, 0.0]`
- car → `[0.1, 0.0, 0.95]`

A list of numbers like that is a **vector**: an arrow pointing somewhere. Kitten and puppy point in almost the same direction; car points somewhere else. Real embeddings have hundreds of numbers that the model learned by itself, but the comparison works the same. This is how AI search ("find documents like this one") works.

## 🔢 The maths, step by step

We'll use the small vectors `a = [3, 4]` and `b = [4, 3]`.

**1. Dot product** (written a · b, "a dot b"): multiply the matching numbers, then add.
3 × 4 = 12, 4 × 3 = 12, and 12 + 12 = **24**.

**2. Length** (written ‖a‖, "the length of a"): square each number, add, take the square root.
- "Square" means times itself: 3² = 3 × 3 = 9, 4² = 16.
- 9 + 16 = 25.
- √25 ("square root of 25") asks "which number times itself is 25?" → **5**.

So ‖a‖ = 5, and ‖b‖ = 5 too.

**3. Cosine similarity:** the dot product divided by the two lengths multiplied:

  cos = (a · b) ÷ (‖a‖ × ‖b‖) = 24 ÷ (5 × 5) = 24 ÷ 25 = **0.96**

What the answer means: **1** = same direction (same meaning), **0** = unrelated, **−1** = opposite. 0.96 is very close.

## 🐍 The Python in this puzzle

| Piece | Say it | What it does |
|---|---|---|
| `range(len(a))` | "for every position in a" | gives 0, 1, 2 … one for each number |
| `a[i]` | "a at i" | the number at position i (counting from 0) |
| `total = total + ...` | "add to the running total" | the total grows each turn of the loop |
| `x * x` | "x times x" | x squared |
| `math.sqrt(25)` | "square root of 25" | `5.0` |
| `( ... )` | brackets | work this out first, like in school maths |

## 🧩 Your puzzle

1. `dot`: each turn, add **a[i] times b[i]** to the total (decoy: plus instead of times).
2. `length`: each turn, add **x times x**.
3. Then give back the **square root** of the total (decoy: `total * total`).
4. `cosine`: dot **divided by** (length × length). (Decoy: times instead of divided.)
5. `closest`: score each item with your `cosine`. The "best so far" loop around it is the same as in lesson 01.

Run it: `24 5.0 0.96 kitten`.

**Remember:** same direction = same meaning.
