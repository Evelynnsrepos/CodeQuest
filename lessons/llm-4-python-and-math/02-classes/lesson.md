---
title: Classes, the shape of every PyTorch model
minutes: 50
xp: 30
hint: Linear.__init__: self.weights = weights and self.bias = bias
hint: Linear.__call__: out = [], then for j in range(len(self.weights)): with row = self.weights[j] and total = 0
hint: Still in that loop: for i in range(len(x)): total = total + row[i] * x[i]. Then out.append(total + self.bias[j]). After it: return out
hint: num_params: count = 0, for row in self.weights: count = count + len(row), then return count + len(self.bias)
hint: Sequential: __init__ stores self.layers = layers; __call__ does for layer in self.layers: x = layer(x) and then return x
---
# A layer as a class

⏱️ About 50 minutes

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

## 🐍 Python you need

A **class** is a blueprint. Making an object from it (`layer = Linear(...)`) is like baking one cake from a recipe card.

| You write | Say it | What it does |
|---|---|---|
| `class Linear:` | "class Linear" | starts the blueprint. Everything indented under it belongs to it. |
| `def __init__(self, weights, bias):` | "init" (two underscores each side) | runs **once**, when you write `Linear(w, b)`. It sets the object up. |
| `self` | "self" | the object itself. Python fills it in for you: you write `Linear(w, b)`, not `Linear(self, w, b)`. |
| `self.weights = weights` | "self dot weights becomes weights" | stores the input **on the object**, so other methods can use it later |
| `def __call__(self, x):` | "call" | runs when you use the object like a function: `layer([2, 3])` |
| `def num_params(self):` | | an ordinary **method**: you run it with `layer.num_params()` |
| `range(len(x))` | | the positions 0, 1, … of `x` |
| `row[i] * x[i]` | | multiply the matching entries |

### 🔬 Take the formula apart: what one layer computes

<div class="formula"><span class="k1">outputⱼ</span> = <span class="k2">weightsⱼ · x</span> <span class="k3">+ biasⱼ</span></div>

- The small **ⱼ** ("sub j") means "number j". **output₀** is the first output, **output₁** the second, and so on. Python counts from 0 too.
- <span class="k2">weightsⱼ · x</span> is a **dot product**: multiply row j of the weights with `x`, entry by entry, then add everything up.
- <span class="k3">+ biasⱼ</span>: add one extra number for that output.

Numbers: weights `[[1, 0], [0, 1], [1, 1]]`, bias `[0, 0, 1]`, x = `[2, 3]`.

1. output₀ = 1×2 + 0×3 + 0 = **2**
2. output₁ = 0×2 + 1×3 + 0 = **3**
3. output₂ = 1×2 + 1×3 + 1 = **6**

So `layer1([2, 3])` is `[2, 3, 6]`. Number of parameters: 2 + 2 + 2 weights + 3 biases = **9**.

### 👀 Worked example: a class for a piggy bank

```python
class Piggy:
    def __init__(self, coins):
        self.coins = coins

    def __call__(self, extra):
        total = 0
        for c in self.coins:
            total = total + c
        return total + extra

    def count(self):
        return len(self.coins)

pig = Piggy([2, 5, 1])
print(pig(10))
print(pig.count())
```

1. `Piggy([2, 5, 1])` runs `__init__`: `self.coins` becomes `[2, 5, 1]`.
2. `pig(10)` runs `__call__` with `extra` = 10: total = 2 + 5 + 1 = 8, returns **18**.
3. `pig.count()` runs `count`: **3** coins.

`Sequential` is the "nesting" idea: it holds other objects and calls each one in turn, feeding the output of one into the next.

## 🎯 Your quest

**Part 1:** class `Linear`. Replace each `pass` / `return` with the lines below. Methods are indented 4 spaces, their bodies 8.

`__init__`:

1. `        self.weights = weights`
2. `        self.bias = bias`

`__call__` (replace `return []`):

1. `        out = []`
2. `        for j in range(len(self.weights)):`
3. `            row = self.weights[j]`
4. `            total = 0`
5. `            for i in range(len(x)):`
6. `                total = total + row[i] * x[i]`
7. `            out.append(total + self.bias[j])`
8. `        return out`

`num_params` (replace `return 0`):

1. `        count = 0`
2. `        for row in self.weights:`
3. `            count = count + len(row)`
4. `        return count + len(self.bias)`

**Part 2:** class `Sequential`.

`__init__`: `        self.layers = layers`

`__call__` (replace `return x`):

1. `        for layer in self.layers:`
2. `            x = layer(x)`
3. `        return x`

The program prints `[2, 3, 6]`, then `[11.5]` (1×2 − 1×3 + 2×6 + 0.5), then `13 parameters`.

## Review

<details><summary>Which boot.dev course matches PyTorch models being classes?</summary>Learn Object Oriented Programming.</details>
<details><summary>What three kinds of math does training rest on?</summary>Linear algebra, calculus and probability.</details>
