---
title: How sure is the model? Log-probs and perplexity
xp: 30
---
# The probability of a whole text

> **Warm-up:** if a model gives the next token a 50% chance, and the token after that also 50%, how likely is the two-token sequence?

A model only ever predicts *one* next token. The probability of a whole text comes from the **chain rule of probability**: multiply the probability of each token given everything before it.

```
P("The cat sat") = P("The") · P(" cat" | "The") · P(" sat" | "The cat")
                 =  0.10    ·      0.02        ·        0.30         = 0.0006
```

Multiplying hundreds of small numbers quickly underflows to 0, so everyone works with **logarithms** instead. The log of a product is the sum of the logs:

```
log P(text) = log 0.10 + log 0.02 + log 0.30 = −2.30 − 3.91 − 1.20 = −7.42
```

These are **log-probs** (always ≤ 0, because probabilities are ≤ 1). Flip the sign and average over the tokens and you get the **cross-entropy**, the number training tries to make small (Module 5):

```
cross-entropy = −(sum of log-probs) / number of tokens
```

Finally, **perplexity** = `e^(cross-entropy)`. It has a lovely meaning: "the model was as unsure as if it were picking uniformly among this many tokens". A perplexity of 1 means it was certain and right every time. A perplexity of 4 means as unsure as a fair 4-sided die. Perplexity is the classic way to compare language models on the same text, and you will use it to evaluate your own fine-tune in the capstone.

## Python you need

`math.log(x)` is the natural logarithm (base e), the inverse of `math.exp`.

## Your quest

Each list holds the probabilities the model gave to the tokens that *actually came next*.

1. Write `total_log_prob(probs)`: the sum of `math.log(p)` for every `p`.
2. Write `perplexity(probs)`: `math.exp` of minus the average log-prob. Reuse `total_log_prob`.

Expected output:

```
confident: 1.25
unsure: 4.0
```

## Review

<details><summary>Why subtract the largest logit inside softmax?</summary>To avoid overflow in math.exp. Subtracting the same number from every logit doesn't change the result, because it cancels out.</details>
<details><summary>What is a logit?</summary>The model's raw score for one candidate next token, before softmax turns all the scores into probabilities.</details>
<details><summary>What does "8B" mean?</summary>The model has about 8 billion parameters (weights).</details>
