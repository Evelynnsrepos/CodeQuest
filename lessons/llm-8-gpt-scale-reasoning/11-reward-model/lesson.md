---
title: RLHF step 1: a reward model
minutes: 50
xp: 60
hint: pair_loss: diff = r_chosen - r_rejected, if diff >= 0: return math.log1p(math.exp(-diff)), else return -diff + math.log1p(math.exp(diff))
hint: train_reward: w = [0.0] * len(pairs[0][0]), then for epoch in range(epochs): for c, r in pairs:
hint: Inside: diff = reward(w, c) - reward(w, r), scale = -(1 - sigmoid(diff)), then for i in range(len(w)): w[i] = w[i] - lr * scale * (c[i] - r[i])
---
# Teaching a model what people prefer

⏱️ About 50 minutes

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

## 🔬 Take the formulas apart

**The reward** is a dot product: weights × features. Features `[is_correct, is_polite, length]`, w = [2, 1, 0]: reward of [1, 1, 1] = 2 + 1 + 0 = 3.

**The probability that chosen beats rejected** <div class="formula">P(c ≻ r) = σ(<span class="k1">r_c − r_r</span>)</div>
- `≻` reads "is preferred to".
- σ is the sigmoid (LLMs 4, lesson 8): any number → 0…1.
- <span class="k1">r_c − r_r</span> is the difference of the two rewards, `diff`. diff = 0 → 0.5 (no idea). Big positive → near 1.

**The loss** <div class="formula">loss = −ln σ(diff)</div>
The surprise (LLMs 4 lesson 10) of "chosen wins". diff = 0 → −ln 0.5 = **0.693**. diff = 5 → σ ≈ 0.993 → loss ≈ **0.007**.

**Computing it safely.** `math.log1p(x)` is ln(1 + x), but accurate for tiny x. The same loss can be written ln(1 + e^(−diff)); for big negative diff, e^(−diff) would overflow, so you use the second form there. Both give the same number.

**The gradient** <div class="formula">∂loss/∂w = <span class="k1">−(1 − σ(diff))</span> · <span class="k2">(features_c − features_r)</span></div>
- <span class="k2">features_c − features_r</span>: what's different between the two answers.
- <span class="k1">−(1 − σ(diff))</span>: how wrong we still are. If σ(diff) ≈ 1 (already right), this is ≈ 0 and the step is tiny.

Numbers, first step (w = 0, so diff = 0, σ = 0.5): scale = −0.5. Pair `([1, 1, 1], [0, 1, 1])`: difference = [1, 0, 0]. w = w − 0.5 · (−0.5) · [1, 0, 0] = **[0.25, 0, 0]**: "correct" got more weight.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `math.log1p(x)` | "log one plus x" | ln(1 + x) |
| `math.exp(-diff)` | | e^(−diff) |
| `[0.0] * 3` | | `[0.0, 0.0, 0.0]` |
| `for c, r in pairs:` | | each pair: chosen features, rejected features |
| `w[i] = w[i] - lr * scale * (c[i] - r[i])` | | one weight, one gradient step |

### 👀 Worked example: one pair_loss

```python
diff = 3 - 1                       # chosen reward 3, rejected 1
print(math.log1p(math.exp(-diff)))  # ln(1 + e⁻²) = ln(1.135) ≈ 0.127
```

## 🎯 Your quest

`pair_loss(r_chosen, r_rejected)`: replace `return 0.0` with:

1. `    diff = r_chosen - r_rejected`
2. `    if diff >= 0:`
3. `        return math.log1p(math.exp(-diff))`
4. `    return -diff + math.log1p(math.exp(diff))`

`train_reward(pairs, lr, epochs)`: replace the `return` line with:

1. `    w = [0.0] * len(pairs[0][0])`
2. `    for epoch in range(epochs):`
3. `        for c, r in pairs:`
4. `            diff = reward(w, c) - reward(w, r)`
5. `            scale = -(1 - sigmoid(diff))`
6. `            for i in range(len(w)):`
7. `                w[i] = w[i] - lr * scale * (c[i] - r[i])`
8. `    return w`

The learned weights are about `[5.28, 4.66, -1.45]`: correctness and politeness count, length counts against.

## Review

<details><summary>In ZeRO-3, what is split across GPUs?</summary>Weights, gradients and optimizer state.</details>
<details><summary>What does an all-reduce do in data-parallel training?</summary>Averages the gradients across GPUs so every copy takes the same step.</details>
