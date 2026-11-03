---
title: Momentum, Adam, AdamW and LR schedules
xp: 50
---
# Smarter steps than plain SGD

> **Warm-up:** in a long narrow valley, the gradient points mostly at the steep walls, not along the valley floor. What happens to plain gradient descent there?

It zig-zags between the walls and crawls along the floor. With a learning rate small enough not to explode on the steep direction, the shallow direction barely moves. Real loss surfaces are full of such valleys, so better optimizers keep extra state per weight:

**Momentum** keeps a running average of past gradients (`m`), so consistent directions build up speed and zig-zags cancel out.

**Adam** (Kingma & Ba, 2014) also tracks a running average of **squared** gradients (`v`) and divides by its square root. Every weight gets its own effective step size: steep directions are damped, shallow ones boosted. Both averages start at 0, so early on they're biased towards 0; Adam corrects that by dividing by `1 − βᵗ`.

**AdamW** (Loshchilov & Hutter, 2017) adds **weight decay** the right way: shrink every weight a little towards 0 each step, separately from the gradient. It's the default optimizer for training transformers, including every LLM fine-tune you'll run.

```
for each weight p with gradient g, at step t (starting at 1):
    m = β₁·m + (1 − β₁)·g
    v = β₂·v + (1 − β₂)·g²
    m̂ = m / (1 − β₁ᵗ)          v̂ = v / (1 − β₂ᵗ)
    p = p − lr·wd·p − lr · m̂ / (√v̂ + ε)
typical: β₁ = 0.9, β₂ = 0.999, ε = 1e-8, wd = 0.01
```

The cost: two extra numbers (`m`, `v`) **per weight**. That's why full fine-tuning needs so much memory (lesson 13) and why LoRA (Module 6) only trains a few weights.

**Learning-rate schedules.** Almost every LLM run uses **warmup** (ramp the LR up from ~0 over the first steps, while Adam's statistics are still unreliable) followed by **cosine decay** (smoothly down towards 0, so the end of training makes fine adjustments):

```
step < warmup:   lr = max_lr · (step + 1) / warmup
afterwards:      lr = max_lr · ½ · (1 + cos(π · progress)),  progress = (step − warmup) / (total − warmup)
```

## Your quest

1. `adamw_step(params, grads, m, v, t, lr, wd)`: update the lists `params`, `m` and `v` **in place** (change `params[i]`, `m[i]`, `v[i]`) using the formulas above with β₁ = 0.9, β₂ = 0.999, ε = 1e-8.
2. `lr_at(step, max_lr, warmup, total)`: the warmup + cosine schedule.

The program races plain SGD against AdamW down a narrow valley.

## Review

<details><summary>How do you spot overfitting?</summary>Training loss keeps falling while validation loss starts rising.</details>
<details><summary>What does early stopping keep?</summary>The checkpoint with the lowest validation loss.</details>
<details><summary>Why must validation data never leak into training?</summary>Then the validation score measures memorization instead of generalization and lies to you.</details>
