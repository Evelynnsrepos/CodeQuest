---
title: RLHF step 2: PPO with a KL leash
xp: 60
---
# Pushing the model toward reward, carefully

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

## Your quest

1. `ppo_objective(ratio, advantage, eps=0.2)`: the clipped objective for one token.
2. `kl_penalized_reward(reward, logp, logp_ref, beta)`: `logp` and `logp_ref` are lists, one entry per token.

## Review

<details><summary>Write the Bradley–Terry probability that c beats r.</summary>σ(r_c − r_r).</details>
<details><summary>What are the three steps of RLHF?</summary>SFT, train a reward model on comparisons, optimize the policy with RL against it.</details>
