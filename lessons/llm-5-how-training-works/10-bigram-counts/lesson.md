---
title: makemore 1: a bigram model by counting
xp: 45
---
# The simplest language model

> **Warm-up:** if you could only look at the *previous letter*, how would you guess the next letter of a name?

Count. Andrej Karpathy's *makemore* lectures (episode 2 of *Zero to Hero*) start exactly here: a **character-level bigram model**, which predicts each character from the one before it. Tokens are the 26 letters plus a special `.` that marks both the start and the end of a name, so `"emma"` becomes the pairs:

```
. → e    e → m    m → m    m → a    a → .
```

Count every pair over a list of names in a 27 × 27 table `N`. Row `a` of `N`, divided by its sum, is the **probability distribution of the next character after `a`**. That table *is* the model: generation samples a character from the current row, moves to that row, and repeats until it samples `.`.

Two details that matter for every language model:

- **Smoothing.** A pair never seen in training gets probability 0, and then `log 0 = −∞` breaks the loss. Adding 1 to every count ("add-one smoothing") gives everything a small chance.
- **Evaluation** uses the same loss as any LLM: the average **negative log-likelihood** of the true next characters (LLMs 1, lesson 6; LLMs 4, lesson 10). A model that guesses uniformly among 27 characters scores `log 27 ≈ 3.30`. Lower is better.

## Your quest

`CHARS` maps index ↔ character (index 0 is `.`).

1. `count_bigrams(names)`: a 27 × 27 list of lists of zeros, then for every name, for every pair in `"." + name + "."`, add 1 at `[index of first][index of second]`. `STOI[ch]` gives a character's index; `zip(s, s[1:])` gives the pairs of a string.
2. `to_probs(N)`: add 1 to every count, then divide each row by its sum.
3. `nll(P, names)`: the average of `−log P[a][b]` over every pair of every name.

The program then samples a few new "names". They'll be bad, and that's the point: one letter of context isn't enough.

## Review

<details><summary>Write the AdamW update for one weight.</summary>m = β₁m + (1−β₁)g; v = β₂v + (1−β₂)g²; bias-correct both; p = p − lr·wd·p − lr·m̂/(√v̂ + ε).</details>
<details><summary>Why use LR warmup?</summary>Early on, Adam's running statistics are unreliable; ramping the LR up avoids huge bad steps.</details>
