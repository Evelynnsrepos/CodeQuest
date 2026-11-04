---
title: micrograd 1: numbers that remember
xp: 40
---
# Building a computation graph

> **Warm-up:** to apply the chain rule automatically, what does a program need to remember about how a result was computed?

Which values went in, and which operation combined them. In the next lessons you build **micrograd**, Andrej Karpathy's tiny autograd engine (~100 lines) that does exactly what PyTorch's `autograd` does, just one number at a time. Follow his video *"The spelled-out intro to neural networks and backpropagation: building micrograd"* alongside; it's the first lecture of *Neural Networks: Zero to Hero*.

The idea: wrap every number in a `Value` object. When you combine Values, the result records its **children** (the inputs) and the **operation**. Do a whole calculation and you've built a **computation graph**:

```
a = Value(2)   b = Value(-3)   c = Value(10)
d = a * b + c

     a ─┐
        ├─(*)─ e=-6 ─┐
     b ─┘            ├─(+)─ d=4
     c ──────────────┘
```

Python lets a class define what `+` and `*` mean through the special methods `__add__(self, other)` and `__mul__(self, other)`. `a + b` calls `a.__add__(b)`. (`__radd__` handles `1 + a`, where the left side isn't a Value.)

## Your quest

Finish `__add__` and `__mul__`. Each returns a **new** `Value` whose:

- `data` is the sum (or product) of `self.data` and `other.data`,
- children are `(self, other)`,
- operation is `"+"` (or `"*"`).

Look at `__init__` to see the order of the arguments. The line that wraps `other` is already there, so `v + 1` works too.

## Review

<details><summary>Name the five steps of the training loop.</summary>Forward pass, loss, backward pass (gradients), update (w −= lr · grad), repeat.</details>
<details><summary>What is mean squared error?</summary>The average of (prediction − target)² over the examples.</details>
