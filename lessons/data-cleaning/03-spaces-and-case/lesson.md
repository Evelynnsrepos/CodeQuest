---
title: Spaces, case and invisible characters
xp: 40
---
# "Berlin", "berlin " and "BERLIN"

> **Warm-up:** how many different cities are in this list: `["Berlin", "berlin ", " BERLIN", "Ber lin"]`?

To a computer those are four different strings. To you it's one city (and a typo). The first cleaning step for any text column:

1. **Strip** spaces at both ends: `" Berlin ".strip()` → `"Berlin"`.
2. **Collapse** runs of spaces, tabs and line breaks inside into one space: `" ".join(s.split())`.
3. For **comparing** (not for displaying), ignore case with `casefold()`. It's like `lower()` but also handles German: `"STRASSE".casefold() == "straße".casefold()` → `True`.

Invisible troublemakers: the **non-breaking space** `\xa0` (copied from websites) and the **zero-width space** `​`. `split()` already treats `\xa0` as a space, but not `​`, so remove it explicitly.

## Python you need

```python
" ".join("  a \t b\n".split())   # 'a b'
"Straße".casefold()              # 'strasse'
s.replace("​", "")
```

## Your quest

1. `tidy(s)`: remove zero-width spaces, strip, and collapse inner whitespace to single spaces. `None` stays `None`.
2. `key(s)`: `tidy(s)` then `casefold()`, the form you use to **compare** values.
3. `distinct(values)`: how many different values there are after `key` (ignore `None`).

**Remember:** tidy for display, casefold for comparing.

## Review

<details><summary>Why is CSV in Germany often separated by semicolons?</summary>The comma is the decimal mark there (12,50), so it can't also separate columns.</details>
