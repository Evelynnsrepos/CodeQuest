---
title: Attention in one picture
xp: 30
hint: weights is lesson 03's softmax without the temperature: biggest = max(scores), exps with math.exp(s - biggest), then shares of the total.
hint: attend starts with w = weights(scores) and size = len(values[0]), then result = []
hint: for d in range(size): total = 0, then for i in range(len(values)): total = total + w[i] * values[i][d], then result.append(total)
---
# Each word looks at the others

⏱️ About 30 minutes · two functions

> **Warm-up:** in "The cat didn't eat because **it** was full", what does "it" refer to? How did you decide?

**In one sentence:** with **attention**, each token scores how useful every earlier token is, turns the scores into weights with softmax, and mixes the earlier tokens' vectors using those weights.

## 💡 The idea in plain words

**Attention** is how a transformer (the T in GPT) lets each token collect information from the tokens before it. Each token is stored as a vector (a list of numbers, lesson 04). For the token "it":

1. It gives every earlier token a **relevance score**: how useful is "cat" for understanding me? "eat"? "The"?
2. **Softmax** turns the scores into **weights**: shares that add up to 1 (exactly lesson 03).
3. Its new vector is the **weighted average** of the earlier tokens' vectors: mostly "cat", a little of the rest. Now "it" carries the meaning "the cat".

<svg viewBox="0 0 520 150" width="100%" style="max-width:520px" role="img" aria-label="The token 'it' with arrows to earlier tokens; the arrow to 'cat' is thickest, weight 0.7">
  <g font-size="14" fill="currentColor" text-anchor="middle">
    <text x="50" y="30">The</text><text x="140" y="30">cat</text><text x="240" y="30">didn't</text><text x="340" y="30">eat</text><text x="440" y="130">it</text>
    <text x="70" y="80" font-size="12">0.05</text><text x="175" y="75" font-size="12">0.70</text><text x="265" y="80" font-size="12">0.05</text><text x="360" y="80" font-size="12">0.20</text>
  </g>
  <g stroke="#6c4cf5" fill="none" stroke-linecap="round">
    <line x1="430" y1="115" x2="55" y2="38" stroke-width="1"/>
    <line x1="430" y1="115" x2="145" y2="38" stroke-width="8"/>
    <line x1="430" y1="115" x2="245" y2="38" stroke-width="1"/>
    <line x1="430" y1="115" x2="345" y2="38" stroke-width="3"/>
  </g>
</svg>

The thicker the line, the bigger the weight. The four weights add up to 0.05 + 0.70 + 0.05 + 0.20 = 1.

In a real model the scores come from learned vectors called **queries** and **keys**, and the mixed vectors are called **values** (LLMs 8 and AI engineer 1 lesson 03). A model stacks dozens of these layers, each with many attention "heads" that look for different relationships.

## 🔢 The weighted average, one step at a time

### A normal average

The average of 2, 4 and 6: add them (12) and divide by how many there are (3): **4**. That's the same as giving each one the weight ⅓: ⅓ × 2 + ⅓ × 4 + ⅓ × 6 = 4.

### A weighted average

Now some count more than others. Exam 90 points with weight 0.5, homework 60 with weight 0.25, project 80 with weight 0.25 (the weights add up to 1):

1. 0.5 × 90 = 45
2. 0.25 × 60 = 15
3. 0.25 × 80 = 20
4. add: 45 + 15 + 20 = **80**

Multiply each value by its weight, then add everything up.

### With vectors: do it once per position

When the values are vectors, you do the weighted average **separately for each position**. Weights 0.5, 0.25, 0.25 and vectors `[2, 0]`, `[0, 4]`, `[4, 4]`:

| | weight × first number | weight × second number |
|---|---|---|
| vector 1 | 0.5 × 2 = 1 | 0.5 × 0 = 0 |
| vector 2 | 0.25 × 0 = 0 | 0.25 × 4 = 1 |
| vector 3 | 0.25 × 4 = 1 | 0.25 × 4 = 1 |
| **add the column** | **2** | **2** |

The result is `[2, 2]`.

### The formula

<div class="formula">new = <span class="k1">Σ</span> <span class="k2">w<sub>i</sub></span> · <span class="k3">v<sub>i</sub></span></div>

| Piece | Say it | Means | Example above |
|---|---|---|---|
| <span class="k1">Σ</span> | "sum" (the Greek capital letter sigma, an S for "sum") | add up the thing after it, for every *i*: for every earlier token | the "add the column" row |
| <span class="k2">w<sub>i</sub></span> | "w i" | the weight of token number *i* (from softmax) | 0.5, 0.25, 0.25 |
| · | "times" | multiply | |
| <span class="k3">v<sub>i</sub></span> | "v i" | the vector (value) of token number *i* | `[2, 0]`, `[0, 4]`, `[4, 4]` |

<div class="quiz" data-answer="0" data-why="Softmax always gives numbers that add up to 1, so the new vector is a true weighted average."><p><b>Predict first:</b> one token’s attention weights come out of a softmax. What do they add up to?</p><button>1</button><button>the number of tokens</button><button>it depends</button></div>

**Go deeper:** LLMs 1 lesson 12, LLMs 8 lesson 01, Math 2 lesson 11.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `values[1]` | "values at 1" | the second vector in the list of vectors, e.g. `[0, 4]` |
| `values[1][0]` | "values at 1, at 0" | first number of the second vector: `0`. Read it left to right: which vector, then which position. |
| `len(values[0])` | "length of the first vector" | how many numbers each vector has (they all have the same) |
| a loop inside a loop | "nested loop" | the inner loop runs completely, every time the outer loop goes round once. Inner lines get **12 spaces**. |

### 👀 Worked example 1: weighted average of numbers

```python
def weighted_average(w, nums):
    total = 0
    for i in range(len(nums)):
        total = total + w[i] * nums[i]
    return total
```

`weighted_average([0.5, 0.25, 0.25], [90, 60, 80])` gives 45 + 15 + 20 = `80`, the exam example.

### 👀 Worked example 2: plain column sums of vectors

This adds up each position (column) of a list of vectors. It has the outer loop over positions and the inner loop over vectors that `attend` needs:

```python
def column_sums(vectors):
    size = len(vectors[0])
    result = []
    for d in range(size):
        total = 0
        for i in range(len(vectors)):
            total = total + vectors[i][d]
        result.append(total)
    return result
```

`column_sums([[1, 2], [10, 20]])`:

- d = 0 (first position): total = 0 + 1 + 10 = 11 → result `[11]`
- d = 1 (second position): total = 0 + 2 + 20 = 22 → result `[11, 22]`

`attend` is this function with one change: `w[i] * vectors[i][d]` instead of `vectors[i][d]`.

## 🎯 Your quest

1. `weights(scores)`: softmax, like lesson 03 but **without** dividing by a temperature:
   - `biggest = max(scores)`
   - `exps = []`, `for s in scores:` → `exps.append(math.exp(s - biggest))`
   - `total = sum(exps)`
   - `result = []`, `for e in exps:` → `result.append(e / total)`
   - `return result`
2. `attend(scores, values)`: `values` is a list of vectors, one per earlier token. Give back the weighted average vector:
   - `w = weights(scores)`
   - then exactly `column_sums`, with `vectors` called `values` and the line `total = total + w[i] * values[i][d]`

**Remember:** score, softmax, weighted average.
