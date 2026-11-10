---
title: micrograd 1: numbers that remember
minutes: 40
xp: 40
hint: __add__: return Value(self.data + other.data, (self, other), "+")
hint: __mul__: the same with * : return Value(self.data * other.data, (self, other), "*")
hint: The order in Value(...) is: data first, then the children (self, other), then the operation as text
---
# Building a computation graph

⏱️ About 40 minutes

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

## 🐍 Python you need

Read `__init__` first. A `Value(data, _children, _op)` stores:

- `self.data`: the number itself,
- `self.grad`: its gradient, 0 for now (next lesson),
- `self._prev`: the children, the Values it was made from,
- `self._op`: the operation as text, like `"+"`,
- `self._backward`: a function for the next lesson. It starts as `do_nothing`.

| You write | Say it | What it does |
|---|---|---|
| `def __add__(self, other):` | "dunder add" | Python runs it for `a + b`, with `self` = a and `other` = b |
| `def __mul__(self, other):` | "dunder mul" | the same for `a * b` |
| `isinstance(other, Value)` | | true if `other` is already a `Value`. If not (like the plain `1` in `v + 1`), the given line wraps it. |
| `self.data + other.data` | | the plain numbers inside, added |
| `(self, other)` | | a **tuple**: two things in brackets, kept together |
| `Value(..., (self, other), "+")` | | a brand-new Value: the number, where it came from, how |

### 👀 Worked example: a "Box" that remembers

```python
class Box:
    def __init__(self, n, parts=(), how=""):
        self.n = n
        self.parts = parts
        self.how = how

    def __add__(self, other):
        return Box(self.n + other.n, (self, other), "+")

x = Box(2)
y = Box(5)
z = x + y            # Python runs x.__add__(y)
print(z.n, z.how)    # 7 +
```

1. `x + y` calls `__add__` with `self` = x and `other` = y.
2. It makes a **new** Box with n = 2 + 5 = 7, parts = (x, y), how = "+".
3. `x` and `y` don't change. `z` remembers both.

Your `Value` works the same way, so `a * b + c` builds the graph from the picture above all by itself.

## 🎯 Your quest

Below the given `other = Value(other)` lines, replace `return None`:

In `__add__`: `        return Value(self.data + other.data, (self, other), "+")`

In `__mul__`: `        return Value(self.data * other.data, (self, other), "*")`

It prints `Value(data=4.0000, grad=0.0000)` and `made by: + from [-6.0, 10.0]`: d came from adding e = −6 and c = 10.

## Review

<details><summary>Name the five steps of the training loop.</summary>Forward pass, loss, backward pass (gradients), update (w −= lr · grad), repeat.</details>
<details><summary>What is mean squared error?</summary>The average of (prediction − target)² over the examples.</details>
