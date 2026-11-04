---
title: Why clean data?
xp: 30
---
# Garbage in, garbage out

> **Warm-up:** open any spreadsheet you've filled by hand over a few months. Is every date written the same way? Every name spelled the same?

Real data is messy because **people and programs made it**: typos, extra spaces, "N/A" in one row and an empty cell in the next, the same customer twice, a price of 99999 that was really a test. Any program you build on top of it, whether a chart, an app or an AI model, inherits every mistake.

Data scientists often say cleaning is **most** of the job. An AI model trained on duplicates learns to repeat them. A chart with one typo'd value of 1,000,000 hides every real trend.

The habit this course builds: **look first, then clean, then check.** Never clean blind.

## The plan for this course

| Step | Lesson |
|---|---|
| Read the file | 02 CSV, 11 JSON |
| Fix text | 03 spaces and case, 07 categories, 12 personal data |
| Fix values | 04 missing, 05 numbers, 06 dates |
| Remove junk | 08 duplicates, 09 outliers |
| Prove it's clean | 10 validation, 13 joins, 14 the whole pipeline |

## Python you need

A table in Python is usually a **list of dicts**: one dict per row, one key per column.

```python
rows = [{"name": "Ada", "city": "Berlin"}, {"name": "", "city": "Hamburg"}]
rows[1]["name"]   # ''
```

`value.strip() == ""` is True for empty text and text that's only spaces.

## Your quest

1. `count_empty(rows, col)`: how many rows have a missing (`None`) or blank (only spaces) value in column `col`.
2. `profile(rows)`: a dict mapping **every** column name (from the first row) to its `count_empty`.

**Remember:** look before you clean.

## Review

<details><summary>Why does cleaning matter for AI models?</summary>The model learns from every example, including the mistakes: duplicates get extra weight, wrong labels teach wrong answers.</details>
