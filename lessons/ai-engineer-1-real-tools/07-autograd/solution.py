import torch


def derivative(f, x):
    t = torch.tensor(float(x), requires_grad=True)
    f(t).backward()
    return t.grad.item()


def mse_grads(w, b, xs, ys):
    w = torch.tensor(float(w), requires_grad=True)
    b = torch.tensor(float(b), requires_grad=True)
    x, y = torch.tensor(xs, dtype=torch.float32), torch.tensor(ys, dtype=torch.float32)
    loss = ((w * x + b - y) ** 2).mean()
    loss.backward()
    return (w.grad.item(), b.grad.item())


print(derivative(lambda t: t ** 3, 2.0), derivative(torch.sigmoid, 0.0))
print(mse_grads(1.0, 0.0, [1, 2, 3], [2, 4, 6]))
