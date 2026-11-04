---
title: Missing values
xp: 45
---
# Empty, "N/A", "-", "null", "?"

> **Warm-up:** in a survey export, the age column contains `"34"`, `""`, `"N/A"`, `"-"`, `"unknown"`. Which of these are real ages?

Missing data shows up in many disguises. Step one is to turn **every** disguise into one honest value: Python's `None`. Then decide what to do, column by column:

| Choice | When | Risk |
|---|---|---|
| **Drop the row** | the column is essential (no price → useless order) | you lose data; if missing isn't random, you bias the result |
| **Fill with a default** | there's a sensible neutral value (`0` items, `"unknown"` category) | a fake 0 can drag averages down |
| **Fill with the median** | numbers, a few gaps | hides that it was missing; add a flag column if it matters |
| **Leave as None** | the next step can handle it | code that does math on it crashes, which is good: loud is better than wrong |

Why **median** and not mean? One huge value pulls the mean but not the median (the middle value when sorted).

## Python you need

```python
MISSING = {"", "na", "n/a", "null", "none", "-", "?", "unknown"}
v.strip().casefold() in MISSING
import statistics; statistics.median([3, 1, 100])   # 3
```

## Your quest

1. `is_missing(v)`: `True` for `None` or any string whose stripped, casefolded form is in `MISSING`.
2. `normalize_missing(rows)`: new rows where every missing value is `None` (other values unchanged).
3. `fill_median(rows, col)`: new rows where `None` in `col` is replaced by the **median** of the other values in that column (they're numbers already).
4. `drop_missing(rows, cols)`: keep only rows where **none** of `cols` is `None`.

**Remember:** first make all the "missings" look the same, then choose what to do.

## Review

<details><summary>Why compare with casefold()?</summary>So "N/A", "n/a" and "N/a" all match one rule (lesson 03).</details>
