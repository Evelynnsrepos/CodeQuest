---
title: Logarithms
xp: 50
---
# "What power do I need?"

> **Warm-up:** 2 to what power gives 8? 10 to what power gives 1,000,000?

**In one sentence:** a logarithm answers "what exponent turns the base into this number?", and it turns multiplication into addition.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `log_b(x)` | "log base b of x" | the power p with `bᵖ = x` | `math.log(x, b)` |
| `log₂(x)` | "log base two of x" | in bits | `math.log2(x)` |
| `log₁₀(x)` | "log base ten" | number of digits, roughly | `math.log10(x)` |
| `ln(x)` | "L N of x" / "natural log" | log base e (lesson 11) | `math.log(x)` |
| `log(x)` | "log x" | in AI papers almost always **ln** | `math.log(x)` |

## The idea

`log₂(8) = 3` because `2³ = 8`. A logarithm **undoes** an exponent: `log_b(bᵖ) = p`.

The rules, all from the exponent rules in lesson 5:

| Rule | In words |
|---|---|
| `log(a · b) = log(a) + log(b)` | **products become sums** |
| `log(a / b) = log(a) − log(b)` | divisions become differences |
| `log(aⁿ) = n · log(a)` | powers become multiplications |
| `log(1) = 0` | because `b⁰ = 1` |
| `log(x) < 0` when `0 < x < 1` | probabilities have negative logs |
| `log(0)` | undefined (it goes to −∞) |

Changing base: `log_b(x) = ln(x) / ln(b)`.

## 🗣️ Say it out loud

`log P(text) = Σₜ log P(tokenₜ)` → "the log of the text's probability is the sum of the logs of each token's probability."

## 🧮 Worked example

The sentence from lesson 9: `0.1 · 0.05 · 0.2 = 0.001`.

With logs (base 10, to make it easy): `log(0.1) + log(0.05) + log(0.2) = −1 + (−1.301) + (−0.699) = −3`. And `10⁻³ = 0.001`. Same answer, but by **adding** numbers of normal size instead of multiplying ever-tinier ones.

## 🤖 Where AI uses it

- **Log-probabilities**: LLMs work with `log p` to avoid numbers too tiny for the computer.
- **The loss**: cross-entropy is `−log p(correct token)` (Math 5).
- **Bits**: `log₂(vocabulary size)` = bits needed to pick one token: `log₂(128000) ≈ 17`.
- **Perplexity**, scaling-law plots (log-log axes), learning-rate searches on a log scale.

## 🎯 Your quest

1. `log_base(x, b)`: using only `math.log` (natural log) and the change-of-base rule.
2. `bits_needed(n)`: the whole number of bits needed for `n` different values (`log₂ n`, rounded **up**: use `math.ceil`).
3. `log_prob(ps)`: the sum of the natural logs of a list of probabilities.

**Remember:** logs turn multiplying into adding, which is why every LLM loss is written with a log.

## Review

<details><summary>What is 4!?</summary>24.</details>
<details><summary>Why does a product of many probabilities cause trouble on a computer?</summary>It gets so tiny that it rounds to 0.</details>
