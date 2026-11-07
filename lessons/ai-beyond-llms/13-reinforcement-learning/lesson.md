---
title: Reinforcement learning basics
minutes: 40
xp: 60
hint: greedy: values = Q[s] and best = 0, then for a in range(len(values)): if values[a] > values[best]: best = a
hint: q_update: if s2 is None: target = r, else: target = r + gamma * max(Q[s2])
hint: q_update: Q[s][a] = Q[s][a] + alpha * (target - Q[s][a]), then return Q[s][a]
---
# Learning from rewards, not answers

⏱️ About 40 minutes

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

## 🔬 Take the update apart

**The signs:**

| Sign | Say it | Means |
|---|---|---|
| `Q(s, a)` | "Q of s and a" | how good action a in state s is, as far as the agent knows so far. In the code: `Q[s][a]`. |
| `r` | "r" | the reward for this one step |
| `s'` | "s prime" | the state you landed in. In the code: `s2`. |
| `γ` | "gamma" | the discount: a reward one step later is worth only γ as much (0.9 = 90%) |
| `max_a' Q(s', a')` | "the max over a prime of Q of s prime, a prime" | the value of the **best** action in the next state. In the code: `max(Q[s2])`. |
| `α` | "alpha" | the learning rate: how far to move towards the target |

**One update, in small steps**: Q[0] = [0, 0] and Q[1] = [0, 1.0]. In state 0 the agent goes right (a = 1), gets r = 0, lands in s2 = 1. α = 0.5, γ = 0.9.

1. The best value in state 1: max(0, 1.0) = **1.0**.
2. target = r + γ · 1.0 = 0 + 0.9 × 1.0 = **0.9**.
3. How wrong the old value was: target − Q[0][1] = 0.9 − 0 = 0.9.
4. Move half-way (α = 0.5): 0 + 0.5 × 0.9 = **0.45**. So Q[0][1] becomes 0.45.

State 1 was already known to be good, and now some of that "good" has flowed back into state 0. That's credit assignment, one step at a time. When the episode has ended (s2 is `None`), there's no next state, so the target is just r.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `values = Q[s]` | | the list of action values in state s, like `[0.0, 0.45]` |
| `if values[a] > values[best]:` | | best-so-far. `>` keeps the lower index on a tie. |
| `if s2 is None:` | "if there is no next state" | the episode ended |
| `max(Q[s2])` | "max of Q at s2" | the biggest number in that list |
| `Q[s][a] = ...` | | changes the value **inside** the dictionary's list ("in place"), so the training loop sees it |

## 🎯 Your quest

`Q` is a dict from state to a list of action values. `env_step` is a tiny corridor world.

1. `greedy(Q, s)`: the index of the best action in state `s` (lowest index on ties).
2. `q_update(Q, s, a, r, s2, alpha, gamma)`: update `Q[s][a]` in place with the rule above; `s2` is `None` when the episode ended. Return the new value.

**Part 1:** `greedy`. Replace `return 0` with:

1. `values = Q[s]`
2. `best = 0`
3. `for a in range(len(values)):`
4. `    if values[a] > values[best]:`
5. `        best = a`
6. `return best`

**Part 2:** `q_update`. Replace `return Q[s][a]` with:

1. `if s2 is None:`
2. `    target = r`
3. `else:`
4. `    target = r + gamma * max(Q[s2])`
5. `Q[s][a] = Q[s][a] + alpha * (target - Q[s][a])`
6. `return Q[s][a]`

When you run it, the agent learns to go right in every state, and the values grow towards the goal: about 0.81, 0.9, 1.

## Review

<details><summary>What does a vision-language model's projector do?</summary>Maps the vision encoder's patch vectors into the LLM's token-embedding space.</details>
<details><summary>Where does the vision part of a GGUF vision model live?</summary>In a separate mmproj file.</details>
