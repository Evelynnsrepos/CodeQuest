---
title: micrograd 3: tanh, powers and ReLU
minutes: 50
xp: 50
hint: __pow__'s _backward (12 spaces): self.grad += k * self.data ** (k - 1) * out.grad
hint: tanh's _backward: self.grad += (1 - t ** 2) * out.grad
hint: relu's _backward: if self.data > 0: and under it (16 spaces) self.grad += out.grad
---
# Every operation brings its local derivative

⏱️ About 50 minutes

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

## 🔬 Take the formulas apart

Each `_backward` adds **local slope × out.grad** to `self.grad`, like last lesson. Only the local slope is new.

**Power** <div class="formula">xᵏ → slope <span class="k1">k</span> · x<span class="k2">ᵏ⁻¹</span></div>
The power rule from LLMs 4, lesson 6: bring <span class="k1">k</span> down in front, make the power <span class="k2">one smaller</span>.
- x³ at x = 2: slope 3 · 2² = 3 · 4 = **12**.
- x⁻¹ (that's 1/x) at x = 2: slope −1 · 2⁻² = −1 · ¼ = **−0.25**.

**tanh** <div class="formula">tanh(x) → slope <span class="k1">1</span> − <span class="k2">tanh(x)²</span></div>
`tanh` squashes any number into the range −1 to 1 (an S-shaped curve, like sigmoid but centered on 0). Its slope uses its own output, called `t` in the code:
- x = 0: t = 0, slope 1 − 0 = **1** (steepest).
- x = 2: t ≈ 0.964, t² ≈ 0.929, slope ≈ **0.071** (almost flat).

**ReLU** <div class="formula">relu(x) = max(0, x) → slope <span class="k1">1</span> if x > 0, else <span class="k2">0</span></div>
Below 0 the output is stuck at 0: flat, slope 0. Above 0 the output equals x: slope 1. Adding `0 · out.grad` changes nothing, so you only need the `if`.

<div class="wrong">❌ self.grad += k * self.data ** k * out.grad: forgot to make the power one smaller.</div>
<div class="right">✅ self.grad += k * self.data ** (k - 1) * out.grad</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `self.data ** (k - 1)` | "self data to the power k minus 1" | the brackets make sure the power is k − 1 |
| `t ** 2` | "t squared" | `t` is already set above `_backward` (the forward result) |
| `if self.data > 0:` | | only when the input was positive |
| `self.grad += …` | | add to the gradient, never overwrite (last lesson) |

### 👀 Worked example: a made-up operation

Say you wanted `double()`, out = 2 · x. The slope of 2x is 2, so:

```python
    def double(self):
        out = Value(2 * self.data, (self,), "double")

        def _backward():
            self.grad += 2 * out.grad
        out._backward = _backward
        return out
```

Your three are the same shape: only the number in front of `out.grad` changes.

## 🎯 Your quest

Replace each `pass` inside a `_backward` (12 spaces):

In `__pow__`: `            self.grad += k * self.data ** (k - 1) * out.grad`

In `tanh`: `            self.grad += (1 - t ** 2) * out.grad`

In `relu`:

1. `            if self.data > 0:`
2. `                self.grad += out.grad`

The check compares each one with a numerical slope (LLMs 4, lesson 6).

## Review

<details><summary>How does addition pass gradients backward? Multiplication?</summary>Addition routes out.grad unchanged to both inputs. Multiplication gives each input the other input's value times out.grad.</details>
<details><summary>Why use += when accumulating gradients?</summary>A value used in several places gets gradient from each use, and those contributions add up.</details>
<details><summary>Why does backward() need a topological order?</summary>A node may only pass its gradient on after every node that uses it has added its contribution.</details>
