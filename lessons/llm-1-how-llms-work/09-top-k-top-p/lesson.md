---
title: Top-k, top-p and min-p
minutes: 40
xp: 30
hint: top_k: for token, q in ranked[:k]: and inside it kept[token] = q
hint: top_p: for token, q in ranked: and inside it kept[token] = q and running = running + q
hint: top_p, still inside the loop: if running >= p: and under it break
---
# Cutting off the long tail

⏱️ About 40 minutes

> **Warm-up:** a vocabulary has ~150,000 tokens. Even if each nonsense token only has a 0.001% chance, what happens when you add all of them up over a 500-token reply?

The long tail of unlikely tokens adds up. Sampling over all of them means that, now and then, a garbage token sneaks in and derails the reply. So samplers first **cut the list down**, then **renormalize** the survivors (divide by their total so they add up to 1 again), then draw.

| Sampler | Keeps | Problem it solves |
|---|---|---|
| **top-k** | the `k` most likely tokens | Simple, but `k` is fixed: too many when the model is sure, too few when many words fit. |
| **top-p** (nucleus) | the smallest set of top tokens whose probabilities add up to at least `p` | Adapts: when the model is sure, one or two tokens pass; when it's unsure, many do. |
| **min-p** | tokens with at least `min_p × (top probability)` | Scales the cut with how confident the model is. Popular for local models. |

Example with `p = 0.9`:

```
" Paris" 0.60  " Lyon" 0.25  " Nice" 0.10  " a" 0.04  " the" 0.01
cumulative:  0.60   0.85   0.95  → stop, 0.95 ≥ 0.9
kept: Paris, Lyon, Nice → renormalized: 0.63, 0.26, 0.11
```

LM Studio shows Top K, Top P, Min P and Repeat Penalty in the sampling settings (names and defaults vary between versions, so check your sidebar). llama.cpp applies the samplers as a chain, and temperature is part of that chain. If a model card recommends values, start with those.

## 🔬 Renormalize, with numbers

"Renormalize" means: divide every kept probability by the total of the kept ones, so they add up to 1 again.

Kept: Paris 0.60, Lyon 0.25, Nice 0.10. Their total is 0.60 + 0.25 + 0.10 = **0.95**.

- Paris: 0.60 ÷ 0.95 = **0.63**
- Lyon: 0.25 ÷ 0.95 = **0.26**
- Nice: 0.10 ÷ 0.95 = **0.11**

0.63 + 0.26 + 0.11 = 1. The order and the ratios stay the same, only the scale changes. The `renormalize` helper in the starter does this for you.

`≥` (in Python `>=`) means "is more than **or equal to**": 0.95 ≥ 0.9 is true, and 0.9 ≥ 0.9 is true too.

## 🐍 Python you need

The starter gives you `rank(probs)`: it turns `{token: probability}` into a list of `(token, probability)` pairs, most likely first. You don't need to change it.

```python
rank({" a": 0.1, " Paris": 0.6})   # [(" Paris", 0.6), (" a", 0.1)]
```

| You write | Say it | What it does |
|---|---|---|
| `ranked[:2]` | "ranked up to 2" | a **slice**: the first 2 items of the list |
| `for token, q in ranked:` | "for each token and q in ranked" | each item is a pair. Python unpacks it: the first value goes into `token`, the second into `q`. |
| `kept = {}` | | a new, empty dictionary |
| `kept[token] = q` | "kept at token becomes q" | adds the pair to the dictionary |
| `running = running + q` | | a running total |
| `running >= p` | "running is at least p" | `>=` is "more than or equal to" |
| `break` | | stops the loop right now |

### 👀 Worked example: fill a bag up to a weight

Items sorted heaviest first. Keep putting them in until the bag weighs at least 5 kg:

```python
items = [("melon", 3), ("milk", 1), ("bread", 1), ("apple", 0.2)]
bag = {}
weight = 0
for name, kg in items:
    bag[name] = kg
    weight = weight + kg
    if weight >= 5:
        break
print(bag)   # {'melon': 3, 'milk': 1, 'bread': 1}
```

1. melon: bag has melon, weight 3. 3 ≥ 5? No.
2. milk: weight 4. No.
3. bread: weight 5. 5 ≥ 5? **Yes** → `break`. The apple never goes in.

Notice the order inside the loop: put it in the bag **first**, then check. That way the item that crosses the line is kept too. `top_p` works exactly like this.

## 🎯 Your quest

Both functions return a **new dictionary** with only the kept tokens, renormalized. `rank` and `renormalize` are given, and the `return renormalize(kept)` lines are there.

**Part 1:** `top_k(probs, k)`: keep the `k` most likely. Replace the comment with:

1. `for token, q in ranked[:k]:`
2. `    kept[token] = q`

**Part 2:** `top_p(probs, p)`: worked example's bag. Replace the comment with:

1. `for token, q in ranked:`
2. `    kept[token] = q`
3. `    running = running + q`
4. `    if running >= p:`
5. `        break`

## Review

<details><summary>What does temperature do to the logits?</summary>Divides them by T before softmax. T below 1 sharpens the distribution, above 1 flattens it.</details>
<details><summary>Where does the randomness in a reply come from?</summary>The sampler, which draws the next token at random according to the probabilities. The model itself is deterministic.</details>
<details><summary>Kept: 0.5 and 0.3. What are they after renormalizing?</summary>Total 0.8. 0.5 ÷ 0.8 = 0.625 and 0.3 ÷ 0.8 = 0.375.</details>
