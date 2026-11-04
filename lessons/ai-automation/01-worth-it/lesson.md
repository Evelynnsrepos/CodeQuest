---
title: Is it worth automating?
xp: 20
---
# Do the math before you build

⏱️ About 10 minutes · one function

> **Warm-up:** renaming your screenshots takes 2 minutes, you do it 5 times a week, and a script would take 3 hours to build. Is it worth it? Guess before you read on.

**In one sentence:** automation pays off when the time it saves adds up to more than the time it takes to build.

## 🪜 The formula, one step at a time

We want the **payback time**: how many weeks until the script has "paid back" the hours you spent building it.

**Step 1. Time saved per week.** Multiply (`×`) the minutes one run saves by how often it runs:

`saved per week = minutes per run × runs per week`

2 minutes × 5 runs = **10 minutes** saved every week.

**Step 2. Build time in minutes.** An hour has 60 minutes, so:

`build minutes = build hours × 60`

3 hours × 60 = **180 minutes**.

**Step 3. Divide.** How many "10 minute weeks" fit into 180 minutes? Divide (`÷`, in Python `/`):

`payback weeks = build minutes ÷ saved per week`

180 ÷ 10 = **18 weeks**. After about 4 months the script has paid for itself, and from then on it's pure win.

**Step 4. Round up.** 17.2 weeks isn't paid back in week 17, only in week 18. Rounding **up** to the next whole number is called the **ceiling**. In Python: `math.ceil(17.2)` gives `18`.

## 🔀 What if it were different?

<div class="wrong"><b>It saves 0 minutes</b>: you'd divide by zero, which Python refuses (<code>ZeroDivisionError</code>). It never pays back, so return <code>None</code> instead.</div>
<div class="right">Saves time and is cheap to build → small number → go build it ✓</div>

Time isn't the only reason: automating something you **always forget** or that's **boring enough to make you avoid it** can be worth it even with a long payback.

## 🎯 Your quest

Write `payback_weeks(minutes_per_run, runs_per_week, build_hours)` that follows steps 1 to 4 and returns a whole number of weeks, or `None` when nothing is saved.

- `payback_weeks(2, 5, 3)` → `18`
- `payback_weeks(5, 7, 1)` → `2` (60 ÷ 35 = 1.7, rounded up)
- `payback_weeks(0, 10, 1)` → `None`

<details><summary>💡 Hint 1</summary>Start with <code>saved = minutes_per_run * runs_per_week</code>. If <code>saved == 0</code>, return <code>None</code> right away.</details>
<details><summary>💡 Hint 2</summary><code>return math.ceil(build_hours * 60 / saved)</code></details>

**Remember:** saved per week, build time in minutes, divide, round up.

## Review

<details><summary>What does math.ceil(4.1) give, and why use it here?</summary>5. A payback of 4.1 weeks only finishes in week 5, so we round up.</details>
