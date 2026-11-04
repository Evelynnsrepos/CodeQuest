---
title: Vectors
xp: 30
---
# Lists of numbers with a direction

> **Warm-up:** in LLMs 1 you used embeddings and dot products. What does it mean, geometrically, to *add* two vectors?

A **vector** is a list of numbers, and you can picture it as an arrow from the origin. `[3, 4]` points 3 right and 4 up. The basic operations:

| Operation | Formula | Picture |
|---|---|---|
| addition `a + b` | `[a₁+b₁, a₂+b₂, …]` | put the arrows tip to tail |
| scaling `c·a` | `[c·a₁, c·a₂, …]` | stretch (or flip, if c < 0) |
| dot product `a · b` | `a₁b₁ + a₂b₂ + …` | `|a|·|b|·cos(angle)`: how much they point the same way |
| length (norm) `|a|` | `√(a · a)` | Pythagoras: `|[3, 4]| = 5` |

Every one of these is used in an LLM thousands of times per token:

- the **residual stream**: each layer *adds* its output vector onto the token's vector
- **scaling**: the learning rate scales the gradient vector before it's subtracted from the weights
- **dot products**: attention scores, logits
- **norms**: RMSNorm divides a vector by its (root-mean-square) length to keep sizes stable; gradient clipping caps the gradient's norm

The famous example of meaning-as-direction: in classic word embeddings, `vec("king") − vec("man") + vec("woman")` lands near `vec("queen")`.

## Your quest

Write `add(a, b)`, `scale(c, a)`, `dot(a, b)`, `norm(a)` and `rms_norm(a)`.

`rms_norm` divides every entry by the **root mean square** of the vector: `√( (a₁² + a₂² + … ) / n )`. (Real RMSNorm also adds a tiny epsilon and multiplies by learned weights; leave those out.) After it, the root mean square of the result is 1.

## Review

<details><summary>What does __call__ do in a Python class?</summary>It runs when you call the object like a function: model(x).</details>
<details><summary>How are big models built from classes?</summary>By nesting: blocks hold attention and MLP objects, the model holds a list of blocks.</details>
