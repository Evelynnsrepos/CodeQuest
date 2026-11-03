---
title: micrograd 3: tanh, powers and ReLU
xp: 50
---
# Every operation brings its local derivative

> **Warm-up:** to build a neural network you need a non-linear "activation" after each layer. Why? What would stacking only `w·x + b` layers give you?

Just another `w·x + b`: a stack of linear layers collapses into a single linear layer, so it can only learn straight lines. An **activation function** between layers bends the space and lets networks approximate almost any function. Each one is an operation with its own local derivative:

| Operation | Forward | Local derivative |
|---|---|---|
| `x ** k` (k a plain number) | `xᵏ` | `k · xᵏ⁻¹` |
| `tanh(x)` | squashes into (−1, 1) | `1 − tanh(x)²` |
| `relu(x)` | `max(0, x)` | `1` if `x > 0`, else `0` |

With `**` you also get division for free: `a / b = a · b⁻¹`, and subtraction is `a + (−1)·b`. (Those are the extra one-line methods at the bottom of the class.)

**ReLU** is the classic activation of modern networks; LLMs use smooth relatives like **GELU** and **SwiGLU** (Llama, Qwen) in their MLP blocks. The principle is identical: forward value, local derivative, chain rule.

A sanity check you should always know: compare autograd with the numerical derivative (LLMs 4, lesson 6). If they disagree, a `_backward` is wrong. The check does this for you.

## Your quest

Fill in the three `_backward` functions. Each one adds *(local derivative) × `out.grad`* to `self.grad`. The forward parts are done; `t` in `tanh` is already the forward result.

## Review

<details><summary>How does addition pass gradients backward? Multiplication?</summary>Addition routes out.grad unchanged to both inputs. Multiplication gives each input the other input's value times out.grad.</details>
<details><summary>Why use += when accumulating gradients?</summary>A value used in several places gets gradient from each use, and those contributions add up.</details>
<details><summary>Why does backward() need a topological order?</summary>A node may only pass its gradient on after every node that uses it has added its contribution.</details>
