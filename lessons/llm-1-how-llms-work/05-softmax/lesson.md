---
title: Predicting the next token
minutes: 35
xp: 25
hint: Step 1: m = max(logits)
hint: Step 2: for z in logits: and inside it exps.append(math.exp(z - m))
hint: Step 3: total = sum(exps)
hint: Step 4: for e in exps: and inside it probs.append(e / total)
---
# Logits and softmax

⏱️ About 35 minutes

> **Warm-up:** what does the model output after reading your prompt: a word, a sentence, or something else?

An LLM is one giant function. It takes the token IDs so far and outputs **one score for every token in its vocabulary**, for the *next* position only. These raw scores are called **logits**. They can be any number, negative or positive; higher means "more likely next".

To turn logits into **probabilities** (all between 0 and 1, adding up to 1), the model applies **softmax**:

```
softmax(zᵢ) = e^zᵢ / (e^z₁ + e^z₂ + … + e^zₙ)
```

`e^z` (the exponential, `math.exp(z)` in Python) is always positive and grows fast, so the biggest logit gets the biggest share.

```
prompt: "The capital of France is"
token:     " Paris"  " Lyon"  " a"   " the"
logit:       9.1      5.2     4.0    3.5
softmax:     0.97     0.02    0.006  0.004
```

**A detail real code always handles:** `math.exp(1000)` overflows (it's far bigger than a float can hold). Softmax gives the same result if you subtract the same number from every logit, because the factor `e^(−m)` cancels out above and below the fraction line. So real implementations first subtract the **largest** logit: then the biggest exponent is `e^0 = 1` and nothing can overflow.

## 🔬 Take the formula apart

First, three pieces of maths you need, one at a time.

**1. Powers.** `2³` (say "2 to the power of 3") means 2 × 2 × 2 = 8: multiply 2 by itself 3 times. `10²` = 10 × 10 = 100. Any number to the power of 0 is **1**.

**2. The number e.** `e` is a special number, about **2.718**. Like π, it shows up everywhere in maths. `e^z` (say "e to the z") is e to the power of z:

| z | e^z | |
|---|---|---|
| −2 | 0.14 | negative powers give small numbers, but never below 0 |
| 0 | 1 | |
| 1 | 2.72 | |
| 2 | 7.39 | |
| 9.1 | 8,955 | grows very fast |

Two things make `e^z` perfect here: it's **always positive** (even for negative logits), and a slightly bigger logit gives a **much** bigger result. In Python: `math.exp(z)`.

**3. Subscripts and "…".** `z₁, z₂, …, zₙ` (say "z one, z two, up to z n") means "all the logits, numbered 1 to n". `zᵢ` (say "z i") is "the one we're looking at right now".

Now the formula:

<div class="formula">softmax(<span class="k1">zᵢ</span>) = <span class="k2">e^zᵢ</span> <span class="k3">/</span> <span class="k4">(e^z₁ + e^z₂ + … + e^zₙ)</span></div>

| Piece | Say it | Means | Example (Paris, logits 9.1, 5.2, 4.0, 3.5) |
|---|---|---|---|
| <span class="k1">zᵢ</span> | "z i" | the logit of one token | 9.1 for " Paris" |
| <span class="k2">e^zᵢ</span> | "e to the z i" | make it positive and spread it out | e^9.1 ≈ 8,955 |
| <span class="k3">/</span> | "divided by" | the fraction line: top ÷ bottom | |
| <span class="k4">(e^z₁ + … + e^zₙ)</span> | "the sum of all of them" | do the same for **every** logit and add them up | 8,955 + 181 + 55 + 33 ≈ 9,224 |

So P(" Paris") ≈ 8,955 ÷ 9,224 ≈ **0.97**. Every token gets "its part ÷ all parts", so all the answers add up to exactly 1.

**The overflow trick, with numbers.** Subtract the biggest logit (9.1) from every logit first: 0, −3.9, −5.1, −5.6. Then e^0 = 1, e^−3.9 ≈ 0.020, e^−5.1 ≈ 0.006, e^−5.6 ≈ 0.004. Sum ≈ 1.030. P(" Paris") = 1 ÷ 1.030 ≈ **0.97**. The same answer, with small, safe numbers.

## 🔀 What if it were different?

<div class="wrong"><b>Divide the logits by their sum, without e</b>: logits can be negative. With logits [2, −1], the sum is 1, and you'd get "probabilities" 2 and −1. A probability can't be negative.</div>
<div class="wrong"><b>Forget the bottom of the fraction</b>: e^9.1 alone is 8,955, not a probability at all.</div>
<div class="right">e^ of each logit, divided by the sum of all of them ✓</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `import math` | | loads Python's maths toolbox (already at the top) |
| `math.exp(z)` | "e to the z" | e^z |
| `max(logits)` | "max of logits" | the biggest number in the list |
| `sum(exps)` | "sum of exps" | all the numbers in the list added up |
| `for z in logits:` | "for each z in logits" | once per number |
| `exps.append(x)` | | adds `x` to the end of the list |

### 👀 Worked example: shares of a pizza bill

Same shape: build a list, add it up, divide each by the total.

```python
def shares(paid):
    total = sum(paid)
    parts = []
    for p in paid:
        parts.append(p / total)
    return parts

print(shares([6, 3, 1]))   # [0.6, 0.3, 0.1]
```

1. `total` = 6 + 3 + 1 = 10.
2. 6 / 10 = 0.6, then 3 / 10 = 0.3, then 1 / 10 = 0.1.
3. The shares add up to 1, just like probabilities.

Softmax is this, but each number goes through `math.exp(z - m)` first.

## 🎯 Your quest

Write `softmax(logits)`. The starter has the boxes ready. Make the function read:

1. `m = max(logits)` (change the `0`)
2. `exps = []`
3. `for z in logits:`
4. `    exps.append(math.exp(z - m))`
5. `total = sum(exps)` (change the `0`)
6. `probs = []`
7. `for e in exps:`
8. `    probs.append(e / total)`
9. `return probs`

The check also tries logits like `[1000, 1001]`, so step 1 matters: `math.exp(1000)` is too big for Python.

## Review

<details><summary>Roughly how many GB is a 14B model at 8 bits per weight?</summary>14 × 8 ÷ 8 = 14 GB, plus room for the context. It would not fit fully in 12 GB of VRAM.</details>
<details><summary>What does a single neuron compute?</summary>A weighted sum of its inputs plus a bias: x₁·w₁ + x₂·w₂ + … + b.</details>
<details><summary>What is e^0, and why does that help softmax?</summary>1. After subtracting the biggest logit, the biggest power is e^0 = 1, so nothing can overflow.</details>
