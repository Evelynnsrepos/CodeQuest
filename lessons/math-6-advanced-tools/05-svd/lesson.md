---
title: SVD: every matrix is rotate, stretch, rotate
xp: 65
---
# The idea behind LoRA and compression

> **Warm-up:** a 4096 × 4096 weight matrix has 16.7 million numbers. Could most of what it does be described with far fewer?

**In one sentence:** the singular value decomposition writes any matrix as A = U Σ Vᵀ: turn the input (Vᵀ), stretch along a few axes by the **singular values** σ (Σ), turn again (U); keeping only the biggest σ gives the best small approximation.

## 🪜 Plain words

Every matrix, however messy, does three simple things in a row: **rotate**, **stretch** each axis by some amount, **rotate** again. The stretch amounts are the **singular values**, sorted biggest first. If only a few are big, the matrix is "almost low-rank": keep those few and you keep almost all of its effect, with far fewer numbers.

How to find the biggest one: the matrix **AᵀA** is symmetric, and its eigenvalues are the **squares** of A's singular values. So power iteration on AᵀA (lesson 04) gives the top right direction v and σ₁ = √λ₁. Then the matching output direction is u = A v / σ₁.

## 🪜 With numbers

A = [[3, 0], [4, 5]].

- AᵀA = [[25, 20], [20, 25]]: eigenvalues 45 and 5, so **σ₁ = √45 = 6.708**, **σ₂ = √5 = 2.236**.
- Top direction v = (0.707, 0.707); A v = (2.121, 6.364); u = A v / 6.708 = (0.316, 0.949).
- **Rank-1 approximation** σ₁ u vᵀ = [[1.5, 1.5], [4.5, 4.5]]. Its error (the "Frobenius norm" of A − approximation: square every entry, add, square root) is √5 = **2.236 = σ₂**. Exactly the singular value we dropped.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `Aᵀ` | "A transpose" | rows become columns | `[list(c) for c in zip(*A)]` |
| `σ` | "sigma" | a singular value: a stretch amount | `math.sqrt(lam)` |
| `u`, `v` | "u", "v" | output and input directions (length 1) | |
| `u vᵀ` | "u v transpose" | the "outer product": matrix with entries uᵢ·vⱼ | `[[a * b for b in v] for a in u]` |
| `‖A‖_F` | "Frobenius norm" | √(sum of squared entries): a matrix's size | |
| rank r | "rank" | how many σ are not zero | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">A</span> ≈ <span class="k2">σ₁</span> <span class="k3">u₁</span> <span class="k4">v₁ᵀ</span> + <span class="k2">σ₂</span> <span class="k3">u₂</span> <span class="k4">v₂ᵀ</span> + …</div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k4">v₁ᵀ</span> | "v one transpose" | which input direction to read | (0.707, 0.707) |
| <span class="k2">σ₁</span> | "sigma one" | how strongly it's stretched | 6.708 |
| <span class="k3">u₁</span> | "u one" | which output direction it goes to | (0.316, 0.949) |
| + … | "plus more terms" | each further term adds less (smaller σ) | σ₂ = 2.236 |
| <span class="k1">A</span> | "A" | the whole matrix | [[3, 0], [4, 5]] |

## 🔀 What if it were different?

<div class="wrong"><b>Use eigenvalues of A itself</b>: A = [[3, 0], [4, 5]] has eigenvalues 3 and 5, not 6.708 and 2.236. Eigenvalues only work this way for symmetric matrices; singular values work for every matrix, even non-square ones.</div>
<div class="wrong"><b>Forget the square root</b>: σ₁ = 45 would make the rank-1 approximation 6.7× too big.</div>
<div class="wrong"><b>Keep the smallest σ instead of the biggest</b>: 2.236 u₂ v₂ᵀ leaves an error of 6.708 instead of 2.236.</div>
<div class="right">σ = 6.708 and 2.236; rank-1 error = σ₂ = 2.236 ✓</div>

## 🗣️ Say it out loud

"A is approximately sigma one u one v one transpose plus sigma two u two v two transpose, and so on."

## 🤖 Where AI uses it

**LoRA** (LLMs 6 lesson 05) bets that the weight *update* is low-rank: B·A with rank 8–64 instead of a full matrix. **Compressing** layers and embeddings, recommendation systems, and analysing what a trained matrix does (how many directions really matter) all use SVD.

## 🎯 Your quest

1. `transpose(A)`, `matmul(A, B)`.
2. `top_singular(A, steps=200)`: return `(sigma, u, v)` using power iteration on `AᵀA` (start from all ones, normalize each step).
3. `rank1(A)`: σ₁ u vᵀ as a matrix.
4. `frobenius(A)`.
5. `lora_params(d, k, r)`: numbers in a rank-r update of a d×k matrix (`r · (d + k)`), and `full_params(d, k)` = `d · k`.

**Remember:** rotate, stretch, rotate; keep the big stretches.

## Review

<details><summary>What does an eigenvalue of the covariance matrix tell you?</summary>How much variance the data has along that eigenvector's direction.</details>
