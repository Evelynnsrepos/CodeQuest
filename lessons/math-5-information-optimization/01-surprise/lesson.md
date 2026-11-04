---
title: Surprise: −log p
xp: 40
---
# Rare things are surprising

> **Warm-up:** which is more surprising: a coin landing heads, or rolling a 6, or winning a 1-in-1000 raffle? Can you rank them, and say **how much** more surprising?

**In one sentence:** the surprise (information) of an event is −log of its probability: certain things carry 0 surprise, rare things carry a lot.

## 🪜 Plain words

Information theory measures **surprise** with a number:

- Something certain (p = 1) tells you nothing new: surprise **0**.
- Something that had a 50/50 chance: surprise **1 bit** (one yes/no question's worth).
- Every time the chance **halves**, the surprise goes up by **1 bit**.

The log does exactly that: it turns "halving" into "add one" (Math 1 lesson 14). The minus sign makes it positive, because logs of numbers below 1 are negative.

## 🪜 With numbers

| event | p | surprise in bits (log base 2) |
|---|---|---|
| sun rises | 1 | 0 |
| coin heads | 0.5 | **1** |
| roll a 6 | 1/6 | **2.58** |
| 1-in-1000 raffle | 0.001 | **9.97** |

With natural log (ln) the unit is called a **nat**: coin = 0.693 nats. ML code uses nats, because `math.log` is ln.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `I(x)` | "the information of x" | surprise of outcome x | |
| `−log p` | "minus log p" | the surprise formula | `-math.log(p)` |
| `log₂` | "log base two" | answer in **bits** | `math.log2(p)` |
| `ln` / `log` | "natural log" | answer in **nats** (ML default) | `math.log(p)` |
| `bit` | | 1 yes/no question | |
| `nat` | | ≈ 1.44 bits | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">I(x)</span> = <span class="k2">−</span> <span class="k3">log₂</span> <span class="k4">p(x)</span></div>

| Piece | Say it | Means | Roll a 6 |
|---|---|---|---|
| <span class="k4">p(x)</span> | "p of x" | the event's probability | 1/6 |
| <span class="k3">log₂</span> | "log base two" | "2 to the what gives this?" | log₂(1/6) = −2.58 |
| <span class="k2">−</span> | "minus" | flip to positive | 2.58 |
| <span class="k1">I(x)</span> | "information of x" | surprise in bits | 2.58 |

## 🔀 What if it were different?

<div class="wrong"><b>Surprise = 1 − p</b>: raffle 0.999, coin 0.5. Rare things barely count more than common ones, and two independent coins (p = 0.25) would give 0.75, not 1 + 1 = 2. With logs, surprises of independent events <b>add up</b>.</div>
<div class="wrong"><b>Forget the minus</b>: −1 bit for a coin. Negative surprise makes no sense, and minimising it would push probabilities of correct answers <i>down</i>.</div>
<div class="wrong"><b>p = 0</b>: −log 0 = ∞. An event the model called impossible that then happens is infinitely surprising: that's why models never output exact zeros.</div>
<div class="right">coin 1 bit, die 2.58 bits, raffle 9.97 bits ✓</div>

## 🗣️ Say it out loud

"The information of x is minus log of p of x."

## 🤖 Where AI uses it

The training loss of an LLM is the model's average surprise at the real next token (lesson 03). Lower surprise = better prediction. A loss of 2.3 nats per token means the model is about as surprised as picking 1 of 10 equally likely options.

## 🎯 Your quest

1. `surprise_bits(p)`.
2. `surprise_nats(p)`.
3. `joint_surprise(ps)`: surprise in bits of several independent events all happening (add them, or use the product's probability: both work).

**Remember:** surprise = −log p; halve the chance, add one bit.

## Review

<details><summary>p-value meaning?</summary>Chance of a result at least this extreme if nothing special were happening.</details>
<details><summary>Why sum log-probabilities?</summary>Multiplying many small numbers underflows to 0.</details>
