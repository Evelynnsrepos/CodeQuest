---
title: PCA: find the main directions
xp: 60
---
# Squash 768 numbers into 2, keep what matters

> **Warm-up:** a cloud of points is shaped like a long, thin cigar. If you could keep only one direction, which one?

**In one sentence:** PCA (principal component analysis) finds the directions in which the data spreads the most; they are the eigenvectors of the covariance matrix, and the eigenvalue says how much spread lies along each.

## 🪜 Plain words

Data often spreads mostly along a few directions. PCA finds them, biggest first:

1. **Center** the data (subtract each column's mean).
2. Compute the **covariance matrix** (lesson 01).
3. Its **eigenvectors** (Math 2 lesson 14: directions a matrix only stretches) are the main directions. The **eigenvalue** of each = the variance along it.
4. **Project** each point onto the top k directions (lesson 03). Now each point is k numbers instead of many.

How to find the biggest eigenvector without a library: **power iteration**. Start with any vector, multiply by the matrix, normalize to length 1, repeat. The biggest direction grows fastest and takes over.

## 🪜 With numbers

Covariance matrix C = [[2, 1], [1, 2]].

- Start v = (1, 0). C·v = (2, 1) → normalize → (0.894, 0.447).
- C·v = (2.236, 1.789) → (0.781, 0.625). Then (0.733, 0.680) … → **(0.707, 0.707)**.
- C·(0.707, 0.707) = (2.121, 2.121) = **3** · (0.707, 0.707). Eigenvalue **3**.

The other direction is (0.707, −0.707) with eigenvalue 1. Share of variance on the first: 3 / (3 + 1) = **75%**.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `C` | "C" | the covariance matrix | `cov_matrix(columns)` |
| `v` | "v" | an eigenvector: a direction | `[0.707, 0.707]` |
| `λ` | "lambda" | its eigenvalue: variance along v | `3` |
| `C v = λ v` | "C v equals lambda v" | C only stretches v | |
| `vᵀ C v` | "v transpose C v" | the variance along a unit vector v | `dot(v, matvec(C, v))` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">C</span> <span class="k2">v</span> = <span class="k3">λ</span> <span class="k2">v</span> &nbsp;&nbsp; share = <span class="k3">λ₁</span> / <span class="k4">Σ λ</span></div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k1">C</span> | "C" | how the columns vary together | [[2, 1], [1, 2]] |
| <span class="k2">v</span> | "v" | a main direction (length 1) | (0.707, 0.707) |
| <span class="k3">λ</span> | "lambda" | spread along v | 3 |
| <span class="k4">Σ λ</span> | "sum of lambdas" | total spread (= sum of the diagonal) | 4 |
| <span class="k3">λ₁</span> / <span class="k4">Σ λ</span> | "explained variance" | share kept by the first direction | 0.75 |

## 🔀 What if it were different?

<div class="wrong"><b>Skip centering</b>: data around (100, 100) makes the first "direction" point at the mean, not along the spread.</div>
<div class="wrong"><b>Don't normalize in power iteration</b>: the vector grows by ×3 every step and overflows after a few hundred steps, though its direction is right.</div>
<div class="wrong"><b>Mix units</b> (meters and millimeters): the millimeter column has a million times the variance and becomes "the" direction. Standardize first when units differ.</div>
<div class="right">top direction (0.707, 0.707), λ = 3, 75% of the variance ✓</div>

## 🗣️ Say it out loud

"C v equals lambda v; the share kept is lambda one over the sum of the lambdas."

## 🤖 Where AI uses it

Plotting embeddings in 2-D, compressing features, removing noise, and checking whether a model's hidden states really use all their dimensions. LoRA's idea (Math 2 lesson 12) is that weight **updates** have only a few important directions, the same idea.

## 🎯 Your quest

1. `power_iteration(C, steps=100)`: return `(v, λ)`: start from all ones, multiply and normalize `steps` times; λ = vᵀCv.
2. `explained(C)`: `λ₁ / trace(C)` (trace = sum of the diagonal = sum of all eigenvalues).
3. `pca_1d(rows)`: `rows` is a list of points. Center the columns, build the covariance matrix, find the top direction, and return each centered point's coordinate along it (the dot product). Make the sign deterministic: flip `v` so its largest-magnitude entry is positive.

**Remember:** center, covariance, eigenvectors, project.

## Review

<details><summary>What is the leftover after projecting a onto b?</summary>a minus the projection; it's perpendicular to b.</details>
