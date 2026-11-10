---
title: micrograd 2: backpropagation
minutes: 70
xp: 60
hint: __add__'s _backward (12 spaces): self.grad += out.grad and other.grad += out.grad
hint: __mul__'s _backward: self.grad += other.data * out.grad and other.grad += self.data * out.grad
hint: backward: def visit(v): with if v not in seen: seen.add(v), for child in v._prev: visit(child), then order.append(v)
hint: After visit (8 spaces): visit(self), self.grad = 1.0, then for v in reversed(order): v._backward()
---
# Running the chain rule backwards

⏱️ About 70 minutes

> **Warm-up:** in `L = (a·b + c)²`, if you nudge `a` a tiny bit, how much does `L` move? Which intermediate results do you need to answer that?

Every node gets a `.grad`: **how much the final output changes per unit change of this node**, `∂L/∂node`. Backpropagation fills them in from the output back to the inputs:

1. The output's own gradient is 1 (`∂L/∂L = 1`).
2. Each node passes its gradient to its children, multiplied by the **local derivative** of its operation (the chain rule).

For the two operations so far, with `out` the result:

```
out = self + other:   self.grad  += 1 · out.grad          other.grad += 1 · out.grad
out = self * other:   self.grad  += other.data · out.grad  other.grad += self.data · out.grad
```

Addition **routes** the gradient unchanged to both inputs. Multiplication **swaps**: each input gets the other's value times the gradient.

Why `+=` and not `=`? A value used twice (like `d` in `d * d`) receives gradient from both uses, and they must add up. That's the multivariable chain rule.

Each operation stores a little function `_backward` that does its step. `backward()` on the final output must call them in the right order: a node may only pass its gradient on once **everything that uses it** has finished. A **topological sort** gives that order: visit children before parents, then walk the list in reverse.

```
L = d·d, d = e + c, e = a·b, a=2, b=−3, c=10
L.grad = 1
d.grad = 2·d = 8             (d used twice: 4 + 4)
e.grad = c.grad = 8          (+ routes)
a.grad = b·8 = −24,  b.grad = a·8 = 16     (* swaps)
```

## 🔬 Take the rules apart

`out.grad` means ∂L/∂out: "if `out` goes up by a tiny bit, how much does the final L go up?" Each node passes that on to its children with the chain rule: **local slope × out.grad**.

**Addition**, out = a + b. If a goes up by 1, out goes up by 1. Local slope 1, for both:
<div class="formula">a.grad <span class="k1">+=</span> <span class="k2">1</span> · out.grad &nbsp;&nbsp; b.grad <span class="k1">+=</span> <span class="k2">1</span> · out.grad</div>

**Multiplication**, out = a · b. If a goes up by 1, out goes up by **b** (like 3 · 5 → 4 · 5 grows by 5). So the local slope of a is b, and of b is a. They **swap**:
<div class="formula">a.grad <span class="k1">+=</span> <span class="k3">b.data</span> · out.grad &nbsp;&nbsp; b.grad <span class="k1">+=</span> <span class="k3">a.data</span> · out.grad</div>

**Why <span class="k1">+=</span>** ("add to")? In `x * x + x`, x is used three times. Each use adds its share: 3 + 3 + 1 = 7, which is the slope of x² + x at x = 3 (2·3 + 1). With `=` the last use would overwrite the others.

Follow the example from the top with a = 2, b = −3, c = 10: e = a·b = −6, d = e + c = 4, L = d·d = 16.

1. L.grad = **1** (start).
2. L = d · d: both "children" are d. Each gets other.data × 1 = 4. d.grad = 4 + 4 = **8**.
3. d = e + c: addition routes. e.grad = **8**, c.grad = **8**.
4. e = a · b: multiplication swaps. a.grad = b × 8 = −3 × 8 = **−24**. b.grad = a × 8 = 2 × 8 = **16**.

**The order.** Step 3 needs d.grad finished first. A **topological order** lists every node after all its children: a, b, e, c, d, L. Walking it **backwards** (L, d, c, e, b, a) means a node is only handled after everything that uses it.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `self.grad += out.grad` | "self grad plus-equals out grad" | short for `self.grad = self.grad + out.grad` |
| `def _backward():` inside `__add__` | | a function made **inside** another function. It **remembers** `self`, `other` and `out` from where it was made. |
| `out._backward = _backward` | (given) | stores that function on `out`, to run later |
| `def visit(v):` inside `backward` | | the same trick: `visit` can use `order` and `seen` |
| `visit(child)` inside `visit` | | a function calling **itself**. It goes down to the children first, then comes back. |
| `seen.add(v)` | | remember "done with v", so a node used twice is only listed once |
| `reversed(order)` | | the list from last to first |
| `v._backward()` | | runs that node's stored function |

### 👀 Worked example: visit, step by step

For e = a · b, d = e + c, `visit(d)` does this:

1. `visit(d)`: not seen → mark it. Its children are e and c. Call `visit(e)`.
2. `visit(e)`: mark it. Children a and b. `visit(a)`: no children → `order` = [a]. `visit(b)` → [a, b]. Back in e: append e → **[a, b, e]**.
3. Back in d: next child, `visit(c)` → [a, b, e, c]. Then append d → **[a, b, e, c, d]**.

Reversed: d, c, e, b, a. Every node comes before its children. (The children are stored in a set, so a and b may swap places. That's fine.)

## 🎯 Your quest

**Part 1:** in `__add__`, replace `pass` inside `_backward` with (12 spaces):

1. `            self.grad += out.grad`
2. `            other.grad += out.grad`

In `__mul__`, replace `pass` with:

1. `            self.grad += other.data * out.grad`
2. `            other.grad += self.data * out.grad`

**Part 2:** `backward`. Below `order, seen = [], set()`, add (8 spaces in):

1. `        def visit(v):`
2. `            if v not in seen:`
3. `                seen.add(v)`
4. `                for child in v._prev:`
5. `                    visit(child)`
6. `                order.append(v)`
7. `        visit(self)`
8. `        self.grad = 1.0`
9. `        for v in reversed(order):`
10. `            v._backward()`

The output should show a.grad −24, b.grad 16, c.grad 8, the same as the worked numbers above.

## Review

<details><summary>What does a Value remember about how it was made?</summary>Its children (the input Values) and the operation that combined them.</details>
<details><summary>Which Python method runs for a + b?</summary>a.__add__(b) (and b.__radd__(a) if a doesn't know how).</details>
