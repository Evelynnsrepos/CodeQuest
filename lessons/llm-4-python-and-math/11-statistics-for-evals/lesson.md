---
title: Statistics for evaluating models
xp: 40
---
# Is the difference real?

> **Warm-up:** your fine-tuned model beats the base model on 13 of 20 test prompts. Is it better?

Maybe. Flip a fair coin 20 times and you'll get 13 or more heads about 13% of the time. Small evaluations are **noisy**, and the capstone's "compare on 20 held-out prompts" needs you to know how noisy.

The tools:

```
mean            x̄ = (x₁ + … + xₙ) / n
sample std dev  s = √( Σ (xᵢ − x̄)² / (n − 1) )      (n − 1: "Bessel's correction")
standard error  SE = s / √n                         how much x̄ itself would wobble
95% confidence interval ≈ x̄ ± 1.96 · SE
```

Encode each prompt as **1** if the tuned model won and **0** if it lost; the mean is the **win rate**. If the confidence interval includes **0.5**, you can't tell the models apart yet: you need more prompts, or the difference is too small to matter.

Notice `√n` in the standard error: to halve the uncertainty you need **four times** as many prompts. That's why serious benchmarks have hundreds or thousands of items. (With very small n or win rates near 0 or 1, the ±1.96·SE shortcut gets rough; boot.dev's *Learn Statistics for Programmers* and proper tests like the binomial test or Wilson interval do better.)

Other habits that matter more than formulas:

- **Held-out** prompts the model never saw in training, written *before* you look at results.
- **Blind** judging: shuffle which answer is A and B so you can't favour your own model.
- Fixed settings (same temperature, same seed where possible), or several samples per prompt.

## Your quest

Write `mean(xs)`, `std(xs)` (sample standard deviation, n − 1), `ci95(xs)` returning `(low, high)`, and `clearly_better(wins)`: `True` only if the whole interval is above 0.5.

## Review

<details><summary>Why is the LLM training loss called cross-entropy?</summary>It's the cross-entropy between the one-hot truth and the model's predicted distribution, which reduces to −log of the probability of the true token.</details>
<details><summary>Where does KL divergence show up in fine-tuning?</summary>RLHF and DPO keep the tuned model close to the reference model with a KL penalty; distillation minimizes KL to a teacher.</details>
