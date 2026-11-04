---
title: Cleaning with pandas
xp: 60
---
# The shop export again, in ten lines

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

## Your quest

`clean(text)` for the shop export in the starter. Return a DataFrame with columns `id, email, date, amount` (rename from `Bestellnr, E-Mail, Datum, Betrag`), where:

- emails are stripped and casefolded; dates are parsed with `%d.%m.%Y` **or** `%Y-%m-%d`; amounts are floats;
- rows with a missing email or date are dropped; then duplicates on `email, date, amount` are dropped (keep first);
- the index is reset (`reset_index(drop=True)`).

**Remember:** `errors="coerce"`, then deal with the missing values on purpose.

## Review

<details><summary>What does groupby do?</summary>Splits rows into groups by a column, applies a function per group, and combines the results.</details>
