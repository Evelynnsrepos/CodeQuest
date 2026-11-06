---
title: Embeddings: meaning as numbers
xp: 30
hint: dot: total = 0, then for i in range(len(a)): and inside it total = total + a[i] * b[i], then return total
hint: length: like dot, but loop over one list: total = total + x * x, and at the end return math.sqrt(total)
hint: cosine has one line: return dot(a, b) / (length(a) * length(b))
hint: closest is the "best so far" loop from lesson 01, with best_score = -2 and score = cosine(query, items[name])
---
# Similar meaning, nearby arrows

⏱️ About 30 minutes · four small functions

> **Warm-up:** "cat" and "kitten" look different as text. How could a computer know they're related?

**In one sentence:** an **embedding** turns text into a list of numbers so that similar meanings point in similar directions, and **cosine similarity** measures how similar two directions are.

## 💡 The idea in plain words

An **embedding** turns a word, a sentence or an image into a list of numbers, called a **vector**. Think of a vector as an **arrow**: `[3, 4]` means "3 steps right, 4 steps up".

The embedding model is trained so that things with similar meanings get arrows that **point the same way**. "kitten" and "cat" point almost the same way; "car" points somewhere else. Search engines, recommendations and RAG (lesson 07) all run on this: "find the text whose arrow points most like my question's arrow".

Real embeddings have hundreds of numbers (hundreds of directions, not just right and up). The maths is exactly the same as with 2 or 3.

**Cosine similarity** is one number that says how alike two directions are:

- **1** = exactly the same direction (same meaning)
- **0** = at a right angle (unrelated)
- **−1** = exactly opposite

## 🔢 The maths, one piece at a time

Cosine needs two smaller tools first.

### Tool 1: the dot product (a · b)

Multiply the numbers that are in the same position, then add those results up.

`a = [3, 4]`, `b = [4, 3]`:

1. position 0: 3 × 4 = 12
2. position 1: 4 × 3 = 12
3. add: 12 + 12 = **24**

The dot (·) between a and b is said "a dot b".

### Tool 2: the length of an arrow (|a|)

The two straight lines around a, |a|, mean "the length of a". To get it: square each number (multiply it by itself), add them up, then take the **square root**.

The **square root** (√) undoes squaring: √25 = 5, because 5 × 5 = 25. √9 = 3, because 3 × 3 = 9.

`a = [3, 4]`:

1. squares: 3 × 3 = 9 and 4 × 4 = 16
2. add: 9 + 16 = 25
3. square root: √25 = **5**

(That's the old right-triangle rule from school: an arrow 3 right and 4 up is 5 long.) And `b = [4, 3]` is also 5 long.

### Putting it together

<div class="formula">cos(a, b) = <span class="k1">a · b</span> <span class="k2">÷</span> <span class="k3">(|a| × |b|)</span></div>

| Piece | Say it | Means | Our example |
|---|---|---|---|
| cos(a, b) | "cosine of a and b" | how alike the two directions are | 0.96 |
| <span class="k1">a · b</span> | "a dot b" | multiply matching numbers, add up | 24 |
| <span class="k2">÷</span> | "divided by" | | |
| <span class="k3">(\|a\| × \|b\|)</span> | "length of a times length of b" | removes the effect of how **long** the arrows are, so only the **direction** counts | 5 × 5 = 25 |

So cos = 24 ÷ 25 = **0.96**: almost the same direction.

Why divide by the lengths? `[1, 2]` and `[2, 4]` point exactly the same way (the second is just twice as long). Dot = 1×2 + 2×4 = 10, lengths √5 ≈ 2.236 and √20 ≈ 4.472, and 10 ÷ (2.236 × 4.472) = 10 ÷ 10 = **1**. Same direction, so 1, no matter the length.

<div class="quiz" data-answer="1" data-why="The dot product is 1·0 + 0·1 = 0: they point at a right angle, so they’re unrelated."><p><b>Predict first:</b> what is the cosine similarity of [1, 0] and [0, 1]?</p><button>1</button><button>0</button><button>−1</button></div>

**Go deeper:** LLMs 1 lesson 11, LLMs 3 (RAG), Math 2 lessons 03–05, AI engineer 2.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `a[0]` | "a at 0" | the first number in the list. Python counts positions from **0**: `a[0]` is the first, `a[1]` the second. |
| `len(a)` | "length of a" | how many items the list has (not the arrow length!) |
| `range(len(a))` | "range of length of a" | the positions 0, 1, 2, … up to the last one |
| `total = total + x` | "total becomes total plus x" | takes what's in the box, adds x, puts the result back. A **running total**. |
| `math.sqrt(25)` | "square root of 25" | `5.0` |
| `x * x` | "x times x" | x squared |

### 👀 Worked example 1: a running total over positions

This adds the numbers at the same positions of two lists. It's the dot product with `+` instead of `×`:

```python
def add_matching(a, b):
    total = 0
    for i in range(len(a)):
        total = total + a[i] + b[i]
    return total
```

`add_matching([1, 2], [10, 20])`: start with total 0. i = 0: 0 + 1 + 10 = 11. i = 1: 11 + 2 + 20 = 33. Gives `33`.

### 👀 Worked example 2: a running total over one list

```python
def sum_of_doubles(v):
    total = 0
    for x in v:
        total = total + x * 2
    return total
```

`sum_of_doubles([3, 4])`: 0 + 6 = 6, then 6 + 8 = 14. Your `length` is the same with `x * x`, and then the square root at the end.

### Functions can use other functions

Once `dot` and `length` work, `cosine` can just call them: `dot(a, b)` runs your dot function and gives back its answer.

## 🎯 Your quest

1. `dot(a, b)`: like `add_matching`, but multiply: `total = total + a[i] * b[i]`.
2. `length(v)`: like `sum_of_doubles`, but `total = total + x * x`, and at the end `return math.sqrt(total)`.
3. `cosine(a, b)`: one line: `return dot(a, b) / (length(a) * length(b))`.
4. `closest(query, items)`: `items` is a dictionary name → vector, e.g. `{"kitten": [0.9, 0.8, 0.1], ...}`. Give back the **name** whose vector has the highest cosine with `query`. It's the "best so far" loop from lesson 01:
   - `best = None` and `best_score = -2` (cosine is never below −1, so the first item always beats −2)
   - `for name in items:` → inside: `score = cosine(query, items[name])`
   - `if score > best_score:` → `best = name` and `best_score = score`
   - after the loop: `return best`

**Remember:** meaning becomes direction; cosine measures it.
