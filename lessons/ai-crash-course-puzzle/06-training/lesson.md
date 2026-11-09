---
title: Training, learning from mistakes
minutes: 30
xp: 30
hint: error = w * xs[i] - ys[i] (guess minus truth). Then total = total + 2 * error * xs[i].
hint: gradient gives back total / len(xs). train: w = w - lr * gradient(w, xs, ys). Minus, so you walk downhill.
distractor: w = w + lr * gradient(w, xs, ys)
distractor: error = ys[i] - xs[i]
---
# Training

⏱️ About 30 minutes · 🧩 4 gaps, 2 decoys

> **Warm-up:** you're blindfolded on a hill and want to reach the bottom. What do you do?

**In one sentence:** training means: guess, measure how wrong you are, nudge the numbers a little in the direction that makes you less wrong, and repeat thousands of times. That's **gradient descent**.

## 💡 The idea

Our tiny model has **one** number, `w` (for **weight**). It guesses **y = w × x**. The data is secretly y = 2x (1→2, 2→4, 3→6), so the best `w` is 2. The model starts at `w = 0` and has to find 2 by itself.

The **gradient** tells you which way is uphill and how steep it is. You step the **other way** (downhill), a small step each time. An LLM does exactly this, just with billions of numbers instead of one.

## 🔢 The maths, step by step

One data point: x = 1, y = 3. Start at w = 0.

1. **Guess:** w × x = 0 × 1 = 0.
2. **Error:** guess minus truth = 0 − 3 = **−3**. (Negative means we guessed too low.)
3. **Gradient** for this point: 2 × error × x = 2 × (−3) × 1 = **−6**. (The 2 comes from the maths of "squared error"; you can just trust it.)
4. With several points, add up each point's gradient and divide by how many points: the **average**.
5. **Step:** new w = w − lr × gradient. **lr** is the **learning rate**, the step size, say 0.1:
   w = 0 − 0.1 × (−6) = 0 + 0.6 = **0.6**. Minus a minus is a plus, so w went **up**, towards 3. ✓

Repeat, and w keeps creeping towards the right answer. Too big an lr and you overshoot and fly off: try `lr = 0.5` after you've solved it.

## 🐍 The Python in this puzzle

| Piece | Say it | What it does |
|---|---|---|
| `xs[i]`, `ys[i]` | "x at i", "y at i" | the i-th input and its right answer |
| `w * xs[i] - ys[i]` | "w times x minus y" | guess minus truth: the error |
| `2 * error * xs[i]` | "2 times error times x" | this point's gradient |
| `total / len(xs)` | "total divided by how many" | the average |
| `w - lr * g` | "w minus lr times g" | times goes first, then minus (like in school) |

## 🧩 Your puzzle

1. The error: **guess minus truth** (decoy: `ys[i] - xs[i]` forgets the guess).
2. Add this point's gradient to the total.
3. After the loop: the **average**.
4. In `train`: step **downhill**, `w minus …` (decoy: plus walks uphill and w runs away).

Run it: `-18.666… 1.99…`: the gradient starts big and negative, and after 50 steps w is almost exactly 2.

**Remember:** guess, error, step downhill, repeat.
