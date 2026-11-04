import pandas as pd
cl, RAW = ns.get("clean"), ns.get("RAW")
assert cl and RAW, "Keep clean and RAW."
df = cl(RAW)
assert list(df.columns) == ["id", "email", "date", "amount"], f"Columns should be id, email, date, amount; got {list(df.columns)}."
assert list(df["id"]) == [1001, 1003], f"Rows 1001 and 1003 survive (1002 duplicate, 1004 no email, 1005 bad date). Got {list(df['id'])}."
assert list(df.index) == [0, 1], "Reset the index."
assert list(df["email"]) == ["ada@example.de", "linus@example.de"], "Emails stripped and casefolded."
assert str(df["date"].dt.date.iloc[1]) == "2026-11-05", "Parse both date formats."
assert list(df["amount"]) == [12.5, 1234.0], f"Amounts as floats, got {list(df['amount'])}."
