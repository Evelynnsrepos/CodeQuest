---
title: The five-line training loop
xp: 60
---
# zero_grad, forward, loss, backward, step

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

## Your quest

`fit_line(xs, ys, steps=500, lr=0.05)`: seed with 0, train `nn.Linear(1, 1)` with SGD and MSE on the data, and return `(w, b, final_loss)` as Python floats (`model.weight.item()`, `model.bias.item()`).

The data `y = 2x + 1` plus noise should give w ≈ 2, b ≈ 1.

**Remember:** zero_grad, forward, loss, backward, step.

## Review

<details><summary>Why call zero_grad every step?</summary>backward() adds to .grad; without zeroing, old gradients pile up.</details>
