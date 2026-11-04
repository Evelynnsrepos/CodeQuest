import torch


def derivative(f, x):
    return 0.0


def mse_grads(w, b, xs, ys):
    return (0.0, 0.0)


print(derivative(lambda t: t ** 3, 2.0), derivative(torch.sigmoid, 0.0))
print(mse_grads(1.0, 0.0, [1, 2, 3], [2, 4, 6]))
