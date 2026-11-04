---
title: Reading CSV files
xp: 40
---
# Comma-separated, except when it isn't

> **Warm-up:** export a sheet from LibreOffice or Excel with German settings as CSV and open it in a text editor. What separates the columns?

**CSV** = "comma-separated values": one row per line, columns separated by a comma, the first line holds the column names.

```
name,city,amount
Ada,Berlin,12.50
"Smith, John",Köln,3
```

Three traps:

1. **Quotes.** `"Smith, John"` is *one* value that contains a comma. Splitting on `,` by hand breaks it. Python's `csv` module handles quotes for you.
2. **The delimiter.** German Excel writes `;` because the comma is the decimal mark (`12,50`). Always check.
3. **Encoding.** Files from Windows Excel are often `cp1252` or have a "BOM" at the start (an invisible `﻿`). Open with `encoding="utf-8-sig"` to drop it.

## Python you need

```python
import csv, io
text = "name;city\nAda;Berlin\n"
rows = list(csv.DictReader(io.StringIO(text), delimiter=";"))
# [{'name': 'Ada', 'city': 'Berlin'}]
```

`io.StringIO(text)` makes a string act like an open file. On a real file: `open(path, newline="", encoding="utf-8-sig")`.

## Your quest

1. `guess_delimiter(text)`: look at the **first line** only and return whichever of `,` `;` `\t` appears most often there.
2. `read_csv(text)`: strip a leading BOM (`﻿`) if present, guess the delimiter, and return a list of dicts using `csv.DictReader`.

**Remember:** never split CSV by hand; let `csv` deal with quotes.

## Review

<details><summary>What does a "profile" of a table count?</summary>For each column, how many values are missing or blank (lesson 01).</details>
