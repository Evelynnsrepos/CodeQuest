---
title: RLHF step 2: PPO with a KL leash
minutes: 40
xp: 60
hint: ppo_objective: clipped = ratio, if clipped < 1 - eps: clipped = 1 - eps, if clipped > 1 + eps: clipped = 1 + eps
hint: ppo_objective ends: return min(ratio * advantage, clipped * advantage)
hint: kl_penalized_reward: total = 0, for i in range(len(logp)): total = total + logp[i] - logp_ref[i], return reward - beta * total
---
# Pushing the model toward reward, carefully

⏱️ About 40 minutes

> **Warm-up:** if you just maximize the reward model's score, what will the language model find?

The reward model's **mistakes**. It will produce whatever weird text the reward model happens to overrate: very long answers, flattery, repeated phrases. This is **reward hacking** (Goodhart's law: a measure that becomes a target stops being a good measure). Two safeguards:

**1. A KL penalty.** Keep the model close to the SFT model (the **reference**). For a sampled answer, with each token's log-probability under the current model (`logp`) and the reference (`logp_ref`):

```
total reward = reward − β · Σ (logp_t − logp_ref_t)
```

The sum estimates the KL divergence between the two models (LLMs 4, information theory). `β` (like 0.01–0.1) sets how short the leash is.

**2. PPO's clipping** (Proximal Policy Optimization, Schulman et al. 2017). The **advantage** `A` says how much better an action was than expected. The **ratio** `ρ = π_new(token) / π_old(token)` says how much the update changed its probability. PPO maximizes

```
min(ρ·A, clip(ρ, 1 − ε, 1 + ε)·A)        ε ≈ 0.2
```

So once a good token's probability went up by more than 20%, there's no more gain from raising it further in this batch; same for lowering bad ones. Updates stay small and stable.

Full PPO for LLMs needs **four models** in memory: the policy, the reference, the reward model and a **value model** (critic) that estimates expected reward to compute advantages. That's why it's expensive, and why DPO (no reward model, no RL loop) and GRPO (no value model, next lesson) became popular.

## 🔬 Take the formulas apart

**The ratio** ρ ("rho") = new probability of the token ÷ old probability. ρ = 1.5: the update made it 50% more likely.

**The advantage** A: was this token better (+) or worse (−) than expected?

**clip** <div class="formula">clip(ρ, <span class="k1">1 − ε</span>, <span class="k2">1 + ε</span>)</div>
Keep ρ inside the range <span class="k1">0.8</span> to <span class="k2">1.2</span> (ε = 0.2). 1.5 → 1.2. 0.5 → 0.8. 1.1 stays 1.1.

**The objective** <div class="formula">min(<span class="k1">ρ·A</span>, <span class="k2">clip(ρ)·A</span>)</div>
Take the **smaller** of the two. Numbers:
1. ρ = 1.5, A = +1: min(1.5, 1.2) = **1.2**. No extra reward for moving further than 20%.
2. ρ = 1.5, A = −1: min(−1.5, −1.2) = **−1.5**. A bad move is punished fully.
3. ρ = 0.5, A = −1: min(−0.5, −0.8) = **−0.8**.

**The KL-penalized reward** <div class="formula">reward − <span class="k1">β</span> · <span class="k2">Σ (logp_t − logp_ref_t)</span></div>
For each token t, how much more likely the new model finds it than the reference, added up, times β. Numbers: (−1 − (−1.2)) + (−0.5 − (−1.5)) + (−2 − (−2)) = 0.2 + 1.0 + 0 = 1.2. 2.0 − 0.1 × 1.2 = **1.88**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `clipped = ratio` then two `if`s | | pushes it back into the range if it's outside |
| `min(a, b)` | | the smaller one |
| `logp[i] - logp_ref[i]` | | one token's difference |

### 👀 Worked example: clipping by hand

```python
ratio, eps = 0.5, 0.2
clipped = ratio
if clipped < 1 - eps:      # 0.5 < 0.8: yes
    clipped = 1 - eps      # 0.8
if clipped > 1 + eps:      # 0.8 > 1.2: no
    clipped = 1 + eps
print(clipped)             # 0.8
```

## 🎯 Your quest

`ppo_objective(ratio, advantage, eps=0.2)`: replace the `return` line with:

1. `    clipped = ratio`
2. `    if clipped < 1 - eps:`
3. `        clipped = 1 - eps`
4. `    if clipped > 1 + eps:`
5. `        clipped = 1 + eps`
6. `    return min(ratio * advantage, clipped * advantage)`

`kl_penalized_reward(reward, logp, logp_ref, beta)`: replace `return reward` with:

1. `    total = 0`
2. `    for i in range(len(logp)):`
3. `        total = total + logp[i] - logp_ref[i]`
4. `    return reward - beta * total`

## Review

<details><summary>Write the Bradley–Terry probability that c beats r.</summary>σ(r_c − r_r).</details>
<details><summary>What are the three steps of RLHF?</summary>SFT, train a reward model on comparisons, optimize the policy with RL against it.</details>
