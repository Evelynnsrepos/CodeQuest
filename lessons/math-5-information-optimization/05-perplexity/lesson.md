---
title: Perplexity: loss you can picture
xp: 45
---
# "As confused as choosing between N options"

> **Warm-up:** your training log says loss 2.1. Is that good? What would you tell a friend it means?

**In one sentence:** perplexity is e to the power of the average cross-entropy loss: the number of equally likely options the model is, on average, as confused as.

## 🪜 Plain words

Loss in nats is hard to picture. Perplexity turns it back into a **count of choices**:

- Perplexity 1: the model is always sure and right.
- Perplexity 2: as unsure as a coin flip at every token.
- Perplexity 50,000: as unsure as picking a random word from the whole vocabulary.

Since loss = −log(probability), undoing the log with e gives back "1 over the typical probability".

## 🪜 With numbers

- Loss 2.1 nats → e^2.1 ≈ **8.2**. Like choosing between about 8 equally likely tokens.
- Correct-token probabilities 0.5 and 0.25 → losses 0.693 and 1.386 → average 1.04 → perplexity **2.83**.
- Uniform over 1000 tokens: loss ln 1000 = 6.91 → perplexity **1000**. Exactly the number of choices.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `PPL` | "perplexity" | | |
| `exp(x)` | "e to the x" | undoes ln (Math 1) | `math.exp(x)` |
| `1/N Σ` | "one over N, sum" | average over N tokens | `sum(...) / N` |
| `−log q(xₜ \| x_<t)` | "minus log q of x t given the earlier tokens" | per-token loss (lesson 03, Math 4 lesson 03) | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">PPL</span> = <span class="k2">exp</span>( <span class="k3">1/N Σₜ</span> <span class="k4">− log q(xₜ | x_&lt;t)</span> )</div>

| Piece | Say it | Means | probs 0.5, 0.25 |
|---|---|---|---|
| <span class="k4">− log q(…)</span> | "minus log q" | each token's loss | 0.693, 1.386 |
| <span class="k3">1/N Σₜ</span> | "one over N, sum over t" | average loss | 1.040 |
| <span class="k2">exp</span>( ) | "e to the" | undo the log | |
| <span class="k1">PPL</span> | "perplexity" | effective number of choices | 2.83 |

## 🔀 What if it were different?

<div class="wrong"><b>Average the probabilities, then 1/that</b>: average p = 0.375 → 2.67. Ignores that one very bad token (p = 0.001) should hurt a lot; the log-average punishes it properly.</div>
<div class="wrong"><b>exp of the summed (not averaged) loss</b>: e^2.08 = 8.0 for 2 tokens, and it would keep growing with text length. You couldn't compare a short and a long document.</div>
<div class="wrong"><b>Mix bases</b>: loss in nats but 2^loss: 2^2.1 = 4.3 instead of 8.2. Use e with nats, 2 with bits.</div>
<div class="right">exp(1.040) = 2.83; exp(2.1) = 8.2 ✓</div>

## 🗣️ Say it out loud

"Perplexity is e to the average negative log-likelihood per token."

## 🤖 Where AI uses it

Comparing language models and quantised versions of the same model (LLMs 2): if quantising raises perplexity from 5.80 to 5.85, little was lost. Perplexity is only comparable between models with the **same tokenizer**.

## 🎯 Your quest

1. `perplexity(probs)`: from the list of correct-token probabilities.
2. `ppl_from_loss(loss)`.
3. `loss_from_ppl(ppl)`.

**Remember:** perplexity = e^loss = "as confused as choosing among this many".

## Review

<details><summary>KL(p ‖ p)?</summary>0.</details>
<details><summary>Is KL symmetric?</summary>No.</details>
