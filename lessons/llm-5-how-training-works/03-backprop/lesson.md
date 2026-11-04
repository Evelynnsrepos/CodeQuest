---
title: micrograd 2: backpropagation
xp: 60
---
# Running the chain rule backwards

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

## Your quest

1. Fill in `_backward` in `__add__` and `__mul__` using the rules above (use `+=`).
2. Write `backward()`:
   - a nested function `visit(v)` that, if `v` isn't in `seen`, adds it to `seen`, calls `visit` on each child in `v._prev`, then appends `v` to `order`;
   - call `visit(self)`, set `self.grad = 1.0`, then call `v._backward()` for every `v` in `reversed(order)`.

Your output should match the worked example.

## Review

<details><summary>What does a Value remember about how it was made?</summary>Its children (the input Values) and the operation that combined them.</details>
<details><summary>Which Python method runs for a + b?</summary>a.__add__(b) (and b.__radd__(a) if a doesn't know how).</details>
