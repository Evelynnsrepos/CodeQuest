---
title: Transpose and the identity matrix
xp: 35
---
# Flipping a matrix, and the matrix that does nothing

> **Warm-up:** the attention formula has `QKᵀ`. Q and K have the same shape (tokens × d). Why can't you just multiply `QK`?

**In one sentence:** transposing swaps rows and columns, and the identity matrix is the "1" of matrices: multiplying by it changes nothing.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `Aᵀ` | "A transpose" | rows become columns: `(Aᵀ)ᵢⱼ = Aⱼᵢ` | `[list(c) for c in zip(*A)]` |
| `I` or `Iₙ` | "the identity" / "I n" | n × n, ones on the diagonal, zeros elsewhere | |
| diagonal | | the entries `Aᵢᵢ` from top-left to bottom-right | `A[i][i]` |
| `A = Aᵀ` | "A is symmetric" | mirror image across the diagonal | |
| `aᵀb` | "a transpose b" | the dot product, written as (1 × n)(n × 1) | |

## The idea

```
A = [1 2 3]      Aᵀ = [1 4]
    [4 5 6]           [2 5]
                      [3 6]
(2 × 3)               (3 × 2)
```

- Transposing turns an `m × n` matrix into `n × m`. That's how you make shapes fit: Q is `T × d`, Kᵀ is `d × T`, so `QKᵀ` is `T × T`: one score for every pair of tokens.
- `(Aᵀ)ᵀ = A` (flip twice), and `(AB)ᵀ = BᵀAᵀ` (**order reverses**, like taking off socks and shoes).
- **Identity:** `IA = AI = A` and `Ix = x`.

```
I₃ = [1 0 0]
     [0 1 0]
     [0 0 1]
```

## 🗣️ Say it out loud

`QKᵀ` → "Q times K transpose" → "the dot product of every query with every key".

## 🧮 Worked example

`Q` is 3 tokens × 2, `K` is 3 × 2. `QK` is `(3×2)(3×2)`: invalid. `QKᵀ` is `(3×2)(2×3) = 3×3` ✓.

## 🤖 Where AI uses it

`QKᵀ` in attention; `XWᵀ` (PyTorch's `nn.Linear` stores W as out × in and computes `xWᵀ + b`); the gradient of a matrix product involves transposes (Math 3); residual connections act like adding an identity: `x + f(x) = (I + f)(x)` when f is linear.

## 🎯 Your quest

1. `transpose(A)`
2. `identity(n)`
3. `is_symmetric(A)`

**Remember:** transpose swaps rows and columns, `m × n` becomes `n × m`.

## Review

<details><summary>Shape of (5 × 3)(3 × 7)?</summary>5 × 7.</details>
<details><summary>Is AB always equal to BA?</summary>No, order matters.</details>
