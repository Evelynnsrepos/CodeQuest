---
title: GRPO and verifiable rewards
xp: 60
---
# Reinforcement learning without a reward model or a critic

> **Warm-up:** for "what is 17 × 23?" you don't need a human or a reward model to judge the answer. What do you need?

Just a **checker**. For math with a known answer, or code with unit tests, the reward can be computed by a program: **RL from verifiable rewards (RLVR)**. No reward model means nothing to hack except the checker itself.

**GRPO** (Group Relative Policy Optimization; DeepSeekMath, 2024) also removes PPO's value model. For each prompt:

1. Sample a **group** of `G` answers (say 8–64).
2. Score each with the verifier.
3. The **advantage** of each answer is how much better it did than its own group:

```
A_i = (r_i − mean(r)) / (std(r) + ε)
```

4. Use `A_i` for every token of answer `i` in PPO's clipped objective, plus a KL penalty to the reference.

If all answers in a group get the same reward, every advantage is 0 and nothing is learned from that prompt: it was too easy or too hard. Good RL datasets are chosen so the model sometimes succeeds.

**DeepSeek-R1** (2025) trained this way with only two rule-based rewards: is the final answer correct, and is the output in the required format (thinking between tags, then the answer). Long step-by-step reasoning, checking its own work and backtracking ("wait, let me recheck") *emerged* from the reward alone. Most open "reasoning" or "thinking" models since then use GRPO-like RL.

**Moving fast:** variants like Dr. GRPO and DAPO (2025) change the normalization (for example dropping the std division or the length averaging) to fix biases such as rewarding long wrong answers. Check current papers before relying on details.

## Your quest

1. `verify(text, truth)`: find the **last** line that starts with `"Answer:"`; return `1.0` if what follows (stripped) equals `truth`, else `0.0`. No such line (wrong format) gives `0.0`.
2. `group_advantages(rewards, eps=1e-6)`: the formula above, with the population standard deviation (divide by `G`).

## Review

<details><summary>What does PPO's clipping prevent?</summary>Changing a token's probability by more than about ±20% (ε) in one update.</details>
<details><summary>What is reward hacking?</summary>The policy exploits mistakes in the reward model to get high scores with bad answers.</details>
