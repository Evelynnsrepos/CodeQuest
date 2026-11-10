---
title: Is it worth automating?
minutes: 15
xp: 20
hint: First line inside the function: saved = minutes_per_run * runs_per_week
hint: Then two lines: if saved == 0: and under it (4 more spaces) return None
hint: Last line: return math.ceil(build_hours * 60 / saved)
---
# Do the math before you build

⏱️ About 15 minutes · one function, four lines

> **Warm-up:** renaming your screenshots takes 2 minutes, you do it 5 times a week, and a script would take 3 hours to build. Is it worth it? Guess before you read on.

**In one sentence:** automation pays off when the time it saves adds up to more than the time it takes to build.

## 🪜 The maths, one step at a time

We want the **payback time**: how many weeks until the script has "paid back" the hours you spent building it.

**Step 1. Time saved per week.** Multiply the minutes one run saves by how often it runs. The sign `×` means "times" (multiply).

`saved per week = minutes per run × runs per week`

2 minutes × 5 runs = **10 minutes** saved every week.

**Step 2. Build time in minutes.** An hour has 60 minutes, so:

`build minutes = build hours × 60`

3 hours × 60 = **180 minutes**.

**Step 3. Divide.** How many "10 minute weeks" fit into 180 minutes? The sign `÷` means "divided by".

`payback weeks = build minutes ÷ saved per week`

180 ÷ 10 = **18 weeks**. After about 4 months the script has paid for itself, and from then on it's pure win.

**Step 4. Round up.** Sometimes the division doesn't give a whole number, like 17.2 weeks. The script isn't paid back in week 17 yet, only in week 18. Rounding **up** to the next whole number is called the **ceiling**: 17.2 → 18, 4.1 → 5, but 6.0 stays 6.

## 🔀 What if it were different?

<div class="wrong"><b>It saves 0 minutes</b>: step 3 would divide by zero. "How many 0-minute weeks fit into 180 minutes?" has no answer, and Python stops with a <code>ZeroDivisionError</code>.</div>
<div class="right">Check for 0 first and give back <code>None</code> ("no answer, it never pays back") ✓</div>

Time isn't the only reason: automating something you **always forget** or that's **boring enough to make you avoid it** can be worth it even with a long payback.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `import math` | "import math" | loads Python's maths toolbox. It's already at the top of the editor. |
| `def payback_weeks(a, b, c):` | "define payback weeks of a, b, c" | starts a **function**: a named recipe. The names in the brackets are its inputs. The lines that belong to it start with 4 spaces. |
| `saved = a * b` | "saved becomes a times b" | `*` is times. The result goes into a box (a **variable**) called `saved`. |
| `/` | "divided by" | `180 / 10` gives `18.0` |
| `if saved == 0:` | "if saved equals 0" | two `=` signs **compare** (one `=` puts something into a box). The lines under it, with 4 more spaces, only run when it's true. |
| `return x` | "return x" | gives `x` back as the function's answer and **stops** the function right there. |
| `None` | "none" | Python's word for "no value". No quotes. |
| `math.ceil(17.2)` | "ceiling of 17.2" | rounds **up**: `18` |

### 👀 Worked example: same shape, other numbers

A function that says how many boxes you need for some cups. One box holds `per_box` cups, and you can't pack into a box that holds 0:

```python
import math

def boxes_needed(cups, per_box):
    if per_box == 0:
        return None
    return math.ceil(cups / per_box)
```

`boxes_needed(10, 4)`, line by line:

1. `cups` is 10, `per_box` is 4.
2. `if per_box == 0:`: is 4 equal to 0? No, so the `return None` line is skipped.
3. `cups / per_box` = 10 / 4 = 2.5.
4. `math.ceil(2.5)` = **3**. Two boxes aren't enough, you need a third. The function returns `3`.

`boxes_needed(10, 0)`: the `if` is true, so it returns `None` and stops before dividing.

## 🎯 Your quest

Write `payback_weeks(minutes_per_run, runs_per_week, build_hours)`. The starter's function only has `pass` in it ("do nothing"): delete that line. The `#` lines show what to write. Inside the function, type these lines (each starts with 4 spaces):

1. `saved = minutes_per_run * runs_per_week` (step 1)
2. `if saved == 0:`
3. `    return None` (8 spaces in total: it belongs to the `if`)
4. `return math.ceil(build_hours * 60 / saved)` (steps 2, 3 and 4 in one line)

It should give:

- `payback_weeks(2, 5, 3)` → `18`
- `payback_weeks(5, 7, 1)` → `2` (60 ÷ 35 = 1.7, rounded up)
- `payback_weeks(0, 10, 1)` → `None`

**Remember:** saved per week, build time in minutes, divide, round up.

## Review

<details><summary>What does math.ceil(4.1) give, and why use it here?</summary>5. A payback of 4.1 weeks only finishes in week 5, so we round up.</details>
<details><summary>What's the difference between = and == in Python?</summary>One = puts a value into a box (saved = 10). Two == ask "are these equal?" (saved == 0).</details>
