---
title: Dates in every format
xp: 50
---
# 04.11.2026, 11/04/2026, 2026-11-04

> **Warm-up:** what date is `03/04/2026`? Ask a German and an American.

Dates are the worst column. One file may contain `04.11.2026` (German), `11/04/2026` (US: month first!), `2026-11-04` (ISO) and `4 Nov 2026`. The fix:

1. Agree on **one** output format: **ISO 8601**, `YYYY-MM-DD`. It sorts correctly as text, every tool reads it, and nobody misreads it.
2. Try a **list of known formats** in order and take the first that works.
3. If none works, return `None` and **look** at those rows. Don't invent a date.

Ambiguity: `03/04/2026` fits both `%m/%d/%Y` and `%d/%m/%Y`. Whichever comes first in your list wins, so the order of the list is a decision about your data. Write it down.

## The format codes

| Code | Means | Example |
|---|---|---|
| `%Y` | 4-digit year | 2026 |
| `%m` | month 01–12 | 11 |
| `%d` | day 01–31 | 04 |
| `%b` | short month name (English) | Nov |

## Python you need

```python
from datetime import datetime
datetime.strptime("04.11.2026", "%d.%m.%Y").date().isoformat()   # '2026-11-04'
```

`strptime` raises `ValueError` when the text doesn't match, including impossible dates like `31.02.2026`.

## Your quest

`FORMATS` is given. `to_iso(s, formats=FORMATS)`: tidy the text (strip), try each format in order, return the ISO string of the first match, or `None`.

Then `bad_dates(values)`: the list of **indexes** of values that are not blank but couldn't be parsed (the rows you need to look at).

**Remember:** store dates as YYYY-MM-DD; write down how you read ambiguous ones.

## Review

<details><summary>How do you parse "1.234,56" correctly?</summary>Know the file uses "," as the decimal mark: remove "." then replace "," with ".".</details>
