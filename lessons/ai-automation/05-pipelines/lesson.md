---
title: Pipelines: small steps in a row
xp: 25
---
# Chain steps instead of one giant prompt

⏱️ About 10 minutes · one function

> **Warm-up:** one prompt "read this invoice, find the total, convert it to euros and write an email" fails sometimes. Which part failed?

**In one sentence:** a **pipeline** is a list of small steps where each step's output is the next step's input, so you can test and fix each step alone.

## 🪜 Plain words

```
text ──► extract_total ──► to_euros ──► write_email ──► done
```

Some steps are model calls, some are plain code (converting money is a job for code, not a model). In Python, functions are values, so a pipeline can simply be a **list of functions**:

```python
value = start
for step in steps:
    value = step(value)
```

Every function has a name: `step.__name__` is `"extract_total"`. Use it in error messages so you know **which** step broke.

## 🔀 What if it were different?

<div class="wrong"><b>A step returns <code>None</code></b> (the model found nothing) and the next step crashes with a confusing error about <code>None</code>.</div>
<div class="right">Stop right there and say which step gave nothing ✓</div>

## 🎯 Your quest

Write `run_pipeline(value, steps)`:

- pass `value` through each step in order and return the final value
- if a step returns `None`, raise `RuntimeError("step extract_total gave nothing")` (with that step's name)

<details><summary>💡 Hint</summary>Inside the loop: <code>value = step(value)</code>, then <code>if value is None: raise RuntimeError(f"step {step.__name__} gave nothing")</code>.</details>

**Remember:** small steps, one input, one output, fail at the step that broke.

## Review

<details><summary>Lesson 4: what goes inside the try in a batch?</summary>The work for one item only, so one failure doesn't stop the loop.</details>
