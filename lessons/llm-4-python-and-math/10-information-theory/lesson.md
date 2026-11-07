---
title: Entropy, cross-entropy and KL divergence
minutes: 60
xp: 45
hint: entropy: total = 0, for pi in p: if pi > 0: total = total + pi * math.log(pi). Then return -total
hint: cross_entropy: same, but for i in range(len(p)): if p[i] > 0: total = total + p[i] * math.log(q[i])
hint: kl: return cross_entropy(p, q) - entropy(p)
---
# Measuring surprise

⏱️ About 60 minutes

> **Warm-up:** which is more surprising: a fair coin landing heads, or rolling a 6 on a die? Can you put a number on "surprise"?

Information theory (Claude Shannon, 1948) measures surprise as `−log p`: certain events (p = 1) carry 0 surprise, rare ones a lot. Averaging surprise over a distribution gives three quantities that run all of machine learning:

```
entropy        H(p)    = −Σ pᵢ log pᵢ          how uncertain p itself is
cross-entropy  H(p, q) = −Σ pᵢ log qᵢ          average surprise when reality follows p
                                               but you predicted q
KL divergence  KL(p‖q) = H(p, q) − H(p)        the *extra* surprise caused by predicting
                       = Σ pᵢ log (pᵢ / qᵢ)    q instead of the truth p (always ≥ 0)
```

With natural logs the unit is **nats**; with log base 2 it's **bits**. A fair coin has 1 bit of entropy.

Why you care:

- **The LLM loss *is* cross-entropy.** The "truth" for one position is one-hot (the actual next token), so `H(p, q) = −log q_true`, exactly the loss from LLMs 1. Training minimizes it, which is the same as minimizing KL from the data to the model.
- **Perplexity** = `e^(cross-entropy)`.
- **KL appears in fine-tuning**: RLHF and DPO (Module 6) keep the tuned model close to the original by penalizing `KL(tuned ‖ reference)`, so it learns preferences without forgetting how to talk. **Distillation** trains a small model to minimize KL to a big model's full distributions.
- **Sampling**: temperature raises or lowers the entropy of the next-token distribution.

`0 · log 0` is treated as 0 (outcomes that can't happen contribute nothing).

## 🔬 Take the formulas apart

**log** <div class="formula">log <span class="k1">x</span> asks: "e to the <b>what</b> gives <span class="k1">x</span>?"</div>
- Here `log` is the **natural log** (also written `ln`), with e ≈ 2.718 from lesson 8. Python: `math.log(x)`.
- log 1 = **0**, because e⁰ = 1.
- For numbers between 0 and 1 the answer is **negative**: log 0.5 ≈ −0.693 (e⁻⁰·⁶⁹³ ≈ 0.5), log 0.1 ≈ −2.303.
- log 0 doesn't exist (no power of e gives 0). Python raises an error, so you skip those terms.

**Surprise** <div class="formula">surprise = <span class="k2">−</span>log <span class="k1">p</span></div>
The minus flips the negative log into a positive number. p = 1 → surprise 0. p = 0.5 → 0.693. p = 0.1 → 2.303. Rarer = more surprising.

**Entropy** <div class="formula">H(p) = <span class="k2">−</span><span class="k3">Σ</span> <span class="k1">pᵢ</span> log <span class="k1">pᵢ</span></div>
The average surprise: each outcome's surprise, weighed by how often it happens. (Σ = "add up for every i", lesson 9.)

Numbers, loaded coin p = [0.9, 0.1]:
1. 0.9 × log 0.9 = 0.9 × (−0.105) = −0.095
2. 0.1 × log 0.1 = 0.1 × (−2.303) = −0.230
3. Add: −0.325. The minus in front: **H = 0.325 nats**. Divide by log 2 (0.693) to get bits: 0.47 bits. A fair coin has 1 bit: it's more uncertain.

**Cross-entropy** <div class="formula">H(p, q) = <span class="k2">−</span><span class="k3">Σ</span> <span class="k1">pᵢ</span> log <span class="k4">qᵢ</span></div>
Same, but the surprise comes from your **guess** <span class="k4">q</span>, while how often things happen comes from the truth <span class="k1">p</span>.

Numbers: truth [0, 1, 0] (the real token is 1), model guess [0.2, 0.7, 0.1].
1. i = 0: p = 0 → skip.
2. i = 1: 1 × log 0.7 = −0.357.
3. i = 2: p = 0 → skip.
4. H = **0.357**. That's −log 0.7: the LLM loss for that one position.

**KL divergence** <div class="formula">KL(p‖q) = <span class="k1">H(p, q)</span> − <span class="k2">H(p)</span></div>
`‖` is just a separator, read "KL of p from q". It's the **extra** surprise from guessing q instead of knowing p. Same distributions → 0. Never negative.

<div class="wrong">❌ KL(p‖q) and KL(q‖p) are the same.</div>
<div class="right">✅ They differ: the order matters. The program prints both so you can see.</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `math.log(0.5)` | "log of 0.5" | −0.693… |
| `if pi > 0:` | | only add the term when the probability isn't 0 |
| `return -total` | "return minus total" | flips the sign |
| `p[i]`, `q[i]` | | the matching entries of the two lists |

### 👀 Worked example: entropy of a three-sided spinner

```python
def spinner_entropy(p):
    total = 0
    for pi in p:
        if pi > 0:
            total = total + pi * math.log(pi)
    return -total

print(spinner_entropy([0.5, 0.5, 0.0]))
```

1. 0.5 × log 0.5 = −0.347. Twice: total = −0.693.
2. 0.0: skipped (no crash).
3. Returns **0.693** = log 2. The empty third side adds no uncertainty.

## 🎯 Your quest

`entropy(p)`: replace `return 0` with the worked example's body:

1. `    total = 0`
2. `    for pi in p:`
3. `        if pi > 0:`
4. `            total = total + pi * math.log(pi)`
5. `    return -total`

`cross_entropy(p, q)`: replace `return 0` with:

1. `    total = 0`
2. `    for i in range(len(p)):`
3. `        if p[i] > 0:`
4. `            total = total + p[i] * math.log(q[i])`
5. `    return -total`

`kl(p, q)`: replace `return 0` with `    return cross_entropy(p, q) - entropy(p)`

## Review

<details><summary>How does inverse transform sampling pick a token?</summary>Draw r uniformly in [0, 1) and walk the cumulative probabilities until the running total exceeds r.</details>
<details><summary>What does the law of large numbers say?</summary>The average over many samples approaches the expected value.</details>
<details><summary>What is a language model, in terms of conditional probability?</summary>A model of P(next token | all previous tokens).</details>
<details><summary>What is log 1, and why?</summary>0, because e⁰ = 1.</details>
