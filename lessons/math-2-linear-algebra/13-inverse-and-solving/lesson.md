---
title: Determinant, inverse and solving equations
xp: 50
---
# Undoing a matrix

> **Warm-up:** `3x = 12`. How do you find x? Now a matrix turned some vector x into b. How could you get x back?

**In one sentence:** the inverse `A⁻¹` undoes A, it exists only when the determinant isn't zero, and it solves `Ax = b`.

## 🪜 Plain words

For numbers, "times 3" is undone by "divided by 3". For matrices the undo-button is the **inverse**. But some matrices **squash** space flat (two different inputs give the same output); those can't be undone, like trying to un-blend a smoothie.

The **determinant** is one number that tells you how much a matrix stretches area. If it's 0, the matrix squashes everything flat: no inverse.

## 🪜 With numbers

Two equations: "2 apples + 1 melon cost 5" and "1 apple + 3 melons cost 10". As a matrix: `[[2, 1], [1, 3]]` times (apple, melon) = (5, 10).

- Determinant: 2·3 − 1·1 = 5 (not 0, so solvable).
- Solution: apple = 1, melon = 3. Check: 2·1 + 3 = 5 ✓, 1 + 3·3 = 10 ✓.

## 🔣 The signs

| Sign | Say it | Means |
|---|---|---|
| `det(A)` or `\|A\|` | "the determinant of A" | area scaling factor (here the bars do NOT mean absolute value!) |
| `A⁻¹` | "A inverse" | the undo-matrix: `A⁻¹A = I` (here ⁻¹ means "inverse", not 1/A) |
| `Ax = b` | "A x equals b" | a system of equations |
| singular | | det = 0, no inverse |

## 🔬 Take the formula apart

<div class="formula">det [[<span class="k1">a</span>, <span class="k2">b</span>], [<span class="k3">c</span>, <span class="k4">d</span>]] = <span class="k1">a</span><span class="k4">d</span> − <span class="k2">b</span><span class="k3">c</span></div>

| Piece | Say it | Means | [[2, 1], [1, 3]] |
|---|---|---|---|
| <span class="k1">a</span><span class="k4">d</span> | "a d" | top-left times bottom-right (one diagonal) | 2·3 = 6 |
| − | "minus" | | |
| <span class="k2">b</span><span class="k3">c</span> | "b c" | top-right times bottom-left (the other diagonal) | 1·1 = 1 → 5 |

<div class="formula"><span class="k5">A⁻¹</span> = <span class="k6">(1 / det)</span> · [[<span class="k4">d</span>, <span class="k2">−b</span>], [<span class="k3">−c</span>, <span class="k1">a</span>]]</div>

| Piece | Means | Example |
|---|---|---|
| <span class="k6">(1 / det)</span> | divide everything by the determinant | 1/5 |
| <span class="k4">d</span> and <span class="k1">a</span> | **swap places** | 3 top-left, 2 bottom-right |
| <span class="k2">−b</span>, <span class="k3">−c</span> | **flip their signs** | −1, −1 |
| result | | [[0.6, −0.2], [−0.2, 0.4]] |

Then `x = A⁻¹b`: (0.6·5 − 0.2·10, −0.2·5 + 0.4·10) = (1, 3) ✓.

## 🔀 What if it were different?

<div class="wrong"><b>det = ad + bc</b>: 7. Your inverse would be 5/7 too small, and x = (0.71, 2.14): wrong prices.</div>
<div class="wrong"><b>Forgetting to swap a and d</b>: [[2, −1], [−1, 3]]/5 → x = (0, 5). Check: 2·0 + 5 = 5 ✓ but 0 + 15 = 15 ✗.</div>
<div class="wrong"><b>[[1, 2], [2, 4]]</b>: det = 4 − 4 = 0 → dividing by 0. The two equations say the same thing twice, so there's no single answer.</div>
<div class="right">det 5, inverse [[0.6, −0.2], [−0.2, 0.4]], x = (1, 3) ✓</div>

## 🗣️ Say it out loud

`x = A⁻¹b` → "x equals A inverse b."

## 🤖 Where AI uses it

Linear regression's exact formula `w = (XᵀX)⁻¹Xᵀy`, Gaussian distributions, and understanding why a layer that squashes dimensions loses information for good.

## 🎯 Your quest

1. `det2(A)`
2. `inverse2(A)`: raise `ValueError` if det is 0.
3. `solve2(A, b)`: `A⁻¹b`.

**Remember:** det 0 = squashed flat = no undo.

## Review

<details><summary>LoRA parameters for 1000 × 1000 at r = 8?</summary>16,000.</details>
<details><summary>Rank of [[1, 2], [2, 4]]?</summary>1.</details>
