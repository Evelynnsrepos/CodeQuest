---
title: Evals: is it actually better?
minutes: 30
xp: 30
hint: accuracy: right = 0, then for i in range(len(gold)): and if preds[i].strip().lower() == gold[i].strip().lower(): right = right + 1
hint: accuracy ends with return right / len(gold). win_interval starts with p = wins / n
hint: margin = 2 * math.sqrt(p * (1 - p) / n), then return (p - margin, p + margin). is_better: low = win_interval(wins, n)[0] and return low > 0.5
---
# Measure, don't vibe

⏱️ About 30 minutes · three small functions

> **Warm-up:** you changed your prompt and the first two answers looked better. Is the new prompt better?

**In one sentence:** an **eval** is a fixed set of test questions scored the same way every time, and an **error bar** tells you whether a difference is real or just luck.

## 💡 The idea in plain words

Maybe it's better. But two examples is luck. An **eval** is a fixed set of test questions with known good answers (a **golden set**), scored the same way every time you change something. Common scores:

- **accuracy**: the share of answers that are right (for questions with one right answer);
- **win rate**: in blind A/B comparisons, how often the new version is preferred (by people, or by a judge model);
- the **error bar**: with few questions, results jump around by luck. It tells you how far.

## 🔢 Accuracy, step by step

Predictions `["Paris", "berlin ", "Rome"]`, right answers `["paris", "Berlin", "Madrid"]`:

1. Clean both before comparing: remove spaces at the ends and make everything lowercase. `"berlin "` → `"berlin"`, `"Berlin"` → `"berlin"`.
2. Compare position by position: paris = paris ✓, berlin = berlin ✓, rome ≠ madrid ✗.
3. Right ones ÷ all: 2 ÷ 3 = **0.67** (67%).

## 🔢 The error bar, one piece at a time

Your new prompt won 60 of 100 blind comparisons. Is it really better than 50/50? Here's the formula; we'll build it from the inside out.

<div class="formula"><span class="k1">p</span> <span class="k2">±</span> <span class="k3">2</span> · <span class="k4">√</span>( <span class="k1">p</span> · <span class="k5">(1 − p)</span> ÷ <span class="k6">n</span> )</div>

| Piece | Say it | Means | 60 wins of 100 |
|---|---|---|---|
| <span class="k6">n</span> | "n" | how many comparisons you ran | 100 |
| <span class="k1">p</span> | "p" | the measured win rate: wins ÷ n | 60 ÷ 100 = 0.6 |
| <span class="k5">(1 − p)</span> | "one minus p" | the loss rate | 1 − 0.6 = 0.4 |
| <span class="k1">p</span> · <span class="k5">(1 − p)</span> | "p times one minus p" | the dot means multiply. Biggest when p is 0.5 (most uncertain). | 0.6 × 0.4 = 0.24 |
| ÷ <span class="k6">n</span> | "divided by n" | more comparisons → smaller → less luck | 0.24 ÷ 100 = 0.0024 |
| <span class="k4">√</span> | "square root of" | undoes a square (lesson 04): √0.0024 is the number that times itself gives 0.0024 | 0.049 |
| <span class="k3">2</span> · | "two times" | 2 is a safety factor: with it, about 95 of 100 times the true rate is inside the bar | 2 × 0.049 = 0.098 |
| <span class="k2">±</span> | "plus or minus" | gives **two** answers: one with minus (the low end), one with plus (the high end) | 0.6 − 0.098 = **0.502** and 0.6 + 0.098 = **0.698** |

So the true win rate is probably between 50.2% and 69.8%. The whole range is above 50%: **it's really better**, just barely.

### What changes with fewer questions

6 wins of 10: p is again 0.6, but 0.24 ÷ **10** = 0.024, √0.024 = 0.155, × 2 = 0.31. The range is 0.29 to 0.91. That includes 50% (and even "worse"!), so you **can't call a winner**. Same 60%, ten times fewer questions, a much wider bar.

The rule: **only call it better if the low end is above 0.5.**

<div class="quiz" data-answer="1" data-why="0.55 ± 2·√(0.55·0.45/100) ≈ 0.45 to 0.65. That range includes 50%, so you can’t call a winner yet."><p><b>Predict first:</b> the new prompt won 55 of 100 blind comparisons. Is it clearly better?</p><button>yes, 55% is more than half</button><button>not yet</button></div>

**Go deeper:** LLMs 7 lesson 05 (blind eval), Math 4 lessons 11–12, AI engineer 2 (evals in practice).

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `" Berlin ".strip()` | "strip" | removes spaces at both ends: `"Berlin"` |
| `"Berlin".lower()` | "lower" | all lowercase: `"berlin"` |
| `text.strip().lower()` | | both, left to right |
| `a == b` | "a equals b" | **two** equals signs **compare**: `True` or `False`. (One `=` puts something into a box.) |
| `right = right + 1` | "right goes up by one" | counting |
| `(low, high)` | "the pair low, high" | gives back two numbers at once (a tuple, lesson 08) |
| `pair[0]` | "pair at 0" | the first of the two |
| `return low > 0.5` | "give back whether low is bigger than 0.5" | a comparison is already `True` or `False`, so you can return it directly |

### 👀 Worked example: counting matches

```python
def count_same(a, b):
    same = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            same = same + 1
    return same
```

`count_same([1, 2, 3], [1, 5, 3])`: position 0 same (1), position 1 different, position 2 same (2). Gives `2`. Your `accuracy` adds `.strip().lower()` on both sides of the `==`, and divides by the count at the end.

### 👀 Worked example: giving back two numbers

```python
def around(x, width):
    return (x - width, x + width)


low_high = around(10, 3)   # (7, 13)
print(low_high[0])         # 7
print(around(10, 3)[0] > 5)   # True, because 7 > 5
```

## 🎯 Your quest

1. `accuracy(preds, gold)`: like `count_same`:
   - `right = 0`
   - `for i in range(len(gold)):`
   - inside: `if preds[i].strip().lower() == gold[i].strip().lower():` → `right = right + 1`
   - after the loop: `return right / len(gold)`
2. `win_interval(wins, n)`, the table above as code:
   - `p = wins / n`
   - `margin = 2 * math.sqrt(p * (1 - p) / n)`
   - `return (p - margin, p + margin)`
3. `is_better(wins, n)`:
   - `low = win_interval(wins, n)[0]`
   - `return low > 0.5`

**Remember:** a fixed test set, the same scoring, and an error bar.
