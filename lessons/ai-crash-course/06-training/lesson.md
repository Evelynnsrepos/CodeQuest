---
title: Training: nudge, check, repeat
minutes: 30
xp: 30
hint: gradient: total = 0, then for i in range(len(xs)): error = w * xs[i] - ys[i] and total = total + 2 * error * xs[i]
hint: gradient ends with return total / len(xs) (back at 4 spaces, after the loop)
hint: train: w = 0.0, then for step in range(steps): w = w - lr * gradient(w, xs, ys), then return w
---
# How a model learns

⏱️ About 30 minutes · two functions

> **Warm-up:** you're blindfolded on a hill and want to reach the bottom. What do you do?

**In one sentence:** training means: guess, measure how wrong the guess was, nudge the model's numbers a small step in the "less wrong" direction, and repeat thousands of times.

## 💡 The idea in plain words

You feel which way the ground slopes and take a small step downhill. Repeat. That's **gradient descent**, and it's how every neural network learns, including LLMs.

A model is a calculation with adjustable numbers called **weights**. Training is:

1. **Predict** with the current weights.
2. **Measure how wrong** the prediction is. That number is the **loss**: 0 = perfect, bigger = worse.
3. **Find the slope** (the **gradient**): which direction to move each weight so the loss goes down.
4. **Take a small step** that way. The step size is the **learning rate**.
5. Repeat.

## 🔢 The tiniest model, one step at a time

Our model has **one** weight, `w`. It predicts: **prediction = w × x**. The training data is pairs of x (the input) and y (the right answer):

| x | 1 | 2 | 3 |
|---|---|---|---|
| y | 2 | 4 | 6 |

You can see the right answer is w = 2 (because 2 × 1 = 2, 2 × 2 = 4, 2 × 3 = 6). The model can't see that; it starts at w = 0 and must find 2 on its own.

### The error

**error = prediction − right answer = w × x − y**. With w = 0: the errors are 0 − 2 = −2, 0 − 4 = −4, 0 − 6 = −6. Negative means "the prediction is too small".

### The loss

The loss is the **average of the squared errors**. Squaring (multiplying a number by itself) makes every error positive, so too big and too small both count as wrong: (−2)² = 4, (−4)² = 16, (−6)² = 36. Average: (4 + 16 + 36) ÷ 3 = 18.67. A big loss: the model is very wrong.

### The gradient

The gradient says how the loss changes when w grows a tiny bit. For this model the rule is: **the average of 2 × error × x**. (The rule comes from calculus, explained in Math 3 lessons 09–10. Here you only need to use it.)

<div class="formula">gradient = <span class="k1">average of</span> ( <span class="k2">2</span> × <span class="k3">(w × x − y)</span> × <span class="k4">x</span> )</div>

| Piece | Means | With w = 0 |
|---|---|---|
| <span class="k3">(w × x − y)</span> | the error for one pair | −2, −4, −6 |
| <span class="k4">x</span> | that pair's input. A big x means w has a big effect on this prediction. | 1, 2, 3 |
| <span class="k2">2</span> | comes from the squaring in the loss | |
| 2 × error × x | one pair's part | 2 × −2 × 1 = −4, 2 × −4 × 2 = −16, 2 × −6 × 3 = −36 |
| <span class="k1">average of</span> | add up, divide by how many | (−4 − 16 − 36) ÷ 3 = −56 ÷ 3 = **−18.67** |

### The step

<div class="formula"><span class="k1">new w</span> = <span class="k2">w</span> <span class="k3">−</span> <span class="k4">learning rate</span> × <span class="k5">gradient</span></div>

The gradient points **uphill** (towards more loss), so we go the other way: that's the **minus**. With learning rate 0.05:

new w = 0 − 0.05 × (−18.67) = 0 + 0.933 = **0.933**.

(Minus a negative number is plus: taking away a debt gives you money.) w moved from 0 towards 2. Repeat 50 times and it lands at 2.

### Learning rate too big or too small

- **Too big**: the step jumps right over the bottom, lands even higher on the other side, and next time jumps further. The loss explodes.
- **Too small**: every step is tiny, so it takes forever.

<div class="quiz" data-answer="0" data-why="The steps overshoot the bottom. Smaller steps fix it. Try it in the drawing below with a learning rate above 1."><p><b>Predict first:</b> your loss gets bigger every step until it explodes. What do you change?</p><button>make the learning rate smaller</button><button>make the learning rate bigger</button><button>train for more steps</button></div>

<div class="explore" data-widget="gradient-descent"></div>

An LLM does exactly this, with billions of weights at once, and the "right answer y" is the real next token.

**Go deeper:** LLMs 5 (How training works), Math 3 lessons 09–11, AI engineer 1 lesson 08.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `xs[i]`, `ys[i]` | "xs at i" | the i-th input and the i-th right answer. Same i = same pair. |
| `error = w * xs[i] - ys[i]` | "error becomes w times x minus y" | one pair's error |
| `total / len(xs)` | "total divided by how many" | an average |
| `w = w - lr * g` | "w becomes w minus lr times g" | replaces what's in the box `w` with the new value. The right side is computed first, with the **old** w. |
| `0.0` | "zero point zero" | zero, written as a decimal number |
| `for step in range(steps):` | "repeat steps times" | `step` counts 0, 1, 2, …; you don't have to use it |

### 👀 Worked example 1: the average error

This computes the **average error** (no 2, no × x). Your `gradient` is the same loop with `2 * error * xs[i]`:

```python
def average_error(w, xs, ys):
    total = 0
    for i in range(len(xs)):
        error = w * xs[i] - ys[i]
        total = total + error
    return total / len(xs)
```

`average_error(0, [1, 2, 3], [2, 4, 6])`: errors −2, −4, −6, total −12, ÷ 3 = `-4.0`.

### 👀 Worked example 2: repeat a nudge

This moves a guess halfway towards a target, again and again. It has the shape of `train`:

```python
def halfway(guess, target, steps):
    for step in range(steps):
        guess = guess - 0.5 * (guess - target)
    return guess
```

`halfway(0, 8, 3)`: 0 → 0 − 0.5 × (−8) = 4 → 4 − 0.5 × (−4) = 6 → 6 − 0.5 × (−2) = 7. Gives `7.0`: closer each step.

## 🎯 Your quest

1. `gradient(w, xs, ys)`: copy `average_error` and change one line to `total = total + 2 * error * xs[i]`. `gradient(0, [1, 2, 3], [2, 4, 6])` should give −18.67, like the table.
2. `train(xs, ys, steps, lr)`:
   - `w = 0.0`
   - `for step in range(steps):` → inside: `w = w - lr * gradient(w, xs, ys)`
   - after the loop: `return w`

Press **Run**: it should print a number very close to 2.

**Remember:** predict, measure the loss, step downhill.
