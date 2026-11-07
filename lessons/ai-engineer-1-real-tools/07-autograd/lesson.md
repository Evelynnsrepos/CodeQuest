---
title: Autograd: gradients for free
minutes: 35
xp: 55
hint: derivative: t = torch.tensor(float(x), requires_grad=True), then f(t).backward(), then return t.grad.item()
hint: mse_grads: make w and b tensors with requires_grad=True, and x, y tensors from the lists with dtype=torch.float32
hint: mse_grads: loss = ((w * x + b - y) ** 2).mean(), loss.backward(), return (w.grad.item(), b.grad.item())
---
# backward() does Math 3 for you

⏱️ About 35 minutes

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

## 🔬 Check the answer by hand

**derivative(t³ at 2)**: the power rule (Math 3) says the derivative of t³ is 3·t². At t = 2: 3 · 2² = 3 · 4 = **12**. Your function should print 12.0.

**derivative(sigmoid at 0)**: the sigmoid's derivative is σ(t) · (1 − σ(t)). σ(0) = 0.5, so 0.5 · 0.5 = **0.25**.

**mse_grads** for w = 1, b = 0, x = (1, 2, 3), y = (2, 4, 6):

1. The predictions w·x + b: 1, 2, 3. The misses (pred − y): −1, −2, −3.
2. dL/dw = the mean of 2 · miss · x = (2·(−1)·1 + 2·(−2)·2 + 2·(−3)·3) / 3 = (−2 − 8 − 18) / 3 = **−9.33**.
3. dL/db = the mean of 2 · miss = (−2 − 4 − 6) / 3 = **−4**.

Negative means "make w and b bigger to lower the loss", which is right: the real line is y = 2x.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `torch.tensor(float(x), requires_grad=True)` | | a one-number tensor that PyTorch will record. `float(...)` makes sure it's a decimal number, since gradients need decimals. |
| `f(t)` | | calls the function you were given on the tensor |
| `.backward()` | | runs the chain rule and fills `.grad` |
| `t.grad.item()` | | the gradient as a plain Python number |
| `torch.tensor(xs, dtype=torch.float32)` | | a list → a tensor of decimals |
| `((w * x + b - y) ** 2).mean()` | | the MSE: misses squared, then averaged, all in one line |

The starter defines `cube(t)` for the example at the bottom, so you can see `derivative` takes a **function** as its input.

## 🎯 Your quest

1. `derivative(f, x)`: the derivative of a function `f` (which uses torch operations) at the number `x`, as a Python float.
2. `mse_grads(w, b, xs, ys)`: for the model `pred = w·x + b` and loss = mean of `(pred − y)²`, return `(dL/dw, dL/db)` as floats, using autograd. Compare with your hand-made `grad_mse` from Math 3 lesson 09.

**Part 1:** `derivative`. Replace `return 0.0` with:

1. `t = torch.tensor(float(x), requires_grad=True)`
2. `f(t).backward()`
3. `return t.grad.item()`

**Part 2:** `mse_grads`. Replace `return (0.0, 0.0)` with:

1. `w = torch.tensor(float(w), requires_grad=True)`
2. `b = torch.tensor(float(b), requires_grad=True)`
3. `x = torch.tensor(xs, dtype=torch.float32)`
4. `y = torch.tensor(ys, dtype=torch.float32)`
5. `loss = ((w * x + b - y) ** 2).mean()`
6. `loss.backward()`
7. `return (w.grad.item(), b.grad.item())`

**Remember:** loss.backward() fills .grad; zero it every step.

## Review

<details><summary>What does PyTorch call NumPy's axis?</summary>dim.</details>
