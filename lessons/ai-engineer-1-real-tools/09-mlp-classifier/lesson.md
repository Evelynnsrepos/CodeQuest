---
title: Your first nn.Module
minutes: 50
xp: 65
hint: Net: in __init__, after super().__init__(), type the self.layers = torch.nn.Sequential(...) lines. forward: return self.layers(x)
hint: train: torch.manual_seed(0), opt = torch.optim.AdamW(...), loss_fn = torch.nn.BCEWithLogitsLoss(), then for epoch in range(epochs):
hint: Inside each epoch: order = torch.randperm(len(X)), then for i in range(0, len(X), batch): idx = order[i:i + batch] and the five training steps on X[idx], y[idx]
hint: accuracy: with torch.no_grad(): guesses = (model(X) > 0).float(), right = (guesses == y).float(), return right.mean().item()
---
# A network that bends

⏱️ About 50 minutes

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

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `class Net(torch.nn.Module):` | | a new kind of object that is a PyTorch model (LLMs 4, lesson 02 explains classes) |
| `super().__init__()` | | runs PyTorch's own setup first (given) |
| `self.layers = ...` | | stores the layers on the object, so PyTorch finds their weights |
| `torch.nn.Sequential(a, b, c)` | | runs a, then b, then c |
| `torch.randperm(500)` | "random permutation" | the numbers 0 to 499 in a random order: a shuffle |
| `range(0, len(X), batch)` | | 0, 64, 128, ...: where each mini-batch starts |
| `order[i:i + batch]` | | the next 64 shuffled positions |
| `X[idx]` | | the rows at those positions |
| `with torch.no_grad():` | | don't record anything for gradients (we only predict) |
| `(model(X) > 0)` | | True where the logit is positive, which means "class 1" |
| `.float()` | | True → 1.0, False → 0.0 |
| `(guesses == y).float().mean()` | | 1.0 for each right answer, then the average: the share that was right |

### 👀 Worked example: accuracy by hand

Logits (2.1, −0.3, 0.4) and labels (1, 0, 0):

1. `> 0`: (True, False, True) → `.float()` → (1, 0, 1).
2. Compare with the labels (1, 0, 0): (True, True, False) → (1, 1, 0).
3. The mean: 2 / 3 = **0.667**.

## 🎯 Your quest

1. `Net`: the class above (2 → 32 → 32 → 1 with ReLUs).
2. `train(model, X, y, epochs=200, lr=0.01, batch=64)`: seed 0, AdamW, `BCEWithLogitsLoss`, mini-batches from `torch.randperm(len(X))` each epoch. Return the model.
3. `accuracy(model, X, y)`: share of correct predictions, computed under `torch.no_grad()`.

The check trains on scikit-learn's `make_moons` and wants ≥ 95% on held-out points.

**Part 1:** `Net`. In `__init__`, under `super().__init__()`, type:

1. `self.layers = torch.nn.Sequential(`
2. `    torch.nn.Linear(2, 32),`
3. `    torch.nn.ReLU(),`
4. `    torch.nn.Linear(32, 32),`
5. `    torch.nn.ReLU(),`
6. `    torch.nn.Linear(32, 1),`
7. `)`

These lines are inside a method of a class, so they start with 8 spaces (12 for lines 2 to 6). In `forward`, replace `return x` with:

1. `return self.layers(x)`

**Part 2:** `train`. Replace `return model` with:

1. `torch.manual_seed(0)`
2. `opt = torch.optim.AdamW(model.parameters(), lr=lr)`
3. `loss_fn = torch.nn.BCEWithLogitsLoss()`
4. `for epoch in range(epochs):`
5. `    order = torch.randperm(len(X))`
6. `    for i in range(0, len(X), batch):`
7. `        idx = order[i:i + batch]`
8. `        opt.zero_grad()`
9. `        loss = loss_fn(model(X[idx]), y[idx])`
10. `        loss.backward()`
11. `        opt.step()`
12. `return model`

**Part 3:** `accuracy`. Replace `return 0.0` with:

1. `with torch.no_grad():`
2. `    guesses = (model(X) > 0).float()`
3. `    right = (guesses == y).float()`
4. `    return right.mean().item()`

**Remember:** layers in `__init__`, flow in `forward`, nonlinearity in between.

## Review

<details><summary>Name the five lines of a training step.</summary>zero_grad, forward, loss, backward, step.</details>
