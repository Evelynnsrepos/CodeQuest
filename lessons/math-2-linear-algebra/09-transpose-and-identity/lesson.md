---
title: Transpose and the identity matrix
xp: 35
---
# Flipping a matrix, and the matrix that does nothing

> **Warm-up:** Q and K are both "tokens × 64". You want every query dotted with every key. Why does Q times K not work?

**In one sentence:** transposing swaps rows and columns, and the identity matrix is the "1" of matrices.

## 🪜 Plain words

**Transpose** = flip the grid over its diagonal: the first row becomes the first column, and so on. A 2 × 3 grid becomes 3 × 2. It's how you make shapes fit.

The **identity** matrix has 1s on the diagonal (top-left to bottom-right) and 0s elsewhere. Multiplying by it changes nothing, like multiplying a number by 1.

## 🪜 With numbers

```
[1 2 3]   transposed:   [1 4]
[4 5 6]                 [2 5]
                        [3 6]
```

Q is 3 × 2, K is 3 × 2. Q times K: inner sizes 2 and 3, no. Q times K-transposed: (3 × 2)(2 × 3) = 3 × 3 ✓, one score per pair of tokens.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `Aᵀ` | "A transpose" | rows ↔ columns: `(Aᵀ)ᵢⱼ = Aⱼᵢ` | `[list(c) for c in zip(*A)]` |
| `I`, `Iₙ` | "the identity", "I n" | 1s on the diagonal, n × n | |
| diagonal | | entries `Aᵢᵢ` (same row and column number) | |
| symmetric | | `A = Aᵀ` | |

## 🔬 Take the formula apart

<div class="formula">(<span class="k1">A</span><sup><span class="k2">ᵀ</span></sup>)<sub><span class="k3">i</span><span class="k4">j</span></sub> = <span class="k1">A</span><sub><span class="k4">j</span><span class="k3">i</span></sub></div>

| Piece | Say it | Means |
|---|---|---|
| <span class="k1">A</span><sup><span class="k2">ᵀ</span></sup> | "A transpose" | the flipped matrix (the T is not a power!) |
| <sub><span class="k3">i</span><span class="k4">j</span></sub> | "row i, column j" | a spot in the flipped matrix… |
| <span class="k1">A</span><sub><span class="k4">j</span><span class="k3">i</span></sub> | "A j i" | …holds what was at row j, column i: **the letters swap** |

<div class="formula">(<span class="k1">A</span><span class="k2">B</span>)<sup>ᵀ</sup> = <span class="k2">B</span><sup>ᵀ</sup><span class="k1">A</span><sup>ᵀ</sup></div>

Transposing a product **reverses the order** (like socks and shoes: put on socks then shoes, take off shoes then socks).

## 🔀 What if it were different?

<div class="wrong"><b>(AB)ᵀ = AᵀBᵀ</b> (no reversal): for a 2×3 A and 3×4 B, Aᵀ is 3×2 and Bᵀ is 4×3: (3×2)(4×3) doesn't even fit.</div>
<div class="wrong"><b>Thinking ᵀ is a power</b> (A to the T): there's no number T. It's a flip.</div>
<div class="right"><b>BᵀAᵀ</b>: (4×3)(3×2) = 4×2 = the shape of (AB)ᵀ ✓</div>

## 🗣️ Say it out loud

`QKᵀ` → "Q K transpose" → "every query dotted with every key."

## 🤖 Where AI uses it

`QKᵀ` in attention, PyTorch layers computing `xWᵀ + b`, the backward pass of a matrix product (Math 3).

## 🎯 Your quest

1. `transpose(A)`
2. `identity(n)`
3. `is_symmetric(A)`

**Remember:** transpose swaps rows and columns.

## Review

<details><summary>Shape of (5 × 3)(3 × 7)?</summary>5 × 7.</details>
<details><summary>Is AB = BA?</summary>Usually not.</details>
