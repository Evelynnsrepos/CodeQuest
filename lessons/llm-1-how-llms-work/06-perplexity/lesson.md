---
title: How sure is the model? Log-probs and perplexity
minutes: 40
xp: 30
hint: total_log_prob: total = 0, then for p in probs: and inside it total = total + math.log(p), then return total
hint: perplexity, step 1: average = total_log_prob(probs) / len(probs)
hint: perplexity, step 2: return math.exp(-average)
---
# The probability of a whole text

⏱️ About 40 minutes

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

## 🔬 Take the symbols apart

**`P("The")`** (say "P of The"): the **probability** of "The", a number from 0 (never) to 1 (certain). 0.10 means 10%.

**`P(" cat" | "The")`** (say "P of cat, given The"): the vertical line `|` means **"given that"**. It's the probability of " cat" coming next, when "The" is already there. That's exactly what a language model outputs.

**`·`** means times. Multiplying probabilities gives the chance that **all** of them happen: 50% and then 50% is 0.5 · 0.5 = 0.25, a 25% chance.

**`log`** (say "log", short for logarithm) is the opposite of `e^`. If e^z = x, then log(x) = z. It answers: "e to the power of **what** gives x?"

| x | log(x) | why |
|---|---|---|
| 1 | 0 | e^0 = 1 |
| 0.8 | −0.22 | a little below 1 → a little below 0 |
| 0.5 | −0.69 | |
| 0.1 | −2.30 | small probability → big negative number |
| 0.02 | −3.91 | |

Probabilities are between 0 and 1, so their logs are always **0 or negative**. The useful rule: **log(a · b) = log(a) + log(b)**. Multiplying turns into adding. Adding hundreds of numbers like −2.3 is safe; multiplying hundreds of numbers like 0.02 gives a number so tiny the computer rounds it to 0.

Now the three formulas, built on each other:

<div class="formula"><span class="k1">log P(text)</span> = <span class="k2">log p₁ + log p₂ + … + log pₙ</span></div>
<div class="formula"><span class="k3">cross-entropy</span> = <span class="k4">−</span>(<span class="k1">log P(text)</span>) <span class="k5">÷ n</span></div>
<div class="formula"><span class="k6">perplexity</span> = e^<span class="k3">cross-entropy</span></div>

| Piece | Say it | Means | Example "unsure": four tokens, each p = 0.25 |
|---|---|---|---|
| <span class="k2">log p₁ + … + log pₙ</span> | "the sum of the logs" | the log of each probability, added up | 4 × (−1.39) = **−5.55** |
| <span class="k1">log P(text)</span> | "log P of the text" | the result: one number for the whole text | −5.55 |
| <span class="k4">−</span> | "minus" | flip the sign, so the number is positive | 5.55 |
| <span class="k5">÷ n</span> | "divided by n" | n = the number of tokens. Makes it an **average per token**, so long and short texts compare fairly | 5.55 ÷ 4 = **1.39** |
| <span class="k3">cross-entropy</span> | | "how surprised was the model, on average?" Lower is better. | 1.39 |
| <span class="k6">perplexity</span> | | e^1.39 = **4.0**: as unsure as picking 1 of 4 at random | 4.0 |

Same steps for "confident" (each p = 0.8): sum = 4 × (−0.22) = −0.89, flip and average: 0.22, e^0.22 = **1.25**. Almost certain.

## 🔀 What if it were different?

<div class="wrong"><b>Forget the minus</b>: the cross-entropy would be −1.39, and e^−1.39 = 0.25. "Perplexity 0.25" means nothing: you can't be unsure between a quarter of a choice.</div>
<div class="wrong"><b>Forget ÷ n</b>: e^5.55 ≈ 256. A text 10 times longer would get a much bigger number, even if the model was just as good.</div>
<div class="right">Sum of logs, minus, divided by n, then e^ ✓</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `math.log(p)` | "log of p" | the natural logarithm (the opposite of `math.exp`) |
| `math.exp(x)` | "e to the x" | e^x |
| `total = total + math.log(p)` | | a running total of logs |
| `len(probs)` | "length of probs" | n, the number of tokens |
| `-average` | "minus average" | flips the sign: −(−1.39) = 1.39 |
| `total_log_prob(probs)` | | calls your first function from inside the second |

### 👀 Worked example: the average of a list, step by step

```python
def average_of_doubles(numbers):
    total = 0
    for x in numbers:
        total = total + x * 2
    return total / len(numbers)

print(average_of_doubles([1, 2, 3]))   # 4.0
```

1. `total` = 0, then 0 + 2 = 2, then 2 + 4 = 6, then 6 + 6 = 12.
2. 12 ÷ 3 numbers = **4.0**.

Your `total_log_prob` is the loop part with `math.log(p)` instead of `x * 2`. Your `perplexity` does the dividing, the minus and the `e^`.

## 🎯 Your quest

Each list holds the probabilities the model gave to the tokens that *actually came next*.

**Part 1:** `total_log_prob(probs)`. Replace `return 0` with:

1. `total = 0`
2. `for p in probs:`
3. `    total = total + math.log(p)`
4. `return total`

**Part 2:** `perplexity(probs)`. Replace `return 0` with:

1. `average = total_log_prob(probs) / len(probs)`
2. `return math.exp(-average)`

Expected output:

```
confident: 1.25
unsure: 4.0
```

## Review

<details><summary>Why subtract the largest logit inside softmax?</summary>To avoid overflow in math.exp. Subtracting the same number from every logit doesn't change the result, because it cancels out.</details>
<details><summary>What is a logit?</summary>The model's raw score for one candidate next token, before softmax turns all the scores into probabilities.</details>
<details><summary>What does "8B" mean?</summary>The model has about 8 billion parameters (weights).</details>
<details><summary>Why do log-probs add up, when probabilities multiply?</summary>Because log(a · b) = log(a) + log(b). Adding is also safe for long texts, where multiplying would round to 0.</details>
