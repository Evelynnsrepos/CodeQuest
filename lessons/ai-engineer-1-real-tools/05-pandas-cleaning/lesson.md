---
title: Cleaning with pandas
minutes: 50
xp: 60
hint: Read every column as text (dtype=str) with na_values, then rename the four columns with df.rename(columns={...})
hint: Dates: parse twice, first = pd.to_datetime(d, format="%d.%m.%Y", errors="coerce") and second with "%Y-%m-%d", then first.fillna(second)
hint: Amount: remove € and spaces, then remove the thousands dot and turn the comma into a dot, then pd.to_numeric(amount, errors="coerce")
hint: End: dropna(subset=["email", "date"]), drop_duplicates(...), keep the four columns, reset_index(drop=True)
---
# The shop export again, in ten lines

⏱️ About 50 minutes

> **Warm-up:** recall the checkpoint of the Data cleaning course. What were the seven steps?

The same pipeline in pandas:

```python
df = pd.read_csv(io.StringIO(text), sep=";", decimal=",", na_values=["N/A", "-", "?"])
df["E-Mail"] = df["E-Mail"].str.strip().str.casefold()        # .str = string methods on a column
df["Datum"] = pd.to_datetime(df["Datum"], format="%d.%m.%Y", errors="coerce")   # bad → NaT
df["Betrag"] = pd.to_numeric(df["Betrag"].str.replace("€", "").str.replace(".", "").str.replace(",", "."), errors="coerce")
df.isna().sum()                      # missing per column (lesson 01's profile)
df.dropna(subset=["E-Mail", "Datum"])
df.drop_duplicates(subset=["E-Mail", "Datum", "Betrag"], keep="first")
```

`errors="coerce"` turns anything unparseable into a missing value (`NaN` for numbers, `NaT` for dates) instead of crashing. Then `dropna` or a report deals with it, the same idea as lesson 04 of Data cleaning.

**Watch out:** `na_values` turns *those exact* strings into missing at read time. Strings with spaces around them (`" N/A "`) won't match; add `skipinitialspace=True` or clean afterwards.

**Mixed date formats:** `format=` handles one format. For a column with two, parse twice and combine: `a.fillna(b)`.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `dtype=str` | | read every column as text first, so nothing is guessed wrong |
| `na_values=["N/A", "-", "?"]` | | these texts become "missing" (`NaN`) |
| `df.rename(columns={"E-Mail": "email", ...})` | | new names for the columns |
| `.astype(int)` | | text `"1001"` → number 1001 |
| `.str.strip()`, `.str.casefold()` | | string methods on a whole column: remove outer spaces, make lower case |
| `pd.to_datetime(d, format="%d.%m.%Y", errors="coerce")` | | `%d` = day, `%m` = month, `%Y` = 4-digit year. A text that doesn't fit becomes `NaT` ("not a time") |
| `first.fillna(second)` | "fill the gaps in first from second" | where `first` is missing, take the value from `second` |
| `.str.replace(".", "")` | | removes the thousands dot: `1.234,00` → `1234,00` |
| `.str.replace(",", ".")` | | `1234,00` → `1234.00` |
| `pd.to_numeric(x, errors="coerce")` | | text → number, missing if it can't |
| `df[["id", "email", "date", "amount"]]` | | double brackets: keep only these columns, in this order |

### 👀 Worked example: one amount, step by step

`" 1.234,00 € "`:

1. `.str.replace("€", "")` → `" 1.234,00  "`.
2. `.str.strip()` → `"1.234,00"`.
3. `.str.replace(".", "")` → `"1234,00"`.
4. `.str.replace(",", ".")` → `"1234.00"`.
5. `pd.to_numeric` → **1234.0**. And `"-"` was already missing from `na_values`, so it stays missing.

And a date `"2026-11-05"`: the first format `%d.%m.%Y` doesn't fit → `NaT`. The second `%Y-%m-%d` fits → 5 Nov 2026. `fillna` takes it from the second. `"31.02.2026"` fits neither (there's no 31 February) → stays `NaT` and the row is dropped.

## 🎯 Your quest

`clean(text)` for the shop export in the starter. Return a DataFrame with columns `id, email, date, amount` (rename from `Bestellnr, E-Mail, Datum, Betrag`), where:

- emails are stripped and casefolded; dates are parsed with `%d.%m.%Y` **or** `%Y-%m-%d`; amounts are floats;
- rows with a missing email or date are dropped; then duplicates on `email, date, amount` are dropped (keep first);
- the index is reset (`reset_index(drop=True)`).

Replace `return pd.DataFrame()` with:

1. `df = pd.read_csv(io.StringIO(text), sep=";", dtype=str, na_values=["N/A", "-", "?"])`
2. `df = df.rename(columns={"Bestellnr": "id", "E-Mail": "email", "Datum": "date", "Betrag": "amount"})`
3. `df["id"] = df["id"].astype(int)`
4. `df["email"] = df["email"].str.strip().str.casefold()`
5. `d = df["date"].str.strip()`
6. `first = pd.to_datetime(d, format="%d.%m.%Y", errors="coerce")`
7. `second = pd.to_datetime(d, format="%Y-%m-%d", errors="coerce")`
8. `df["date"] = first.fillna(second)`
9. `amount = df["amount"].str.replace("€", "").str.strip()`
10. `amount = amount.str.replace(".", "").str.replace(",", ".")`
11. `df["amount"] = pd.to_numeric(amount, errors="coerce")`
12. `df = df.dropna(subset=["email", "date"])`
13. `df = df.drop_duplicates(subset=["email", "date", "amount"], keep="first")`
14. `df = df[["id", "email", "date", "amount"]]`
15. `return df.reset_index(drop=True)`

**Remember:** `errors="coerce"`, then deal with the missing values on purpose.

## Review

<details><summary>What does groupby do?</summary>Splits rows into groups by a column, applies a function per group, and combines the results.</details>
