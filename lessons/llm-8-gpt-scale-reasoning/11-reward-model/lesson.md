---
title: RLHF step 1: a reward model
xp: 60
---
# Teaching a model what people prefer

> **Warm-up:** "write a good poem" has no single correct answer, so there's no label to compute a loss against. What *can* you easily get from people instead?

**Comparisons.** People can't write the perfect answer, but they can say which of two answers is better. **RLHF** (reinforcement learning from human feedback; InstructGPT, OpenAI 2022, the recipe behind ChatGPT) has three steps:

1. **SFT**: fine-tune on example conversations (LLMs 6).
2. **Reward model**: train a model that gives any answer a score `r`, so that preferred answers score higher.
3. **RL**: optimize the language model to get high reward (next lesson).

The reward model uses the **Bradley–Terry** model (1952, originally for ranking chess players and sports teams): the probability that answer `c` (chosen) beats `r` (rejected) is

```
P(c ≻ r) = σ(r_c − r_r)        σ(x) = 1 / (1 + e^(−x))
loss     = −ln σ(r_c − r_r)
```

Only the *difference* matters. A real reward model is an LLM with its output head replaced by one number. Here it's linear: `reward = w · features`. The gradient (chain rule, LLMs 4): with `diff = r_c − r_r`,

```
∂loss/∂w = −(1 − σ(diff)) · (features_c − features_r)
```

DPO (LLMs 6, lesson 9) uses this same Bradley–Terry loss but skips the separate reward model.

## Your quest

`reward` and `sigmoid` are given.

1. `pair_loss(r_chosen, r_rejected)`: the loss above. Compute it stably as `math.log1p(math.exp(-diff))` when `diff ≥ 0`, else `-diff + math.log1p(math.exp(diff))`.
2. `train_reward(pairs, lr, epochs)`: `pairs` is a list of `(features_chosen, features_rejected)`. Start `w` at zeros, and for each epoch and each pair take one gradient step `w = w − lr · gradient`. Return `w`.

## Review

<details><summary>In ZeRO-3, what is split across GPUs?</summary>Weights, gradients and optimizer state.</details>
<details><summary>What does an all-reduce do in data-parallel training?</summary>Averages the gradients across GPUs so every copy takes the same step.</details>
