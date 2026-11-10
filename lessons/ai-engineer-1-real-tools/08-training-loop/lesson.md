---
title: The five-line training loop
minutes: 35
xp: 60
hint: Setup: torch.manual_seed(0), then X and y as float32 tensors with .unsqueeze(1), then model, opt and loss_fn as in the example above
hint: The loop: for step in range(steps): opt.zero_grad(), pred = model(X), loss = loss_fn(pred, y), loss.backward(), opt.step()
hint: After the loop: return (model.weight.item(), model.bias.item(), loss.item())
---
# zero_grad, forward, loss, backward, step

⏱️ About 35 minutes

> **Warm-up:** write down, from memory, the steps of gradient descent from Math 3 lesson 10.

Every PyTorch training loop, from a line fit to a 70B LLM, has the same core:

```python
model = torch.nn.Linear(1, 1)                       # w and b, randomly initialized
opt = torch.optim.SGD(model.parameters(), lr=0.05)  # or AdamW (Math 5 lesson 10)
loss_fn = torch.nn.MSELoss()
for step in range(500):
    opt.zero_grad()              # 1. forget last step's gradients
    pred = model(X)              # 2. forward
    loss = loss_fn(pred, y)      # 3. how wrong?
    loss.backward()              # 4. gradients for every parameter
    opt.step()                   # 5. w -= lr · grad (or Adam's version)
```

Shapes: `nn.Linear(1, 1)` wants inputs of shape `(n, 1)`: n examples, 1 feature. A plain list of numbers has shape `(n,)`; `.unsqueeze(1)` or `.view(-1, 1)` adds the column.

**Seeds:** `torch.manual_seed(0)` makes the random initialization the same every run, so results are reproducible (the same reason you seeded the shuffle in LLMs 7).

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `torch.manual_seed(0)` | | fixes the random starting weights, so every run gives the same result |
| `torch.tensor(xs, dtype=torch.float32)` | | the list of numbers as a tensor, shape `(n,)` |
| `.unsqueeze(1)` | "unsqueeze at 1" | adds a column axis: shape `(n,)` → `(n, 1)`. `[1, 2, 3]` becomes `[[1], [2], [3]]`. |
| `torch.nn.Linear(1, 1)` | | one input, one output: just a w and a b |
| `torch.optim.SGD(model.parameters(), lr=lr)` | | the optimizer that will change w and b |
| `model.weight.item()` | | w as a plain number (same for `model.bias`) |

### 👀 What one step does

Say the model starts at w = 0.5, b = 0 and one point is x = 1, y = 3. The prediction is 0.5, the loss is (0.5 − 3)² = 6.25. `backward()` finds that a bigger w and b would lower it, and `opt.step()` moves them a little (by lr times the gradient). After 500 such steps on all 50 points, w is close to 2 and b close to 1.

## 🎯 Your quest

`fit_line(xs, ys, steps=500, lr=0.05)`: seed with 0, train `nn.Linear(1, 1)` with SGD and MSE on the data, and return `(w, b, final_loss)` as Python floats (`model.weight.item()`, `model.bias.item()`).

The data `y = 2x + 1` plus noise should give w ≈ 2, b ≈ 1.

Replace `return (0.0, 0.0, 0.0)` with:

1. `torch.manual_seed(0)`
2. `X = torch.tensor(xs, dtype=torch.float32).unsqueeze(1)`
3. `y = torch.tensor(ys, dtype=torch.float32).unsqueeze(1)`
4. `model = torch.nn.Linear(1, 1)`
5. `opt = torch.optim.SGD(model.parameters(), lr=lr)`
6. `loss_fn = torch.nn.MSELoss()`
7. `for step in range(steps):`
8. `    opt.zero_grad()`
9. `    pred = model(X)`
10. `    loss = loss_fn(pred, y)`
11. `    loss.backward()`
12. `    opt.step()`
13. `return (model.weight.item(), model.bias.item(), loss.item())`

Lines 8 to 12 are the five steps from the title, in order.

**Remember:** zero_grad, forward, loss, backward, step.

## Review

<details><summary>Why call zero_grad every step?</summary>backward() adds to .grad; without zeroing, old gradients pile up.</details>
