import io
import pandas as pd

SALES = """Datum;Produkt;Menge;Preis
2026-11-02;Kaffee;30;2,90
2026-11-02;Kuchen;12;3,50
2026-11-03;Kaffee;41;2,90
2026-11-03;Tee;9;2,40
2026-11-04;Kaffee;25;2,90
2026-11-04;Kuchen;20;3,50
"""


def load(text):
    df = pd.read_csv(io.StringIO(text), sep=";", decimal=",")
    df["Umsatz"] = df["Menge"] * df["Preis"]
    return df


def per_product(df):
    totals = df.groupby("Produkt")["Umsatz"].sum()
    return totals.sort_values(ascending=False)


def best_day(df):
    totals = df.groupby("Datum")["Umsatz"].sum()
    return str(totals.idxmax())


df = load(SALES)
print(df)
print(per_product(df))
print(best_day(df))
