---
title: Top-k, top-p and min-p
xp: 30
---
# Cutting off the long tail

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

## Python you need

This sorts a `{token: probability}` dictionary into a list of `(token, probability)` pairs, most likely first:

```python
ranked = sorted(probs.items(), key=lambda pair: pair[1], reverse=True)
```

`ranked[:k]` is the first `k` items. `for token, p in ranked:` walks the pairs.

## Your quest

Both functions take a `{token: probability}` dictionary and return a **new dictionary** with only the kept tokens, renormalized so they add up to 1. Use the `renormalize` helper.

1. `top_k(probs, k)`: keep the `k` most likely.
2. `top_p(probs, p)`: walk the ranked list adding probabilities, keep each token, and stop as soon as the running total is at least `p`.

## Review

<details><summary>What does temperature do to the logits?</summary>Divides them by T before softmax. T below 1 sharpens the distribution, above 1 flattens it.</details>
<details><summary>Where does the randomness in a reply come from?</summary>The sampler, which draws the next token at random according to the probabilities. The model itself is deterministic.</details>
