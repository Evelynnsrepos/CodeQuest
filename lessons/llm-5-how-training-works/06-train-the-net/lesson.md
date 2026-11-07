---
title: Training your neural network
minutes: 50
xp: 50
hint: Forward: predictions = [], for x in xs: predictions.append(model(x)[0])
hint: Loss: loss = Value(0.0), then for i in range(len(ys)): loss = loss + (predictions[i] - ys[i]) ** 2
hint: Zero, then backward: for p in model.parameters(): p.grad = 0.0, and after that loop loss.backward()
hint: Update: for p in model.parameters(): p.data = p.data - learning_rate * p.grad
---
# Watch the loss go down

⏱️ About 50 minutes

> **Warm-up:** you have a model, data and gradients. Write the training loop from memory, as five steps, before reading on.

Here it is with micrograd:

1. **Forward:** run the model on every example → predictions.
2. **Loss:** add up the squared errors into one `Value`.
3. **Zero the grads**, then **backward**: fill in every `.grad`.
4. **Update:** nudge every parameter against its gradient.
5. **Repeat.**

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

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `model(x)[0]` | | the model returns a list with one output; `[0]` takes that one `Value` |
| `loss = Value(0.0)` | | start the total as a `Value`, so the sum is part of the graph |
| `(predictions[i] - ys[i]) ** 2` | | squared error for example i. `Value` minus a plain number works (lesson 4). |
| `p.grad = 0.0` | | wipe the old gradient |
| `loss.backward()` | | fills in `.grad` on every parameter (lesson 3) |
| `p.data = p.data - learning_rate * p.grad` | | one gradient descent step on the plain number inside |

### 👀 Worked example: one round by hand

One example, x = [1], target 1, a model whose output is just `w · 1` with w = 0.5. Learning rate 0.1.

1. Forward: prediction = 0.5.
2. Loss: (0.5 − 1)² = 0.25.
3. Zero and backward: d(loss)/dw = 2 · (0.5 − 1) · 1 = **−1**.
4. Update: w = 0.5 − 0.1 · (−1) = **0.6**. Closer to 1. Next round: loss (0.6 − 1)² = 0.16, lower.

Your loop does this for all 41 parameters at once, 60 times.

## 🎯 Your quest

In `train`, below `for step in range(steps):`, add these lines (8 spaces in, more inside the small loops).

1. `        predictions = []`
2. `        for x in xs:`
3. `            predictions.append(model(x)[0])`
4. `        loss = Value(0.0)`
5. `        for i in range(len(ys)):`
6. `            loss = loss + (predictions[i] - ys[i]) ** 2`
7. `        for p in model.parameters():`
8. `            p.grad = 0.0`
9. `        loss.backward()`
10. `        for p in model.parameters():`
11. `            p.data = p.data - learning_rate * p.grad`

Watch the loss fall to almost 0; the predictions end close to the targets `[1, -1, -1, 1]`.

## Review

<details><summary>Why are a network's weights initialized randomly?</summary>To break symmetry: identical weights would get identical gradients and stay identical.</details>
<details><summary>How many parameters does a layer from n inputs to m outputs have?</summary>n·m weights plus m biases.</details>
