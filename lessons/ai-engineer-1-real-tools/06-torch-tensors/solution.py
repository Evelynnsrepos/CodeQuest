import math
import numpy as np
import torch


def pick_device():
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def linear(x, W, b):
    return x @ W.T + b


def to_float_tensor(arr):
    return torch.from_numpy(arr).float()


def n_params(shapes):
    return sum(math.prod(s) for s in shapes)


x = torch.tensor([[1.0, 2.0, 3.0]])
W = torch.ones(2, 3)
b = torch.tensor([0.5, -0.5])
print(pick_device(), linear(x, W, b), to_float_tensor(np.arange(3)).dtype, n_params([(4, 3), (4,)]))
