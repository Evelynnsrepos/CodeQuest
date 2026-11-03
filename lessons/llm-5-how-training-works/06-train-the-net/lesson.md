---
title: Training your neural network
xp: 50
---
# Watch the loss go down

> **Warm-up:** you have a model, data and gradients. Write the training loop from memory, as five steps, before reading on.

Here it is with micrograd:

```python
for step in range(steps):
    predictions = [model(x)[0] for x in xs]                       # 1. forward
    loss = sum((p - y) ** 2 for p, y in zip(predictions, ys))     # 2. loss
    for p in model.parameters(): p.grad = 0.0                     # 3a. zero the grads
    loss.backward()                                               # 3b. backward
    for p in model.parameters(): p.data -= lr * p.grad            # 4. update
```

The one step people forget is **zeroing the gradients**. `backward()` *adds* to `.grad` (that's what `+=` does), so without resetting, every step's gradient piles on top of the old ones and training goes haywire. PyTorch has exactly the same rule: `optimizer.zero_grad()` before `loss.backward()`. It's one of the most common bugs in real training code.

The same five steps in PyTorch, for comparison (you'll meet these lines again in Module 6):

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
for step in range(steps):
    loss = loss_fn(model(xs), ys)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

## Your quest

Write the body of `train`, replacing the four comment lines (keep `loss` as a `Value` so the print works): build the predictions, sum the squared errors into `loss`, zero all grads, call `loss.backward()`, and update every parameter.

The model must learn to output the four targets. Watch the loss.

## Review

<details><summary>Why are a network's weights initialized randomly?</summary>To break symmetry: identical weights would get identical gradients and stay identical.</details>
<details><summary>How many parameters does a layer from n inputs to m outputs have?</summary>n·m weights plus m biases.</details>
