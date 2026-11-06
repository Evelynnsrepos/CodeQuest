---
title: Probabilities and temperature
xp: 30
hint: First loop: scaled = [] then for s in scores: and inside it scaled.append(s / t)
hint: biggest = max(scaled), then a second loop: exps.append(math.exp(s - biggest))
hint: total = sum(exps), then a third loop: probs.append(e / total), then return probs
---
# Why answers vary

⏱️ About 30 minutes · one function, three small loops

> **Warm-up:** ask a chatbot the same question twice. Why can the answers differ?

**In one sentence:** the model gives each possible next token a score, **softmax** turns the scores into chances that add up to 100%, and **temperature** decides how strongly the top score wins.

## 💡 The idea in plain words

For every possible next token, the network outputs a **score** (also called a *logit*). Bigger score = better fit. But scores aren't chances: they can be negative and don't add up to anything nice.

So we turn them into **probabilities**: numbers between 0 and 1 that add up to exactly 1 (1 = 100%). Then the model **samples**: it rolls a weighted die. A token with probability 0.66 comes out 66 times in 100. That's why the same question can give different answers.

## 🔢 Softmax, one step at a time

Softmax has two steps. First the new symbol it uses.

### The number e

**e** is a fixed number, like π. It's about **2.718**. "e to the power of x", written **eˣ**, means 2.718 multiplied by itself x times:

| x | eˣ | why |
|---|---|---|
| 0 | 1 | anything to the power 0 is 1 |
| 1 | 2.718 | just e |
| 2 | 7.389 | 2.718 × 2.718 |
| −1 | 0.368 | a minus power means "1 divided by": 1 ÷ 2.718 |
| 0.1 | 1.105 | a power between 0 and 1 gives a number between 1 and e |

Two facts make eˣ perfect here: it is **always positive** (even for negative scores), and **bigger x always gives a bigger result**, so the order of the scores stays the same.

### Step 1 and step 2

1. **Raise e to each score.** Scores 2.0, 1.0, 0.1 become 7.389, 2.718, 1.105.
2. **Divide each by the total.** Total = 7.389 + 2.718 + 1.105 = 11.212. Then 7.389 ÷ 11.212 = 0.659, and so on.

```
scores   2.0     1.0     0.1
e^x      7.389   2.718   1.105    total 11.212
probs    0.659   0.242   0.099    (they add up to 1)
```

Dividing by the total is the same thing you do for percentages: "my share of the pizza = my slices ÷ all slices".

<div class="formula">p<sub>i</sub> = <span class="k1">e<sup>s<sub>i</sub></sup></span> <span class="k2">÷</span> <span class="k3">(e<sup>s<sub>1</sub></sup> + e<sup>s<sub>2</sub></sup> + …)</span></div>

| Piece | Say it | Means | With the numbers above (first token) |
|---|---|---|---|
| p<sub>i</sub> | "p i" | the probability of token number *i* (the little *i* below just means "number i") | 0.659 |
| <span class="k1">e<sup>s<sub>i</sub></sup></span> | "e to the s i" | e raised to that token's score | e² = 7.389 |
| <span class="k2">÷</span> | "divided by" | its share of… | |
| <span class="k3">(e<sup>s<sub>1</sub></sup> + …)</span> | "the sum of all of them" | …the total of all tokens' eˣ | 11.212 |

### The safety trick: subtract the biggest score first

Computers can't store huge numbers: e¹⁰⁰⁰ is too big and Python crashes with `OverflowError`. The fix: **subtract the biggest score from every score first**. Then the biggest becomes 0 (and e⁰ = 1), and everything else is negative (small, safe numbers).

It doesn't change the answer. Check with our numbers: scores minus 2.0 are 0, −1, −1.9. Then e⁰ = 1, e⁻¹ = 0.368, e⁻¹·⁹ = 0.150, total 1.518, and 1 ÷ 1.518 = 0.659. Same as before! (Every eˣ shrank by the same factor, so every share stays the same.)

### Temperature

**Temperature** (T) divides every score **before** softmax.

- **T = 0.2**: 2.0 ÷ 0.2 = 10, 1.0 ÷ 0.2 = 5. The gap grew from 1 to 5, so the top token wins almost always (>99%). **Focused, repeatable**: good for code and facts.
- **T = 5**: 2.0 ÷ 5 = 0.4, 1.0 ÷ 5 = 0.2. The gap shrank, so the chances get closer to each other. **Varied, creative**, more mistakes.
- **T = 1**: dividing by 1 changes nothing.
- **T = 0** in apps means "always take the top token" (you can't divide by 0, so apps handle it separately).

<div class="quiz" data-answer="0" data-why="Dividing by 0.2 makes the gaps between scores 5 times bigger, so the top token pulls further ahead."><p><b>Predict first:</b> you lower the temperature from 1 to 0.2. What happens to the top token’s probability?</p><button>it goes up</button><button>it goes down</button><button>it stays the same</button></div>

<div class="explore" data-widget="temperature"></div>

**Go deeper:** LLMs 1, lessons 5, 8 and 9; Math 3 lesson 05 (e and exp); Math 5 lesson 06.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `scaled = []` | "scaled becomes an empty list" | a list with nothing in it yet, ready to fill |
| `for s in scores:` | "for each s in scores" | repeats the indented lines once per number; `s` holds the current one |
| `scaled.append(s / t)` | "append s divided by t" | adds one new number to the end of the list |
| `max(scaled)` | "max of scaled" | the biggest number in the list |
| `sum(exps)` | "sum of exps" | all numbers in the list added up |
| `math.exp(x)` | "e to the x" | computes eˣ (`import math` is already at the top) |

### 👀 Worked example: shares of a total

This turns any list of positive numbers into shares that add up to 1. It's softmax without the e and without temperature, and it uses the exact loop pattern you need: **empty list, loop, append**.

```python
def shares(numbers):
    total = sum(numbers)
    result = []
    for n in numbers:
        result.append(n / total)
    return result
```

`shares([1, 3])`: total = 4. The loop: n = 1 → append 1 ÷ 4 = 0.25; n = 3 → append 3 ÷ 4 = 0.75. Gives `[0.25, 0.75]`.

Softmax is this pattern three times in a row: one loop to divide by t, one loop for eˣ, one loop for the shares.

## 🎯 Your quest

Write `softmax_t(scores, t)`. Each step is marked in the editor:

1. Divide by the temperature:
   - `scaled = []`
   - `for s in scores:` → inside: `scaled.append(s / t)`
2. The safety trick: `biggest = max(scaled)`
3. e to each (minus the biggest):
   - `exps = []`
   - `for s in scaled:` → inside: `exps.append(math.exp(s - biggest))`
4. Shares, exactly like the worked example:
   - `total = sum(exps)`
   - `probs = []`
   - `for e in exps:` → inside: `probs.append(e / total)`
   - `return probs`

Press **Run**: the first line should print `[0.66, 0.24, 0.1]`, the second (T = 0.2) almost `[1.0, 0.01, 0.0]`, the third (T = 5) close together.

**Remember:** low temperature sharpens, high temperature flattens.
