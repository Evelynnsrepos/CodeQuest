---
title: Autograd: gradients for free
xp: 55
---
# backward() does Math 3 for you

> **Warm-up:** in Math 3 lesson 11 you did backprop by hand. What was the most error-prone part?

PyTorch records every operation on tensors that have `requires_grad=True`. Calling `.backward()` on a single number (the loss) runs the chain rule backward through that record and stores **∂loss/∂tensor** in each tensor's `.grad`.

```python
w = torch.tensor(3.0, requires_grad=True)
loss = (2 * w - 4) ** 2      # PyTorch remembers: multiply, subtract, square
loss.backward()
w.grad                       # tensor(8.)  = 2·(2w − 4)·2 at w = 3
```

Three rules that bite everyone:

1. **Gradients add up.** A second `backward()` **adds** to `.grad`. Training loops call `optimizer.zero_grad()` (or `w.grad = None`) every step.
2. `backward()` needs a **single number**. For a vector, reduce first (`.sum()`, `.mean()`).
3. Use `with torch.no_grad():` when you change weights by hand or just predict, so PyTorch doesn't record it.

## Your quest

1. `derivative(f, x)`: the derivative of a function `f` (which uses torch operations) at the number `x`, as a Python float.
2. `mse_grads(w, b, xs, ys)`: for the model `pred = w·x + b` and loss = mean of `(pred − y)²`, return `(dL/dw, dL/db)` as floats, using autograd. Compare with your hand-made `grad_mse` from Math 3 lesson 09.

**Remember:** loss.backward() fills .grad; zero it every step.

## Review

<details><summary>What does PyTorch call NumPy's axis?</summary>dim.</details>
