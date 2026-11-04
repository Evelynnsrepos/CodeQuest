import torch
from sklearn.datasets import make_moons
Net, tr, acc = ns.get("Net"), ns.get("train"), ns.get("accuracy")
assert Net and tr and acc, "Keep Net, train and accuracy."
torch.manual_seed(0)
net = Net()
n = sum(p.numel() for p in net.parameters())
assert n == 2 * 32 + 32 + 32 * 32 + 32 + 32 + 1, f"Net should be 2 → 32 → 32 → 1: 1185 parameters, got {n}."
assert any(isinstance(m, torch.nn.ReLU) for m in net.modules()), "Put ReLUs between the layers."
Xn, yn = make_moons(800, noise=0.15, random_state=3)
X, y = torch.tensor(Xn, dtype=torch.float32), torch.tensor(yn, dtype=torch.float32).unsqueeze(1)
model = tr(net, X[:600], y[:600])
a = acc(model, X[600:], y[600:])
assert 0.95 <= a <= 1.0, f"Held-out accuracy should be at least 0.95, got {a:.3f}."
