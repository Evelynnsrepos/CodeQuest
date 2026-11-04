---
title: pandas: tables that think
xp: 55
---
# A spreadsheet you can program

> **Warm-up:** in the Data cleaning course you wrote `read_csv`, `parse_number` and `left_join` by hand. How many lines was that?

**pandas** gives you a **DataFrame**: a table with named columns, each column a NumPy array. Everything you built by hand is one call:

```python
import pandas as pd, io
df = pd.read_csv(io.StringIO(text), sep=";", decimal=",")   # German CSV
df.head()                      # first 5 rows
df["Betrag"].sum()             # a column is a "Series"
df[df["Betrag"] > 10]          # filter rows with a True/False mask
df.groupby("Stadt")["Betrag"].sum()       # total per city
df.sort_values("Betrag", ascending=False)
df.merge(customers, on="kunde_id", how="left")   # left join
```

`groupby` = "split into groups, apply a function, combine the results". It answers most "per X" questions.

## Your quest

The starter has `SALES`, a German CSV string of a café's sales (`Datum;Produkt;Menge;Preis`).

1. `load(text)`: a DataFrame from the CSV (semicolons, decimal comma), plus a new column `Umsatz` = `Menge * Preis`.
2. `per_product(df)`: a **Series** of total `Umsatz` per `Produkt`, sorted from biggest to smallest.
3. `best_day(df)`: the `Datum` (string) with the highest total `Umsatz`.

**Remember:** filter with masks, summarize with `groupby`.

## Review

<details><summary>What is the causal mask for?</summary>So a token can't attend to later tokens: scores above the diagonal become −∞ before softmax.</details>
