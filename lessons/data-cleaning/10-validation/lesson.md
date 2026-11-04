---
title: Validation: prove it's clean
xp: 55
---
# Rules your data must follow

> **Warm-up:** write down three rules every row of a customer table should follow.

After cleaning, **check** every row against explicit rules, a **schema**. A schema says, per column: is it required, what type is it, and what extra rule applies (age between 0 and 120, email contains `@`, rating in 1..5).

Rows that break a rule go to a **reject pile** with the reason, never silently away. Then you can count them ("3% rejected, mostly missing emails") and fix the source.

This is exactly what tools like **pydantic** and **pandera** do; real APIs (and the structured-output lesson in LLMs 9) use the same idea to check what an LLM returns.

## The schema format in this lesson

```python
SCHEMA = {
    "email":  {"type": str, "required": True,  "check": lambda v: "@" in v},
    "age":    {"type": int, "required": False, "check": lambda v: 0 <= v <= 120},
    "rating": {"type": int, "required": True},
}
```

## Your quest

1. `errors(row, schema)`: a list of error strings, checking each column **in schema order**:
   - missing (`None` or key absent) and required → `"<col>: missing"`; missing and optional → no error;
   - wrong type (`not isinstance(v, type)`) → `"<col>: not <typename>"` (use `t.__name__`) and skip its check;
   - `check` present and returns False → `"<col>: invalid"`.
2. `split_valid(rows, schema)`: `(good, bad)` where `bad` is a list of `(row, errors)` pairs.

**Remember:** rejected rows get a reason, not a silent delete.

## Review

<details><summary>Why are quartile fences more robust than z-scores?</summary>A big outlier inflates the mean and standard deviation and can hide itself; quartiles barely move.</details>
