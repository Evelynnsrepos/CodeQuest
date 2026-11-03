---
title: Classes, the shape of every PyTorch model
xp: 30
---
# A layer as a class

> **Warm-up:** a model has millions of weights and a recipe for using them. How would you keep the numbers and the recipe together in code?

With a **class**: a blueprint that bundles data (**attributes**) with functions that use it (**methods**). Every PyTorch model is a class, and they all look like this:

```python
class TinyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(4, 2)      # holds weights and bias

    def forward(self, x):
        return self.layer(x)              # the recipe

model = TinyModel()
y = model(x)                              # calling the object runs forward
```

- `__init__` runs once when you create the object and sets up its attributes (`self.something = …`).
- `self` is the object itself, so methods can reach its attributes.
- `__call__` is the method Python runs when you call an object like a function. PyTorch's `nn.Module` defines `__call__` to run your `forward`.
- Models are built by **nesting** objects: a transformer block holds an attention object and an MLP object; the model holds a list of blocks.

boot.dev's *Learn Object Oriented Programming* covers classes, inheritance and more; this is the part you need for PyTorch.

## Your quest

1. Write a class `Linear` with:
   - `__init__(self, weights, bias)` storing both. `weights` is a list of rows, one row per output; `bias` has one number per output.
   - `__call__(self, x)`: return a list with, for each output `j`, the dot product of `weights[j]` with `x` plus `bias[j]`.
   - `num_params(self)`: the number of weights plus the number of biases.
2. Write a class `Sequential` with `__init__(self, layers)` and `__call__(self, x)` that feeds `x` through every layer in order.

## Review

<details><summary>Which boot.dev course matches PyTorch models being classes?</summary>Learn Object Oriented Programming.</details>
<details><summary>What three kinds of math does training rest on?</summary>Linear algebra, calculus and probability.</details>
