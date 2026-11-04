---
title: PyTorch tensors
xp: 50
---
# NumPy arrays that can learn

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

## Your quest

1. `pick_device()`: `"cuda"` if `torch.cuda.is_available()`, else `"mps"` if `torch.backends.mps.is_available()`, else `"cpu"`.
2. `linear(x, W, b)`: the layer from LLMs 1: `x @ W.T + b` (PyTorch stores `W` as `(out, in)`).
3. `to_float_tensor(arr)`: a NumPy array → a **float32** tensor.
4. `n_params(shapes)`: total number of numbers in tensors with these shapes, e.g. `[(4, 3), (4,)]` → 16. (`math.prod` helps.)

**Remember:** same habits as NumPy, plus `dtype` and `device`.

## Review

<details><summary>Why put StandardScaler inside the pipeline?</summary>So it learns its means only from training data; scaling on everything leaks test information.</details>
