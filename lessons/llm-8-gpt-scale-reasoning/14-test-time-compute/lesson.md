---
title: Thinking longer, and measuring it fairly
minutes: 45
xp: 50
hint: majority_vote: counts = {}, for a in answers: counts[a] = counts.get(a, 0) + 1
hint: Then best = answers[0], for a in answers: if counts[a] > counts[best]: best = a. return best
hint: pass_at_k: if n - c < k: return 1.0. Otherwise return 1 - math.comb(n - c, k) / math.comb(n, k)
---
# Spending compute at answer time

⏱️ About 45 minutes

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

## 🔬 Take the formula apart

**"n choose k"**, written C(n, k): how many different ways to pick k things out of n (order doesn't matter). C(4, 2) = 6: from {a, b, c, d} you can pick ab, ac, ad, bc, bd, cd. Python: `math.comb(4, 2)`.

<div class="formula">pass@k = 1 − <span class="k1">C(n − c, k)</span> / <span class="k2">C(n, k)</span></div>
- You have n samples, c of them correct. You pick k at random.
- <span class="k2">C(n, k)</span>: all the ways to pick k.
- <span class="k1">C(n − c, k)</span>: the ways that pick **only wrong** ones.
- Their ratio is the chance that all k are wrong. 1 minus that = the chance that **at least one** is right.

Numbers, n = 10, c = 3, k = 5: C(7, 5) = 21, C(10, 5) = 252. 21 / 252 ≈ 0.083. 1 − 0.083 = **0.917**. With k = 1 it's simply 3/10 = 0.3.

If there are fewer wrong samples than k (n − c < k), every pick must include a right one: pass@k = **1**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `counts = {}` | | a dictionary: answer → how often |
| `counts.get(a, 0) + 1` | | the count so far (0 if new), plus one |
| `if counts[a] > counts[best]:` | | strictly more; on a tie the earlier one stays |
| `math.comb(n, k)` | "n choose k" | C(n, k) |

### 👀 Worked example: counting votes

`["42", "41", "42"]` → counts `{"42": 2, "41": 1}`. best starts as "42"; "41" has 1, not more than 2; → **"42"**.

## 🎯 Your quest

`majority_vote(answers)`: replace `return answers[0]` with:

1. `    counts = {}`
2. `    for a in answers:`
3. `        counts[a] = counts.get(a, 0) + 1`
4. `    best = answers[0]`
5. `    for a in answers:`
6. `        if counts[a] > counts[best]:`
7. `            best = a`
8. `    return best`

`pass_at_k(n, c, k)`: replace `return c / n` with:

1. `    if n - c < k:`
2. `        return 1.0`
3. `    return 1 - math.comb(n - c, k) / math.comb(n, k)`

## Review

<details><summary>Why does GRPO need no value model?</summary>It uses the group's own mean reward as the baseline for each answer's advantage.</details>
<details><summary>What does a group with all-equal rewards teach the model?</summary>Nothing: every advantage is 0.</details>
