---
title: Your first nn.Module
xp: 65
---
# A network that bends

> **Warm-up:** why can't a straight line separate two interleaving half-moons?

A real model is a **class** that inherits from `nn.Module`. You create the layers in `__init__` and say how data flows in `forward`:

```python
class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = torch.nn.Sequential(
            torch.nn.Linear(2, 32), torch.nn.ReLU(),
            torch.nn.Linear(32, 32), torch.nn.ReLU(),
            torch.nn.Linear(32, 1),             # one number: the logit
        )
    def forward(self, x):
        return self.layers(x)
```

The **ReLU**s between the layers are what lets it bend; without them, stacked linear layers collapse into one straight line (Math 2).

For yes/no classification the last layer outputs a **logit** (any number), and the loss is `BCEWithLogitsLoss`: sigmoid and cross-entropy in one, numerically stable (Math 5 lesson 06). To predict, `logit > 0` means class 1.

**Mini-batches:** instead of all data at once, shuffle and take 64 examples per step. Noisier steps, but many more of them per second, and it's how every big model trains.

## Your quest

1. `Net`: the class above (2 → 32 → 32 → 1 with ReLUs).
2. `train(model, X, y, epochs=200, lr=0.01, batch=64)`: seed 0, AdamW, `BCEWithLogitsLoss`, mini-batches from `torch.randperm(len(X))` each epoch. Return the model.
3. `accuracy(model, X, y)`: share of correct predictions, computed under `torch.no_grad()`.

The check trains on scikit-learn's `make_moons` and wants ≥ 95% on held-out points.

**Remember:** layers in `__init__`, flow in `forward`, nonlinearity in between.

## Review

<details><summary>Name the five lines of a training step.</summary>zero_grad, forward, loss, backward, step.</details>
