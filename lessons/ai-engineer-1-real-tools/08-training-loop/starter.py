import torch


def fit_line(xs, ys, steps=500, lr=0.05):
    # torch.manual_seed(0)
    # X = torch.tensor(xs, dtype=torch.float32).unsqueeze(1)
    # y = torch.tensor(ys, dtype=torch.float32).unsqueeze(1)
    # model = torch.nn.Linear(1, 1)
    # opt = torch.optim.SGD(model.parameters(), lr=lr)
    # loss_fn = torch.nn.MSELoss()
    # for step in range(steps):
    #     opt.zero_grad()
    #     pred = model(X)
    #     loss = loss_fn(pred, y)
    #     loss.backward()
    #     opt.step()
    # return (model.weight.item(), model.bias.item(), loss.item())
    return (0.0, 0.0, 0.0)


g = torch.Generator().manual_seed(1)
xs = torch.linspace(-2, 2, 50)
ys = 2 * xs + 1 + 0.1 * torch.randn(50, generator=g)
print(fit_line(xs.tolist(), ys.tolist()))
