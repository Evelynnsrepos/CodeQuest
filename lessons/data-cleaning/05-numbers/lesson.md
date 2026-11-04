---
title: Numbers written by humans
xp: 50
---
# 1.234,56 or 1,234.56?

> **Warm-up:** what number is `"1.234"`? In Germany it's one thousand two hundred thirty-four. In the US it's one point two three four.

Text that *looks* like a number needs converting before you can add it. People write numbers with:

- **Currency signs**: `€12`, `12 €`, `$3.50`
- **Percent**: `12%` (do you want 12 or 0.12? Decide and document it.)
- **Thousands separators**: `1,234,567` (US) or `1.234.567` (DE) or `1 234 567` (FR, with a normal or non-breaking space)
- **Decimal marks**: `.` (US, UK) or `,` (Germany, most of Europe)

You can't always guess. `"1,234"` could be 1234 (US) or 1.234 (DE). So the function takes the **decimal mark** as a setting: you find out once per file (lesson 02: semicolon-separated files are usually German) and pass it in.

## Python you need

```python
s.replace(".", "").replace(",", ".")   # German → Python: '1.234,56' → '1234.56'
float("1234.56")                       # 1234.56
try: float(s)
except ValueError: ...                 # not a number
```

## Your quest

`parse_number(s, decimal=".")`:
1. `None` or blank → `None`.
2. Remove `€`, `$`, `£`, normal spaces and `\xa0`.
3. If `decimal == ","`: remove `.` (thousands) then turn `,` into `.`. Otherwise remove `,` (thousands).
4. A trailing `%` is removed and the number divided by 100.
5. Return a `float`, or `None` if it still isn't a number.

**Remember:** one file, one decimal mark: find it out, don't guess per value.

## Review

<details><summary>Why fill missing numbers with the median rather than the mean?</summary>One extreme value pulls the mean a lot but barely moves the median.</details>
