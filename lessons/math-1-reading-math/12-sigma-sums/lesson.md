---
title: Σ: the adding-up sign
xp: 40
---
# A for loop that adds things up

> **Warm-up:** you have 5 numbers. Describe in words how you'd get their average.

**In one sentence:** the big `Σ` means "add up a list of things", and it's exactly a `for` loop with a running total.

## 🪜 Plain words

To get an average: add up everything, then divide by how many there are. "Add up everything" happens so often that math has a single sign for it, a big Greek letter S (for **S**um) called **sigma**: `Σ`. Around it, small notes say **which items** to add.

## 🪜 With numbers

Average of 2, 4 and 9: add them, 2 + 4 + 9 = 15. There are 3 numbers. 15 divided by 3 = **5**.

"Add up the squares of 1, 2, 3": 1 times 1 is 1, 2 times 2 is 4, 3 times 3 is 9. Total: 1 + 4 + 9 = **14**.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `Σ` | "sigma" / "the sum of" | add up | `sum(...)` or a loop |
| `xᵢ` | "x sub i" / "x i" | item number i of the list x (the small low letter is the **position**) | `x[i - 1]` |
| `i = 1` under Σ | "from i equals one" | the counter is called i and starts at 1 | `range(1, …)` |
| `n` above Σ | "to n" | the counter stops at n (**included**) | `range(1, n + 1)` |
| `n` | "n" | how many items | `len(x)` |
| `x̄` | "x bar" | the average (mean) of x | `sum(x) / len(x)` |

Watch out: math counts from **1**, Python from **0**. `x₁` in math is `x[0]` in Python.

## 🔬 Take the formula apart

The average:

<div class="formula"><span class="k1">x̄</span> = <span class="k2">(1/n)</span> <span class="k3">Σ</span><sub><span class="k4">i=1</span></sub><sup><span class="k5">n</span></sup> <span class="k6">xᵢ</span></div>

| Piece | Say it | Means | For 2, 4, 9 |
|---|---|---|---|
| <span class="k1">x̄</span> | "x bar" | the answer: the average | 5 |
| <span class="k2">(1/n)</span> | "one over n" | divide by how many there are | 1/3 |
| <span class="k3">Σ</span> | "the sum of" | add up… | |
| <sub><span class="k4">i=1</span></sub> (below) | "from i equals 1" | start counting at item 1 | |
| <sup><span class="k5">n</span></sup> (above) | "to n" | stop at item n, **including** it | n = 3 |
| <span class="k6">xᵢ</span> | "x i" | …item number i, for each i | 2, 4, 9 |

Step by step: i = 1 → x₁ = 2; i = 2 → x₂ = 4; i = 3 → x₃ = 9. Sum 15. Times 1/3 → 5.

As Python, piece by piece:

```python
total = 0
for i in range(1, n + 1):   # Σ from i=1 to n (top included!)
    total += x[i - 1]       # x_i (math counts from 1)
x_bar = (1 / n) * total     # (1/n) · Σ
```

## 🔀 What if the formula were different?

<div class="wrong"><b>Σ from i=1 to n−1</b> (stopping one early, like Python's range): 2 + 4 = 6, average 2. You lost the last item.</div>
<div class="wrong"><b>Σ xᵢ</b> without (1/n): 15. That's the total, not the average.</div>
<div class="wrong"><b>(1/n) Σ xᵢ²</b> (extra square): (4 + 16 + 81)/3 ≈ 33.7. A different thing (the mean of the squares).</div>
<div class="right"><b>(1/n) Σᵢ₌₁ⁿ xᵢ</b> = 15 / 3 = 5 ✓</div>

## 🗣️ Say it out loud

`x̄ = (1/n) Σᵢ₌₁ⁿ xᵢ` → "x bar equals one over n times the sum from i equals one to n of x i" → "add them all up, divide by how many."

## 🤖 Where AI uses it

Everywhere: the dot product `Σᵢ aᵢbᵢ` (Math 2), mean squared error, the softmax bottom `Σⱼ e^(zⱼ)`, the total loss over a dataset.

## 🎯 Your quest

1. `sigma(f, start, end)`: `f(start) + f(start + 1) + … + f(end)` (**end included**).
2. `mean(xs)`: `(1/n) Σ xᵢ`.
3. `mse(ys, preds)`: `(1/n) Σᵢ (yᵢ − ŷᵢ)²`: the average of the squared errors.

**Remember:** Σ is a loop with a running total, and the top number is included.

## Review

<details><summary>In f(g(x)), which runs first?</summary>g, the inner one.</details>
<details><summary>Write 2.5 · 10⁻³ in Python.</summary>2.5e-3</details>
