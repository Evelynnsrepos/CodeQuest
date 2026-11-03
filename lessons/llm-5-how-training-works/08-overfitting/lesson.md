---
title: Overfitting and the validation set
xp: 40
---
# Learning vs memorizing

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

## Your quest

1. `split(data, val_fraction)`: return `(train, val)`, where `val` is the **last** `int(len(data) * val_fraction)` items and `train` is the rest. (Real code shuffles first; the data here is already shuffled.)
2. `best_epoch(val_losses)`: the index of the lowest validation loss (early stopping picks it).
3. `overfitting_starts(train_losses, val_losses)`: the first epoch `i ≥ 1` where training loss went **down** but validation loss went **up** compared with epoch `i − 1`. Return `None` if that never happens.

The program uses a recorded training run's loss curves.

## Review

<details><summary>What is an epoch? A step?</summary>An epoch is one pass over all training data; a step is one batch's forward, backward and update.</details>
<details><summary>What does gradient accumulation do?</summary>Adds gradients from several small batches before one update, simulating a bigger batch with less memory.</details>
