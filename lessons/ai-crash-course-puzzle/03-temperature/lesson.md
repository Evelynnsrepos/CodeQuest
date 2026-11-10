---
title: Temperature, how wild the model is
minutes: 25
xp: 25
hint: First loop: scaled.append(s / t). Divide by the temperature.
hint: Second loop: exps.append(math.exp(s - biggest)). Then total = sum(exps), then probs.append(e / total).
distractor: scaled.append(s * t)
distractor: probs.append(total / e)
---
# Temperature

⏱️ About 25 minutes · 🧩 4 gaps, 2 decoys

> **Warm-up:** if you ask a chatbot the same question twice, do you always get the same answer? Why not?

**In one sentence:** the model gives each possible next token a **score**; **softmax** turns scores into chances, and **temperature** decides how sharp or flat those chances are.

## 💡 The idea

- **Low temperature** (like 0.2): the top token gets almost all the chance. Safe, the same every time.
- **Temperature 1**: the model's normal chances.
- **High temperature** (like 5): the chances get flatter, so unlikely tokens get picked more. Creative, but wilder.

## 🔢 The maths, step by step

New symbol: **e** is a special number, about **2.718**. "e to the power of x", written eˣ, means "e multiplied by itself x times". You don't need to work it out yourself, Python's `math.exp(x)` does it. What matters: eˣ is **always positive**, and bigger x gives a much bigger eˣ.

Softmax of the scores `[2, 0]` with temperature t = 1:

1. **Divide by t:** 2 ÷ 1 = 2 and 0 ÷ 1 = 0 → `[2, 0]`.
2. **Subtract the biggest** (2) from each: `[0, -2]`. This keeps the numbers small so the computer doesn't overflow. It doesn't change the final chances.
3. **e to the power:** e⁰ = 1 and e⁻² ≈ 0.135 → `[1, 0.135]`.
4. **Total:** 1 + 0.135 = 1.135.
5. **Divide each by the total:** 1 ÷ 1.135 ≈ **0.88** and 0.135 ÷ 1.135 ≈ **0.12**. They add up to 1 (100%). ✓

Now with t = 0.5: step 1 gives 2 ÷ 0.5 = 4, so `[4, 0]` → `[0, -4]` → `[1, 0.018]` → about **0.98** and **0.02**. Lower temperature made the winner even stronger.

## 🐍 The Python in this puzzle

| Piece | Say it | What it does |
|---|---|---|
| `scaled = []` | "scaled is an empty list" | an empty list to fill up |
| `for s in scores:` | "for each s in scores" | repeats for every score |
| `scaled.append(s / t)` | "append s divided by t" | adds one result to the list |
| `max(scaled)` | "max of scaled" | the biggest number in the list |
| `math.exp(x)` | "e to the x" | eˣ |
| `sum(exps)` | "sum of exps" | adds up everything in the list |

## 🧩 Your puzzle

The function does the five steps above, each as a loop that fills a new list:

1. First loop: divide each score by the temperature `t`. (Decoy: `s * t`, which would make low temperature *flatter*: backwards!)
2. Second loop: e to the power of (score minus the biggest).
3. Add up all the exps.
4. Last loop: each exp divided by the total. (Decoy: the other way round.)

Run it: the first line should be `[0.66, 0.24, 0.1]`, the low-temperature line almost `[1.0, 0.0, 0.0]`, the high one flatter.

**Remember:** divide by t, softmax, done.
