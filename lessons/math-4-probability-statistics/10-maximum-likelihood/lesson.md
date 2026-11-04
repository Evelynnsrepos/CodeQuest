---
title: Maximum likelihood: the idea behind every loss
xp: 60
---
# Pick the settings that make your data least surprising

> **Warm-up:** a coin lands heads 7 times out of 10. If you had to guess the coin's true chance of heads, what would you guess? Why that number?

**In one sentence:** maximum likelihood picks the model settings under which the data you actually saw was most probable, and minimising the negative log of that probability is exactly the loss LLMs train on.

## 🪜 Plain words

Try different guesses for the coin's heads-chance p and ask: "If p were this, how likely would **my exact flips** have been?" That "how likely" is the **likelihood**. The best guess is the p with the highest likelihood.

Likelihoods are products of many small numbers (lesson 02), which get impossibly tiny. So we take the **log**: products become sums (Math 1 lesson 14), and the best p stays the same. Flip the sign so smaller = better, and you have a **loss**: the **negative log-likelihood**.

## 🪜 With numbers

Flips: 7 heads (1), 3 tails (0).

| guess p | likelihood p⁷ · (1 − p)³ | log-likelihood |
|---|---|---|
| 0.5 | 0.000977 | −6.93 |
| 0.7 | **0.002224** | **−6.11** |
| 0.9 | 0.000478 | −7.65 |

p = 0.7 wins, matching your gut: 7 out of 10.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `L(θ)` | "the likelihood of theta" | P(the data \| settings θ) | |
| `θ` | "theta" | the settings / weights | `p` |
| `Π` | "product" | multiply all (Math 1) | `math.prod` |
| `log` | "log" (natural log, ln) | turns × into + | `math.log` |
| `argmax` | "arg max" | **which** θ gives the biggest value (not the value itself) | `max(grid, key=...)` |
| `NLL` | "negative log-likelihood" | −log L: the loss | |
| `θ̂` | "theta hat" | the best estimate (a hat = "estimated") | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">θ̂</span> = <span class="k2">argmax<sub>θ</sub></span> <span class="k3">Σ<sub>i</sub></span> <span class="k4">log</span> <span class="k5">p<sub>θ</sub>(xᵢ)</span></div>

| Piece | Say it | Means | Coin |
|---|---|---|---|
| <span class="k5">p<sub>θ</sub>(xᵢ)</span> | "p theta of x i" | probability of data point i under settings θ | p for heads, 1 − p for tails |
| <span class="k4">log</span> | "log" | turn tiny probabilities into manageable negatives | log 0.7 = −0.357 |
| <span class="k3">Σ<sub>i</sub></span> | "sum over i" | add over all data points (instead of multiplying) | −6.11 |
| <span class="k2">argmax<sub>θ</sub></span> | "arg max over theta" | the θ with the biggest total | |
| <span class="k1">θ̂</span> | "theta hat" | our best estimate | 0.7 |

For an LLM, the data points are tokens and p<sub>θ</sub> is the model's probability for the right next token. Average the **negative** sum per token and you get the **cross-entropy loss** (Math 5).

## 🔀 What if it were different?

<div class="wrong"><b>Multiply instead of summing logs</b>: 1000 tokens each with p = 0.1: 0.1¹⁰⁰⁰ is 0.0 in Python (underflow). Every model looks equally terrible and you can't compare or train.</div>
<div class="wrong"><b>Forget the minus sign on the loss</b>: minimising +log-likelihood pushes the right answer's probability <b>down</b>. The model learns to be wrong.</div>
<div class="wrong"><b>argmax vs max</b>: max gives the best likelihood (0.002224), argmax gives the best setting (0.7). You wanted the setting.</div>
<div class="right">best p = 0.7, loss = −Σ log p = 6.11 (0.611 per flip) ✓</div>

## 🗣️ Say it out loud

"Theta hat is the arg max over theta of the sum of log p theta of x i."

## 🤖 Where AI uses it

Pre-training an LLM **is** maximum likelihood on internet text. The "loss: 2.1" in a training log is the average negative log-likelihood per token. Perplexity (LLMs 1) is e to that number.

## 🎯 Your quest

Flips are lists of 1 (heads) and 0 (tails).

1. `likelihood(p, flips)`.
2. `log_likelihood(p, flips)`: sum of logs (never multiply first!).
3. `best_p(flips)`: try p = 0.01, 0.02, …, 0.99 and return the one with the biggest log-likelihood.
4. `nll_per_token(probs)`: average of −log p over a list of correct-token probabilities.

**Remember:** likelihood = how probable your data is; loss = −log of it, averaged.

## Review

<details><summary>SE for σ = 2, n = 400?</summary>2 / 20 = 0.1.</details>
<details><summary>Data needed to halve the error?</summary>4×.</details>
