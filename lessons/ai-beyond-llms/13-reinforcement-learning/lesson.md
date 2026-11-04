---
title: Reinforcement learning basics
xp: 60
---
# Learning from rewards, not answers

> **Warm-up:** nobody tells a chess player the right move after each turn; they only learn at the end whether they won. How can earlier moves get credit for a win?

That's the **credit assignment** problem, the core of **reinforcement learning (RL)**. An **agent** in **state** `s` takes an **action** `a`, the environment returns a **reward** `r` and the next state `s'`. The goal is to maximize total future reward, with later rewards **discounted** by `γ` (gamma, like 0.9–0.99) per step.

**Q-learning** (Watkins, 1989) learns `Q(s, a)`: the expected future reward of doing `a` in `s` and acting well afterwards. After every step:

```
target  = r + γ · max_a' Q(s', a')        (just r if the episode ended)
Q(s, a) = Q(s, a) + α · (target − Q(s, a))
```

`α` is the learning rate. The reward at the goal flows backwards one step at a time through the `max`, which solves credit assignment. To keep discovering, the agent is **ε-greedy**: usually take the best known action, sometimes a random one (**exploration vs exploitation**).

Where it went next:

- **DQN** (DeepMind, 2015): a CNN approximates Q from screen pixels and learned Atari games.
- **AlphaGo** (2016) and AlphaZero: policy and value networks plus tree search, self-play.
- **Policy gradient** methods learn the policy directly: raise the probability of actions with positive **advantage**. PPO (LLMs 8) is one, and RLHF and GRPO are policy-gradient RL where the "actions" are tokens.

## Your quest

`Q` is a dict from state to a list of action values. `env_step` is a tiny corridor world.

1. `greedy(Q, s)`: the index of the best action in state `s` (lowest index on ties).
2. `q_update(Q, s, a, r, s2, alpha, gamma)`: update `Q[s][a]` in place with the rule above; `s2` is `None` when the episode ended. Return the new value.

## Review

<details><summary>What does a vision-language model's projector do?</summary>Maps the vision encoder's patch vectors into the LLM's token-embedding space.</details>
<details><summary>Where does the vision part of a GGUF vision model live?</summary>In a separate mmproj file.</details>
