import pandas as pd
ld, pp, bd, SALES = ns.get("load"), ns.get("per_product"), ns.get("best_day"), ns.get("SALES")
assert ld and pp and bd and SALES, "Keep load, per_product, best_day and SALES."
df = ld(SALES)
assert isinstance(df, pd.DataFrame) and len(df) == 6, "load: 6 rows."
assert df["Preis"].dtype.kind == "f", "load: Preis must be numbers. Use decimal=','."
assert "Umsatz" in df and abs(df["Umsatz"].sum() - 412.0) < 1e-6, f"Umsatz = Menge × Preis; total should be 412.00, got {df['Umsatz'].sum() if 'Umsatz' in df else None}."
s = pp(df)
assert isinstance(s, pd.Series) and list(s.index) == ["Kaffee", "Kuchen", "Tee"], f"per_product: sorted biggest first, got {list(s.index)}."
assert abs(s["Kaffee"] - 278.4) < 1e-6, "Kaffee: 96 cups × 2.90 = 278.40."
assert bd(df) == "2026-11-04", f"best_day: 2026-11-04 (142.50), got {bd(df)!r}."
