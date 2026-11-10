---
title: PyTorch tensors
minutes: 30
xp: 50
hint: pick_device: if torch.cuda.is_available(): return "cuda", then the same for torch.backends.mps.is_available() and "mps", else return "cpu"
hint: linear: return x @ W.T + b
hint: to_float_tensor: return torch.from_numpy(arr).float()
hint: n_params: total = 0, then for shape in shapes: total = total + math.prod(shape)
---
# NumPy arrays that can learn

⏱️ About 30 minutes

> **Warm-up:** what two things does a neural network library need that NumPy doesn't have?

(Answer: running on a **GPU**, and computing **gradients** automatically.)

A PyTorch **tensor** is a NumPy-style array with those two extras. Most NumPy habits carry over:

```python
import torch
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
x.shape, x.dtype          # torch.Size([2, 2]), torch.float32
x @ x.T                   # matrix multiply
x.mean(dim=0)             # PyTorch says dim where NumPy says axis
torch.from_numpy(arr)     # share memory with a NumPy array
t.numpy()                 # and back (CPU tensors only)
t.item()                  # a 1-element tensor → a Python number
```

**dtype:** models use `float32` (or smaller: `bfloat16`, see Math 5 lesson 12). NumPy defaults to `float64`, so `torch.from_numpy` gives float64. Convert with `.float()`.

**device:** where the tensor lives. `"cpu"`, `"cuda"` (NVIDIA, and AMD with ROCm builds) or `"mps"` (Apple). Every tensor in one calculation must be on the same device: `t.to(device)`.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `torch.cuda.is_available()` | | `True` if there's a usable GPU (NVIDIA, or AMD with a ROCm build) |
| `torch.backends.mps.is_available()` | | `True` on an Apple chip |
| `x @ W.T + b` | | the linear layer: x times W transposed, plus the bias |
| `torch.from_numpy(arr)` | | a tensor that shares the array's numbers |
| `.float()` | | converts to float32 |
| `math.prod((4, 3))` | "the product of 4 and 3" | multiplies all the numbers: 12. `math.prod((4,))` is 4. |

### 👀 Worked example: counting numbers in tensors

Shapes `[(4, 3), (4,)]`:

1. `(4, 3)` is a 4 × 3 table: 4 · 3 = **12** numbers (the weights).
2. `(4,)` is a list of 4: **4** numbers (the biases). The comma makes it a tuple with one item.
3. Total: 12 + 4 = **16**.

And `linear` with x = [[1, 2, 3]], W = all ones of shape (2, 3), b = [0.5, −0.5]: each output is 1 + 2 + 3 = 6, plus its bias: **[[6.5, 5.5]]**.

## 🎯 Your quest

1. `pick_device()`: `"cuda"` if `torch.cuda.is_available()`, else `"mps"` if `torch.backends.mps.is_available()`, else `"cpu"`.
2. `linear(x, W, b)`: the layer from LLMs 1: `x @ W.T + b` (PyTorch stores `W` as `(out, in)`).
3. `to_float_tensor(arr)`: a NumPy array → a **float32** tensor.
4. `n_params(shapes)`: total number of numbers in tensors with these shapes, e.g. `[(4, 3), (4,)]` → 16. (`math.prod` helps.)

**Part 1:** `pick_device`. Replace `return ""` with:

1. `if torch.cuda.is_available():`
2. `    return "cuda"`
3. `if torch.backends.mps.is_available():`
4. `    return "mps"`
5. `return "cpu"`

**Part 2:** `linear`. Replace `return x` with:

1. `return x @ W.T + b`

**Part 3:** `to_float_tensor`. Replace `return arr` with:

1. `return torch.from_numpy(arr).float()`

**Part 4:** `n_params`. Replace `return 0` with:

1. `total = 0`
2. `for shape in shapes:`
3. `    total = total + math.prod(shape)`
4. `return total`

**Remember:** same habits as NumPy, plus `dtype` and `device`.

## Review

<details><summary>Why put StandardScaler inside the pipeline?</summary>So it learns its means only from training data; scaling on everything leaks test information.</details>
