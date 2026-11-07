---
title: Probability distributions and sampling
minutes: 60
xp: 40
hint: expected_value: total = 0, for i in range(len(values)): total = total + probs[i] * values[i], return total
hint: variance: mean = expected_value(values, probs), total = 0, then in the loop total = total + probs[i] * (values[i] - mean) ** 2
hint: sample: running = 0, for i in range(len(probs)): running = running + probs[i], and if r < running: return i
hint: After the loop in sample: return len(probs) - 1 (the last index)
---
# The language of next-token prediction

⏱️ About 60 minutes

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

## 🔬 Take the formulas apart

**The big Σ** <div class="formula"><span class="k1">Σ</span> <span class="k2">pᵢ · xᵢ</span></div>
`Σ` is the Greek capital letter sigma. It means "**add up**, for every i". So Σ pᵢ · xᵢ is p₁·x₁ + p₂·x₂ + p₃·x₃ + … In code, Σ is always a loop with a running total.

**Expected value** <div class="formula">E[X] = <span class="k1">Σ</span> <span class="k2">pᵢ</span> · <span class="k3">xᵢ</span></div>
- `X` is the random thing (a die roll). `E[X]` reads "expected value of X": the long-run average.
- <span class="k3">xᵢ</span>: each possible value. <span class="k2">pᵢ</span>: its probability.

Numbers: a game pays 0 € with probability 0.7 and 10 € with probability 0.3. E = 0.7 × 0 + 0.3 × 10 = **3 €**. You never win exactly 3 €, but over many games you average 3.

**Variance** <div class="formula">Var[X] = <span class="k1">Σ</span> <span class="k2">pᵢ</span> · <span class="k3">(xᵢ − E[X])²</span></div>
Read the inside first:
1. <span class="k3">xᵢ − E[X]</span>: how far is this value from the average?
2. <span class="k3">²</span>: square it, so "too low" and "too high" both count as positive.
3. <span class="k2">pᵢ</span> ·: weigh it by how often it happens, then <span class="k1">Σ</span> add up.

Same game, average 3: (0 − 3)² = 9 with p 0.7, (10 − 3)² = 49 with p 0.3. Var = 0.7 × 9 + 0.3 × 49 = 6.3 + 14.7 = **21**. The **standard deviation** is √21 ≈ 4.6: "a typical distance from the average".

For a fair die: E = (1 + 2 + 3 + 4 + 5 + 6) / 6 = **3.5**, Var ≈ **2.917**.

**Sampling with cumulative sums.** Lay the probabilities end to end on a line from 0 to 1:

```
|---- A 0.5 ----|-- B 0.3 --|- C 0.2 -|
0              0.5         0.8       1.0
```

Pick a random spot `r`. Whose stretch is it in? The running total tells you: keep adding until it's bigger than `r`.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `for i in range(len(values)):` | | positions 0, 1, … so you can use `values[i]` and `probs[i]` together |
| `total = total + probs[i] * values[i]` | | one term of the Σ |
| `(values[i] - mean) ** 2` | | the distance, squared. `**` is "to the power of". |
| `if r < running:` | "if r is less than running" | the spot `r` is inside this stretch |
| `return i` | | the **index** (position), not the probability |
| `len(probs) - 1` | | the last index. 3 items → indexes 0, 1, 2 → last is 2. |

`[1 / 6] * 6` in the given code makes a list of six `1/6`s. `10_000` is 10000; the `_` is only there for reading.

### 👀 Worked example: walking the line

probs = `[0.5, 0.3, 0.2]`, r = 0.65:

1. `i` = 0: running = 0.5. Is 0.65 < 0.5? No.
2. `i` = 1: running = 0.8. Is 0.65 < 0.8? Yes → `return 1` (B).

With r = 0.5: round 1, is 0.5 < 0.5? **No** (equal is not less), round 2, 0.5 < 0.8 → 1. So the line at exactly 0.5 belongs to B.

## 🎯 Your quest

`expected_value(values, probs)`: replace `return 0` with:

1. `    total = 0`
2. `    for i in range(len(values)):`
3. `        total = total + probs[i] * values[i]`
4. `    return total`

`variance(values, probs)`: replace `return 0` with:

1. `    mean = expected_value(values, probs)`
2. `    total = 0`
3. `    for i in range(len(values)):`
4. `        total = total + probs[i] * (values[i] - mean) ** 2`
5. `    return total`

`sample(probs, r)`: replace `return 0` with:

1. `    running = 0`
2. `    for i in range(len(probs)):`
3. `        running = running + probs[i]`
4. `        if r < running:`
5. `            return i`
6. `    return len(probs) - 1`

Line 6 is the safety net: if rounding makes the probabilities add up to 0.9999999, a very high `r` still gets the last token.

## Review

<details><summary>What is the gradient of softmax + cross-entropy with respect to the logits?</summary>p − y: the probabilities minus the one-hot vector of the true token.</details>
<details><summary>State the chain rule.</summary>The derivative of f(g(x)) is f'(g(x)) · g'(x).</details>
<details><summary>Values [2, 4] with probabilities [0.5, 0.5]: what's E[X]?</summary>0.5 × 2 + 0.5 × 4 = 1 + 2 = 3.</details>
