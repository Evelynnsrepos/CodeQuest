---
title: pandas: tables that think
minutes: 35
xp: 55
hint: load: df = pd.read_csv(io.StringIO(text), sep=";", decimal=","), then df["Umsatz"] = df["Menge"] * df["Preis"], then return df
hint: per_product: totals = df.groupby("Produkt")["Umsatz"].sum(), then return totals.sort_values(ascending=False)
hint: best_day: totals = df.groupby("Datum")["Umsatz"].sum(), then return str(totals.idxmax())
---
# A spreadsheet you can program

⏱️ About 35 minutes

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

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `io.StringIO(text)` | | makes a text look like a file, because `read_csv` wants a file |
| `sep=";"`, `decimal=","` | | German CSV: columns split by `;`, and `2,90` means 2.90 |
| `df["Menge"] * df["Preis"]` | | multiplies two whole columns, row by row, with no loop |
| `df["Umsatz"] = ...` | | adds a new column |
| `df.groupby("Produkt")["Umsatz"].sum()` | "group by product, take Umsatz, sum" | one total per product |
| `.sort_values(ascending=False)` | | biggest first |
| `.idxmax()` | "index of the max" | the **label** (here the date) of the biggest total |

### 👀 Worked example: groupby by hand

Rows: (Kaffee, 87.0), (Kuchen, 42.0), (Kaffee, 118.9).

1. **Split** by product: Kaffee → 87.0 and 118.9. Kuchen → 42.0.
2. **Apply** `sum`: Kaffee 205.9, Kuchen 42.0.
3. **Combine** into one Series with the product as the label: `Kaffee 205.9, Kuchen 42.0`.

`.idxmax()` on that gives `"Kaffee"`, the label of the biggest number.

## 🎯 Your quest

The starter has `SALES`, a German CSV string of a café's sales (`Datum;Produkt;Menge;Preis`).

1. `load(text)`: a DataFrame from the CSV (semicolons, decimal comma), plus a new column `Umsatz` = `Menge * Preis`.
2. `per_product(df)`: a **Series** of total `Umsatz` per `Produkt`, sorted from biggest to smallest.
3. `best_day(df)`: the `Datum` (string) with the highest total `Umsatz`.

**Part 1:** `load`. Replace `return pd.DataFrame()` with:

1. `df = pd.read_csv(io.StringIO(text), sep=";", decimal=",")`
2. `df["Umsatz"] = df["Menge"] * df["Preis"]`
3. `return df`

**Part 2:** `per_product`. Replace its `return` line with:

1. `totals = df.groupby("Produkt")["Umsatz"].sum()`
2. `return totals.sort_values(ascending=False)`

**Part 3:** `best_day`. Replace `return ""` with:

1. `totals = df.groupby("Datum")["Umsatz"].sum()`
2. `return str(totals.idxmax())`

**Remember:** filter with masks, summarize with `groupby`.

## Review

<details><summary>What is the causal mask for?</summary>So a token can't attend to later tokens: scores above the diagonal become −∞ before softmax.</details>
