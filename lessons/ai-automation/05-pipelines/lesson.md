---
title: Pipelines: small steps in a row
minutes: 20
xp: 25
hint: Loop over the steps: for step in steps: and inside it value = step(value)
hint: Still inside the loop: if value is None: and under it raise RuntimeError("step " + step.__name__ + " gave nothing")
hint: After the loop (back at 4 spaces): return value
---
# Chain steps instead of one giant prompt

⏱️ About 20 minutes · one function, five lines

> **Warm-up:** one prompt "read this invoice, find the total, convert it to euros and write an email" fails sometimes. Which part failed?

**In one sentence:** a **pipeline** is a list of small steps where each step's output is the next step's input, so you can test and fix each step alone.

## 🪜 Plain words

```
text ──► extract_total ──► to_euros ──► write_email ──► done
```

The arrows mean "the answer goes into the next step". Some steps are model calls, some are plain code (converting money is a job for code, not a model: code never gets maths wrong).

In Python a function can be put into a list like any other value. So a pipeline can simply be a **list of functions**: `[extract_total, to_euros, write_email]`. Note: no brackets `()` after the names. `to_euros` is the function itself, `to_euros(5)` would **run** it.

## 🔀 What if it were different?

<div class="wrong"><b>A step gives back <code>None</code></b> (the model found nothing), and the next step crashes with a confusing error about <code>None</code>. You don't know which step went wrong.</div>
<div class="right">Stop right there and say <b>which</b> step gave nothing ✓</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `for step in steps:` | "for each step in steps" | goes through the list one function at a time. Each time, the function is in the box `step`. |
| `value = step(value)` | "value becomes step of value" | runs the function on the current value and puts the answer back in the same box. The next round uses that new value. |
| `if value is None:` | "if value is none" | true only when the value is `None` ("nothing"). Use `is` for `None`, not `==`. A real `0` or `""` is **not** `None`. |
| `step.__name__` | "step's name" | the function's name as text, like `"extract_total"`. Two underscores on each side. |
| `raise RuntimeError("...")` | "raise a runtime error" | stops with your own error message |
| `"step " + name + " gave nothing"` | | glues three texts together |

### 👀 Worked example: a recipe pipeline

```python
def add_two(x):
    return x + 2

def times_ten(x):
    return x * 10

def run_all(value, steps):
    for step in steps:
        value = step(value)
    return value

print(run_all(1, [add_two, times_ten]))
```

`run_all(1, [add_two, times_ten])`, round by round:

1. Start: `value` = 1.
2. Round 1: `step` is `add_two`. `value = add_two(1)` = **3**.
3. Round 2: `step` is `times_ten`. `value = times_ten(3)` = **30**.
4. The list is done. Return **30**.

With the order swapped, `[times_ten, add_two]`: 1 × 10 = 10, then 10 + 2 = **12**. Order matters.

Your quest is `run_all` plus a check after every step.

## 🎯 Your quest

Write `run_pipeline(value, steps)`. Replace the starter's `return value` with:

1. `for step in steps:`
2. `    value = step(value)`
3. `    if value is None:`
4. `        raise RuntimeError("step " + step.__name__ + " gave nothing")`
5. `return value` (back at 4 spaces, after the loop)

If `extract_total` gave `None`, the error says `step extract_total gave nothing`, and you know exactly where to look.

**Remember:** small steps, one input, one output, fail at the step that broke.

## Review

<details><summary>Lesson 4: what goes inside the try in a batch?</summary>The work for one item only, so one failure doesn't stop the loop.</details>
<details><summary>Why write "is None" and not just check if the value is empty?</summary>0 or an empty text can be real answers. Only None means "this step found nothing".</details>
