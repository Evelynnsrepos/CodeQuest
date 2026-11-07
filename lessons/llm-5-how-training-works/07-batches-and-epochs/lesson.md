---
title: Learning rate, batches and epochs
minutes: 45
xp: 40
hint: make_batches: batches = [], for i in range(0, len(data), batch_size): batches.append(data[i:i + batch_size]), return batches
hint: steps_per_epoch: return math.ceil(n_examples / batch_size)
hint: train: for epoch in range(epochs): and inside it for batch in make_batches(data, batch_size):
hint: Inside both loops: dw, db = gradients(w, b, batch), w = w - lr * dw, b = b - lr * db
---
# The knobs of a training run

⏱️ About 45 minutes

> **Warm-up:** an LLM's training set has trillions of tokens. Can you compute the exact gradient over *all* of it before every single step?

No, one step would take forever. Instead, each step uses a small random **batch** of examples, and the batch's average gradient serves as a noisy estimate of the true one. That's **stochastic gradient descent (SGD)** with **mini-batches**, and it's how every model is trained.

| Knob | Meaning | Typical effect |
|---|---|---|
| **batch size** | examples per step | bigger: smoother gradient, more memory per step; smaller: noisier, more steps |
| **step** (iteration) | one batch: forward, backward, update | |
| **epoch** | one full pass over the training data | steps per epoch = ⌈examples ÷ batch size⌉ |
| **learning rate** | step size | the single most important knob |

The noise of small batches isn't all bad: it helps escape flat regions and often generalizes better. When a big batch doesn't fit in memory, **gradient accumulation** adds up the gradients of several small batches before one update (Module 6 uses this on your 12 GB card).

**Learning rate**: too low and loss crawls; too high and it bounces or **diverges** (loss becomes huge or `nan`). The output of this lesson shows all three. Fine-tuning runs typically use around `1e-5` to `2e-4`; you'll see why in Module 6.

LLM pretraining is usually measured in **tokens** rather than epochs, often less than one epoch over the data. Fine-tuning typically runs 1–3 epochs over a small dataset; more invites **overfitting** (next lesson).

## 🔬 Take the formula apart

<div class="formula">steps per epoch = <span class="k1">⌈</span> <span class="k2">examples</span> ÷ <span class="k3">batch size</span> <span class="k1">⌉</span></div>

- <span class="k1">⌈ ⌉</span> are "ceiling" brackets: **round up** to the next whole number. ⌈2.1⌉ = 3, ⌈2.0⌉ = 2.
- Why up? 40 examples in batches of 16: 40 ÷ 16 = 2.5. Two full batches (32 examples) plus one smaller batch with the last 8. That's **3** steps, and 2.5 rounded up is 3.

Python: `math.ceil(40 / 16)` → 3.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `range(0, 40, 16)` | "range from 0 to 40 in steps of 16" | 0, 16, 32 |
| `data[i:i + batch_size]` | "data from i up to i plus batch size" | the slice for one batch. Past the end it just stops: `data[32:48]` on 40 items gives the last 8. |
| `math.ceil(x)` | "ceiling of x" | rounds up |
| a loop inside a loop | | for **every** epoch, go through **every** batch |
| `gradients(w, b, batch)` | | the given function from lesson 1, on just this batch |

### 👀 Worked example: 7 cards in packs of 3

```python
cards = ["A", "B", "C", "D", "E", "F", "G"]
packs = []
for i in range(0, len(cards), 3):
    packs.append(cards[i:i + 3])
print(packs)                  # [['A', 'B', 'C'], ['D', 'E', 'F'], ['G']]
print(math.ceil(7 / 3))       # 3
```

1. `i` = 0: `cards[0:3]` → A, B, C.
2. `i` = 3: `cards[3:6]` → D, E, F.
3. `i` = 6: `cards[6:9]` → only G is left.

## 🎯 Your quest

`make_batches(data, batch_size)`: replace `return []` with:

1. `    batches = []`
2. `    for i in range(0, len(data), batch_size):`
3. `        batches.append(data[i:i + batch_size])`
4. `    return batches`

`steps_per_epoch(n_examples, batch_size)`: replace `return 0` with `    return math.ceil(n_examples / batch_size)`

`train(data, lr, epochs, batch_size)`: between `w, b = 0.0, 0.0` and `return w, b`, add:

1. `    for epoch in range(epochs):`
2. `        for batch in make_batches(data, batch_size):`
3. `            dw, db = gradients(w, b, batch)`
4. `            w = w - lr * dw`
5. `            b = b - lr * db`

The output shows the three learning-rate stories: lr 0.001 crawls (still far off), lr 0.05 lands near w = 3, b = 1, and lr 0.3 explodes into huge numbers.

## Review

<details><summary>What does optimizer.zero_grad() / p.grad = 0 prevent?</summary>Gradients from earlier steps piling up, because backward() adds to .grad.</details>
<details><summary>Write the five lines of a PyTorch training step.</summary>loss = loss_fn(model(x), y); optimizer.zero_grad(); loss.backward(); optimizer.step(); (in a loop over batches).</details>
