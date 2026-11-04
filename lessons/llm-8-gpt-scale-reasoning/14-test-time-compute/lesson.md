---
title: Thinking longer, and measuring it fairly
xp: 50
---
# Spending compute at answer time

> **Warm-up:** a model gets a hard math question right 30% of the time. Without retraining it, how could you make it right more often?

Spend more compute **when answering** (test-time compute):

- **Chain of thought:** ask for (or train for) step-by-step reasoning before the answer. Each generated token is one more forward pass of computation the model can use. Reasoning models are trained with RL (last lesson) to produce long, useful thinking.
- **Self-consistency** (Wang et al., 2022): sample several answers at temperature > 0 and take the **majority vote** on the final answer. Wrong reasoning paths tend to disagree with each other; right ones agree.
- **Best-of-n with a verifier:** sample n, keep the one a checker or reward model likes best.

**Measuring it.** **pass@k** is the probability that at least one of `k` samples is correct. Estimating it by taking just k samples is noisy, so (Chen et al., 2021, the Codex paper) take `n ≥ k` samples, count the `c` correct ones, and use the unbiased estimator

```
pass@k = 1 − C(n − c, k) / C(n, k)
```

where `C(a, b)` is "a choose b" (`math.comb`). It's the chance that a random subset of `k` of your `n` samples contains at least one correct one. If `n − c < k`, every subset contains a correct one, so pass@k = 1.

Be careful comparing models: pass@1 (one try) and pass@64 can rank models differently, and reasoning models also spend far more tokens per answer, so report the token cost too. Also watch for **contamination**: popular benchmarks leak into training data, which is why new benchmarks keep appearing.

## Your quest

1. `majority_vote(answers)`: the most common answer; on a tie, the one that appeared first.
2. `pass_at_k(n, c, k)`: the estimator above.

## Review

<details><summary>Why does GRPO need no value model?</summary>It uses the group's own mean reward as the baseline for each answer's advantage.</details>
<details><summary>What does a group with all-equal rewards teach the model?</summary>Nothing: every advantage is 0.</details>
