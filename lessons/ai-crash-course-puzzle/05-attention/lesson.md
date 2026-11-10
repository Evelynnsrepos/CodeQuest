---
title: Attention, which words matter
minutes: 30
xp: 30
hint: weights is softmax again: exps.append(math.exp(s - biggest)) and result.append(e / total).
hint: attend: w = weights(scores), then inside the inner loop total = total + w[i] * values[i][d], then result.append(total).
distractor: total = total + values[i][d]
distractor: w = scores
---
# Attention

⏱️ About 30 minutes · 🧩 5 gaps, 2 decoys

> **Warm-up:** in "The cat sat on the mat because **it** was tired", which word is "it"?

**In one sentence:** **attention** lets each word look at all the other words, decide how much each one matters (the **weights**), and mix their meanings in those amounts.

## 💡 The idea

To understand "it", the model gives every other word a **score**: "cat" high, "mat" lower, "the" almost nothing. Softmax (from lesson 03) turns the scores into **weights** that add up to 1. Then it takes a **weighted average** of the words' vectors: lots of "cat", a little "mat". That mix becomes the new meaning of "it". Transformers (the T in GPT) are mostly this, repeated many times.

## 🔢 The maths, step by step: a weighted average

Two words with the vectors `[2, 0]` and `[0, 4]`, and weights `0.5` and `0.5`:

1. First number of the result: 0.5 × 2 + 0.5 × 0 = 1 + 0 = **1**.
2. Second number: 0.5 × 0 + 0.5 × 4 = 0 + 2 = **2**.
3. Result: `[1, 2]`, exactly half-way between them.

With weights `0.9` and `0.1` instead: first number 0.9 × 2 + 0.1 × 0 = **1.8**, second 0.9 × 0 + 0.1 × 4 = **0.4** → `[1.8, 0.4]`, mostly the first word.

So for each **position d** (first number, second number …) you go through every **word i** and add **weight × that word's number at d**.

## 🐍 The Python in this puzzle

| Piece | Say it | What it does |
|---|---|---|
| `values[i]` | "values at i" | word number i's vector, e.g. `[2, 0]` |
| `values[i][d]` | "values at i, at d" | the number at position d inside that vector |
| `len(values[0])` | "length of the first vector" | how many numbers each vector has |
| a loop inside a loop | "for each d, for each i" | the inner loop runs completely, every turn of the outer one |
| `w[i]` | "w at i" | the weight of word i |

## 🧩 Your puzzle

**`weights`** is softmax again (same as lesson 03, without temperature):

1. e to the power of (score minus biggest).
2. Each one divided by the total.

**`attend`**:

3. First turn the scores into weights with your function (decoy: `w = scores` skips the softmax).
4. Inner loop: add **weight × number** to the total (decoy: forgets the weight).
5. After the inner loop: put that total in the result.

Run it: the weights line shows the second word winning (about 0.69), and the mix leans towards its vector `[0, 1]`.

**Remember:** score, softmax, weighted average.
