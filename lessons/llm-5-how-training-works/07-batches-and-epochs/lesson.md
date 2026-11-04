---
title: Learning rate, batches and epochs
xp: 40
---
# The knobs of a training run

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

## Python you need

`data[i:i + size]` for `i` in `range(0, len(data), size)` walks the data in chunks. `math.ceil(x)` rounds up.

## Your quest

1. `make_batches(data, batch_size)`: split the list into consecutive batches; the last may be smaller.
2. `steps_per_epoch(n_examples, batch_size)`.
3. `train(data, lr, epochs, batch_size)`: for each epoch, for each batch, compute the batch's gradients (the `gradients` function from lesson 1 is given) and update `w` and `b`. Return `(w, b)`.

## Review

<details><summary>What does optimizer.zero_grad() / p.grad = 0 prevent?</summary>Gradients from earlier steps piling up, because backward() adds to .grad.</details>
<details><summary>Write the five lines of a PyTorch training step.</summary>loss = loss_fn(model(x), y); optimizer.zero_grad(); loss.backward(); optimizer.step(); (in a loop over batches).</details>
