---
title: Predicting the next token
xp: 25
---
# Logits and softmax

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

## Python you need

`import math` then `math.exp(x)`. `max(numbers)` and `sum(numbers)` work on lists.

## Your quest

Write `softmax(logits)`. It takes a list of numbers and returns a list of probabilities in the same order.

1. Find the largest logit `m`.
2. Make a list of `math.exp(z - m)` for every logit `z`.
3. Divide every entry by the sum of that list.

The check also tries logits like `[1000, 1001]`, so step 1 matters.

## Review

<details><summary>Roughly how many GB is a 14B model at 8 bits per weight?</summary>14 × 8 ÷ 8 = 14 GB, plus room for the context. It would not fit fully in 12 GB of VRAM.</details>
<details><summary>What does a single neuron compute?</summary>A weighted sum of its inputs plus a bias: x₁·w₁ + x₂·w₂ + … + b.</details>
