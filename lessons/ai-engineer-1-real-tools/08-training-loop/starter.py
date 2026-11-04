import torch


def fit_line(xs, ys, steps=500, lr=0.05):
    return (0.0, 0.0, 0.0)


g = torch.Generator().manual_seed(1)
xs = torch.linspace(-2, 2, 50)
ys = 2 * xs + 1 + 0.1 * torch.randn(50, generator=g)
print(fit_line(xs.tolist(), ys.tolist()))
