import torch
from sklearn.datasets import make_moons


class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x


def train(model, X, y, epochs=200, lr=0.01, batch=64):
    return model


def accuracy(model, X, y):
    return 0.0


Xn, yn = make_moons(600, noise=0.15, random_state=0)
X, y = torch.tensor(Xn, dtype=torch.float32), torch.tensor(yn, dtype=torch.float32).unsqueeze(1)
model = train(Net(), X[:500], y[:500])
print("held-out accuracy:", accuracy(model, X[500:], y[500:]))
