---
title: Probability distributions and sampling
xp: 40
---
# The language of next-token prediction

> **Warm-up:** a die is fair. What's the *average* roll over many throws? Is that a number you can actually roll?

A **probability distribution** assigns each possible outcome a probability ≥ 0, all adding up to 1. An LLM's output for the next position is a **categorical distribution** over its whole vocabulary.

Two numbers summarize a distribution of numeric outcomes:

```
expected value  E[X]   = Σ pᵢ · xᵢ                   the long-run average (3.5 for a die)
variance        Var[X] = Σ pᵢ · (xᵢ − E[X])²         how spread out it is
standard deviation     = √Var[X]
```

**Sampling** from a categorical distribution, the way a sampler picks a token: take a uniform random number `r` between 0 and 1 and walk the **cumulative** probabilities until the running total exceeds `r`:

```
tokens:      A     B     C
probs:      0.5   0.3   0.2
cumulative: 0.5   0.8   1.0
r = 0.65 → passes A (0.5), stops at B (0.8) → B
```

Each token wins exactly as often as its probability, because its slice of the 0–1 line is exactly that wide. (This is called **inverse transform sampling**.)

The **law of large numbers**: averages over many samples approach the expected value. It's why you need many evaluation prompts before trusting a result (lesson 11), and why a model's output varies run to run but its *behaviour* is stable.

Two more ideas you'll meet constantly: **conditional probability** `P(A | B)`, "probability of A given B" (a language model *is* `P(next token | previous tokens)`), and the **chain rule**, `P(A and B) = P(A) · P(B | A)`. That's how LLMs 1 multiplied token probabilities: P("the cat sat") = P(the) · P(cat | the) · P(sat | the cat). Each factor is *conditional* on the tokens before it, which is exactly what the model predicts. Only when two events are **independent** (B doesn't care about A, like two coin flips) does it shrink to `P(A)·P(B)`. Tokens in a sentence are not independent.

## Your quest

1. `expected_value(values, probs)` and `variance(values, probs)`.
2. `sample(probs, r)`: given a list of probabilities and a number `r` in [0, 1), return the **index** chosen by walking the cumulative sum. If floating-point rounding makes you run off the end, return the last index.

The program then samples 10,000 times and compares the frequencies with the probabilities.

## Review

<details><summary>What is the gradient of softmax + cross-entropy with respect to the logits?</summary>p − y: the probabilities minus the one-hot vector of the true token.</details>
<details><summary>State the chain rule.</summary>The derivative of f(g(x)) is f'(g(x)) · g'(x).</details>
