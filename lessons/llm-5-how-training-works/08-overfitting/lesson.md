---
title: Overfitting and the validation set
minutes: 40
xp: 40
hint: split: n_val = int(len(data) * val_fraction), cut = len(data) - n_val, return data[:cut], data[cut:]
hint: best_epoch: return val_losses.index(min(val_losses))
hint: overfitting_starts: for i in range(1, len(train_losses)): then train_down = train_losses[i] < train_losses[i - 1] and val_up = val_losses[i] > val_losses[i - 1]
hint: Then if train_down and val_up: return i. After the loop: return None
---
# Learning vs memorizing

⏱️ About 40 minutes

> **Warm-up:** a student memorizes last year's exam answers word for word. They ace the practice exam. What happens on the real one?

A model with enough parameters can do the same: drive the loss on its training data towards zero by **memorizing** it, while getting *worse* on anything new. That's **overfitting**, and the only way to see it is to measure on data the model never trains on.

So you split your data:

| Split | Used for | Typical share |
|---|---|---|
| **training** set | computing gradients and updating weights | 80–90% |
| **validation** set | measuring progress during training, choosing settings | 10–20% |
| **test** set (optional) | one final, honest measurement at the very end | held back |

Then you watch two curves. Early on both fall. When the training loss keeps falling but the **validation loss turns around and rises**, the model has started memorizing:

```
loss
 │\
 │ \  validation          ← starts rising: overfitting begins
 │  \______    ___/‾‾‾
 │   \     ‾‾‾
 │    \_______  training  ← keeps falling
 │            ‾‾‾‾‾‾‾‾‾‾
 └──────────────────────── epochs
```

Remedies: **early stopping** (keep the checkpoint with the lowest validation loss), **more or more varied data**, **regularization** (weight decay, dropout), a **smaller model or fewer epochs**. In fine-tuning, overfitting shows up as a model that parrots your training examples and has forgotten general skills, so in Module 6 and the capstone you'll always keep a validation split.

One rule matters more than any formula: **never let validation or test examples leak into training.** Duplicates across the split make the validation score lie.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `int(50 * 0.2)` | "int of ten point zero" | cuts off the decimals: `10` |
| `data[:cut]` | "data up to cut" | everything before position `cut` |
| `data[cut:]` | "data from cut on" | everything from `cut` to the end |
| `min(val_losses)` | | the smallest number in the list |
| `val_losses.index(x)` | | the **position** of `x` in the list (the first one, if it appears twice) |
| `range(1, len(train_losses))` | | starts at 1, because epoch 0 has nothing before it to compare with |
| `train_losses[i - 1]` | | the epoch before |
| `a < b` stored in a name | | `train_down` becomes `True` or `False` |
| `if train_down and val_up:` | | both must be true |
| `return None` | | "no answer": it never happened |

### 👀 Worked example: reading the recorded run

```
epoch:   0     1     2     3     4     5     6
train: 2.10  1.62  1.31  1.12  0.95  0.80  0.66
val:   2.15  1.70  1.45  1.33  1.30  1.32  1.38
```

1. Epochs 1 to 4: both go down. Not overfitting.
2. Epoch 5: train 0.95 → 0.80 (down ✅), val 1.30 → 1.32 (up ✅). **Overfitting starts at 5.**
3. The lowest val loss is 1.30, at position **4**: that's the checkpoint early stopping keeps.

The split with 50 examples and 0.2: n_val = int(10.0) = 10, cut = 50 − 10 = 40 → 40 training, 10 validation.

## 🎯 Your quest

`split(data, val_fraction)`: replace `return data, []` with:

1. `    n_val = int(len(data) * val_fraction)`
2. `    cut = len(data) - n_val`
3. `    return data[:cut], data[cut:]`

`best_epoch(val_losses)`: replace `return 0` with `    return val_losses.index(min(val_losses))`

`overfitting_starts(train_losses, val_losses)`: above `return None`, add:

1. `    for i in range(1, len(train_losses)):`
2. `        train_down = train_losses[i] < train_losses[i - 1]`
3. `        val_up = val_losses[i] > val_losses[i - 1]`
4. `        if train_down and val_up:`
5. `            return i`

It prints `40 training, 10 validation`, then epochs 4 and 5.

## Review

<details><summary>What is an epoch? A step?</summary>An epoch is one pass over all training data; a step is one batch's forward, backward and update.</details>
<details><summary>What does gradient accumulation do?</summary>Adds gradients from several small batches before one update, simulating a bigger batch with less memory.</details>
