---
title: AND, OR and independent events
xp: 45
---
# Combining chances

> **Warm-up:** an AI agent finishes each step correctly 95% of the time. A task needs 20 steps. What's the chance it gets **all 20** right? Guess first.

**In one sentence:** for independent events, "both happen" multiplies the chances, "at least one happens" adds them but subtracts the overlap.

## 🪜 Plain words

**Independent** = one doesn't affect the other (two coin flips).

- **AND** (both happen): multiply. Each extra requirement can only make it **less** likely.
- **OR** (at least one happens): add, but things that are both got counted twice, so take the overlap off once.
- **At least one in n tries**: easier the other way round: 1 minus "it never happens".

## 🪜 With numbers

- Two coins both heads: 0.5 × 0.5 = **0.25**.
- Agent, 20 steps at 95%: 0.95²⁰ = **0.358**. Only about 1 in 3 tasks succeed! (Warm-up answer.)
- A card is a heart OR a king: 13/52 + 4/52 − 1/52 (king of hearts counted twice) = 16/52 ≈ **0.308**.
- A tool fails 5% of the time. In 10 calls, at least one failure: 1 − 0.95¹⁰ = **0.401**.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `A ∩ B` or `A, B` | "A and B" / "A intersect B" | both happen | `a and b` |
| `A ∪ B` | "A or B" / "A union B" | at least one happens | `a or b` |
| `P(A ∩ B)` | "P of A and B" | chance of both | |
| `⊥` | "is independent of" | doesn't affect | |
| `ⁿ` | "to the n" | multiply by itself n times | `p ** n` |

## 🔬 Take the formulas apart

<div class="formula"><span class="k1">P(A ∩ B)</span> = <span class="k2">P(A)</span> · <span class="k3">P(B)</span> &nbsp;(only if independent)</div>

<div class="formula"><span class="k4">P(A ∪ B)</span> = <span class="k2">P(A)</span> + <span class="k3">P(B)</span> − <span class="k1">P(A ∩ B)</span></div>

| Piece | Say it | Means | Heart or king |
|---|---|---|---|
| <span class="k2">P(A)</span> | "P of A" | heart | 13/52 |
| <span class="k3">P(B)</span> | "P of B" | king | 4/52 |
| − <span class="k1">P(A ∩ B)</span> | "minus P of A and B" | the overlap, counted twice → remove once | 1/52 |
| <span class="k4">P(A ∪ B)</span> | "P of A or B" | at least one | 16/52 |

<div class="formula">P(at least one in <span class="k5">n</span>) = 1 − ( 1 − <span class="k6">p</span> )<sup><span class="k5">n</span></sup></div>

| Piece | Means | Tool example |
|---|---|---|
| 1 − <span class="k6">p</span> | chance it does **not** happen once | 0.95 |
| ( … )<sup><span class="k5">n</span></sup> | never happens in n independent tries | 0.95¹⁰ = 0.599 |
| 1 − ( … ) | flip: at least once | 0.401 |

## 🔀 What if it were different?

<div class="wrong"><b>OR without subtracting the overlap</b>: 17/52 ≈ 0.327. With big overlaps this can even go above 1 (P(even) + P(≥ 2) on a die = 0.5 + 0.833 = 1.33).</div>
<div class="wrong"><b>AND by adding</b>: 0.95 + 0.95 + … is bigger than 1 after 2 steps. AND can never be more likely than either part alone.</div>
<div class="wrong"><b>At least one = n · p</b>: 10 · 0.05 = 0.5, and with 30 calls 1.5 (impossible). It's only roughly right when n · p is small.</div>
<div class="wrong"><b>Multiply events that aren't independent</b>: "it's cloudy" and "it rains" aren't independent; multiplying 0.4 × 0.3 gives 0.12, but nearly all rain comes with clouds, so it's really close to 0.3.</div>
<div class="right">AND: multiply (independent). OR: add, minus overlap. At least one: 1 − (1 − p)ⁿ ✓</div>

## 🗣️ Say it out loud

"P of A or B equals P of A plus P of B minus P of A and B."

## 🤖 Where AI uses it

Agent reliability (LLMs 3): long chains of steps fail a lot unless each step is very reliable, which is why agents verify and retry. **pass@k** (LLMs 8) is "at least one of k samples is correct": 1 − (1 − p)ᵏ.

## 🎯 Your quest

1. `p_and(pa, pb)`: independent AND.
2. `p_or(pa, pb, pab)`: OR with overlap `pab`.
3. `p_all(p, n)`: n independent successes in a row.
4. `p_at_least_one(p, n)`.

**Remember:** AND multiplies, OR adds minus the overlap, "at least one" = 1 − "never".

## Review

<details><summary>P(not A)?</summary>1 − P(A).</details>
<details><summary>P(3) on a die?</summary>1/6.</details>
