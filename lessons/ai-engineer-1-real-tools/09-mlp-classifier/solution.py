import torch
from sklearn.datasets import make_moons


class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = torch.nn.Sequential(
            torch.nn.Linear(2, 32), torch.nn.ReLU(),
            torch.nn.Linear(32, 32), torch.nn.ReLU(),
            torch.nn.Linear(32, 1),
        )

    def forward(self, x):
        return self.layers(x)


def train(model, X, y, epochs=200, lr=0.01, batch=64):
    torch.manual_seed(0)
    opt = torch.optim.AdamW(model.parameters(), lr=lr)
    loss_fn = torch.nn.BCEWithLogitsLoss()
    for _ in range(epochs):
        order = torch.randperm(len(X))
        for i in range(0, len(X), batch):
            idx = order[i:i + batch]
            opt.zero_grad()
            loss = loss_fn(model(X[idx]), y[idx])
            loss.backward()
            opt.step()
    return model


def accuracy(model, X, y):
    with torch.no_grad():
        return ((model(X) > 0).float() == y).float().mean().item()


Xn, yn = make_moons(600, noise=0.15, random_state=0)
X, y = torch.tensor(Xn, dtype=torch.float32), torch.tensor(yn, dtype=torch.float32).unsqueeze(1)
model = train(Net(), X[:500], y[:500])
print("held-out accuracy:", accuracy(model, X[500:], y[500:]))
