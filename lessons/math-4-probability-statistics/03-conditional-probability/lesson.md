---
title: P(A | B): probability given something
xp: 50
---
# Zooming into a smaller world

> **Warm-up:** of 100 emails, 30 contain the word "free", and 24 of those 30 are spam. If an email contains "free", how likely is it spam?

**In one sentence:** `P(A | B)` is the chance of A **when you already know B happened**: you zoom into the B-world and ask what share of it is also A.

## 🪜 Plain words

Knowing something changes the odds. Once you know the email says "free", you ignore the other 70 emails completely. Your new "all outcomes" is just those 30.

So: count the ones that are **both**, divide by the size of the world you zoomed into.

## 🪜 With numbers

- P(spam | "free") = 24 ÷ 30 = **0.8**.
- In probabilities: P(spam and "free") = 24/100 = 0.24, P("free") = 30/100 = 0.3. 0.24 ÷ 0.3 = **0.8** ✓.
- The other way round, P("free" | spam): if 40 emails are spam in total, 24 ÷ 40 = **0.6**. Different number!

An LLM is a conditional-probability machine: P(next token | all previous tokens).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `\|` (inside P) | "given" | "knowing that…" (not absolute value, not "or"!) | |
| `P(A \| B)` | "P of A given B" | chance of A inside the B-world | `both / b` |
| `P(A ∩ B)` | "P of A and B" | both happen (lesson 02) | |
| `P(x₁, …, xₙ)` | "P of x one to x n" | all of them together | |
| `Π` | "product" (capital pi) | multiply a list (Math 1) | `math.prod` |
| `x_<t` | "x before t" | all tokens before position t | `tokens[:t]` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">P(A | B)</span> = <span class="k2">P(A ∩ B)</span> / <span class="k3">P(B)</span></div>

| Piece | Say it | Means | Spam example |
|---|---|---|---|
| <span class="k1">P(A \| B)</span> | "P of A given B" | what we want | 0.8 |
| <span class="k2">P(A ∩ B)</span> | "P of A and B" | both: spam **and** "free" | 0.24 |
| <span class="k3">P(B)</span> | "P of B" | the world we zoom into: "free" | 0.3 |

Turn it around and you get the **chain rule of probability**, which is how an LLM scores a whole sentence:

<div class="formula">P(<span class="k4">x₁ … xₙ</span>) = <span class="k5">Π</span> P( <span class="k6">xₜ</span> | <span class="k4">x_&lt;t</span> )</div>

| Piece | Means | "the cat sat" |
|---|---|---|
| <span class="k6">xₜ</span> | the token at position t | "cat" |
| <span class="k4">x_&lt;t</span> | everything before it | "the" |
| <span class="k5">Π</span> | multiply them all | 0.05 · 0.02 · 0.3 = 0.0003 |

## 🔀 What if it were different?

<div class="wrong"><b>Divide by P(A) instead of P(B)</b>: 0.24 / 0.4 = 0.6. That's P("free" | spam): the question backwards. Mixing these up is the most common probability mistake in the world (next lesson).</div>
<div class="wrong"><b>Forget to divide</b>: 0.24. That's "spam AND free" out of all emails, not "spam among free emails".</div>
<div class="wrong"><b>Multiply unconditional token probabilities</b> (each token's overall frequency): "sat" is rare overall, but very likely after "the cat". You'd score natural sentences as very unlikely.</div>
<div class="right">P(spam | free) = 0.24 / 0.3 = 0.8 ✓</div>

## 🗣️ Say it out loud

"P of A given B equals P of A and B over P of B."

## 🤖 Where AI uses it

The training objective of every LLM: maximise P(xₜ | x_&lt;t) for every position. Perplexity (LLMs 1) and log-probabilities (Math 5) are built on this product.

## 🎯 Your quest

1. `conditional(p_ab, p_b)`.
2. `from_counts(both, b_count)`: the same from counts.
3. `sequence_prob(cond_probs)`: multiply a list of conditional probabilities (empty → 1).

**Remember:** "given B" = zoom into B, then ask what share is A.

## Review

<details><summary>P(A and B) for independent events?</summary>P(A) · P(B).</details>
<details><summary>At least one success in n tries?</summary>1 − (1 − p)ⁿ.</details>
