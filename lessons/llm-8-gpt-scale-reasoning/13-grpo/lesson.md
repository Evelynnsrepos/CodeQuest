---
title: GRPO and verifiable rewards
minutes: 45
xp: 60
hint: verify: last = None, for line in text.splitlines(): if line.startswith("Answer:"): last = line
hint: verify continued: if last is None: return 0.0. if last[len("Answer:"):].strip() == truth: return 1.0. Last line: return 0.0
hint: group_advantages: n, mean = sum(rewards) / n, total of (r - mean) ** 2, std = math.sqrt(total / n), then out.append((r - mean) / (std + eps))
---
# Reinforcement learning without a reward model or a critic

⏱️ About 45 minutes

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

## 🔬 Take the formula apart

<div class="formula">Aᵢ = (<span class="k1">rᵢ − mean(r)</span>) / (<span class="k2">std(r)</span> + <span class="k3">ε</span>)</div>
- The model writes a **group** of G answers to one question; rᵢ is answer i's reward (1 right, 0 wrong).
- <span class="k1">rᵢ − mean</span>: better or worse than the group's average?
- <span class="k2">std</span>: the standard deviation (LLMs 4, lesson 11), here dividing by G. Dividing by it puts the advantages on a standard scale.
- <span class="k3">ε</span> = 0.000001 stops a division by 0 when all rewards are equal.

Numbers, rewards [1, 0, 1, 0]: mean = 0.5. Distances ±0.5, squared 0.25 each, average 0.25, √ = **0.5**. A = (1 − 0.5) / 0.5 = **+1**, (0 − 0.5) / 0.5 = **−1**. Right answers get pushed up, wrong ones down. No reward model needed.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `text.splitlines()` | | the lines of the text |
| `line.startswith("Answer:")` | | true if the line begins with that |
| `last = line` in a loop | | after the loop, `last` is the **last** matching line |
| `last[len("Answer:"):]` | | everything after "Answer:" |
| `.strip()` | | removes spaces at both ends |
| `if last is None:` | | no "Answer:" line at all |

### 👀 Worked example: verify

`"I think it's 40.\nAnswer: 40"` → lines `["I think it's 40.", "Answer: 40"]`. last = "Answer: 40". After "Answer:": " 40" → strip → "40". "40" == "42"? No → **0.0**.

## 🎯 Your quest

`verify(text, truth)`: replace `return 0.0` with:

1. `    last = None`
2. `    for line in text.splitlines():`
3. `        if line.startswith("Answer:"):`
4. `            last = line`
5. `    if last is None:`
6. `        return 0.0`
7. `    if last[len("Answer:"):].strip() == truth:`
8. `        return 1.0`
9. `    return 0.0`

`group_advantages(rewards, eps=1e-6)`: replace the `return` line with:

1. `    n = len(rewards)`
2. `    mean = sum(rewards) / n`
3. `    total = 0`
4. `    for r in rewards:`
5. `        total = total + (r - mean) ** 2`
6. `    std = math.sqrt(total / n)`
7. `    out = []`
8. `    for r in rewards:`
9. `        out.append((r - mean) / (std + eps))`
10. `    return out`

## Review

<details><summary>What does PPO's clipping prevent?</summary>Changing a token's probability by more than about ±20% (ε) in one update.</details>
<details><summary>What is reward hacking?</summary>The policy exploits mistakes in the reward model to get high scores with bad answers.</details>
