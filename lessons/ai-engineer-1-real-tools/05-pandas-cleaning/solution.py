import io
import pandas as pd

RAW = """Bestellnr;Kunde;E-Mail;Datum;Betrag;Stadt
1001;Ada Lovelace;ada@example.de;04.11.2026;12,50 €;Köln
1002; ada lovelace ;ADA@example.de ;04.11.2026;12,50 €;koeln
1003;Linus;linus@example.de;2026-11-05;1.234,00 €;Muenchen
1004;Grace;N/A;05.11.2026;-;Berlin
1005;Test;test@example.de;31.02.2026;99999,00 €;?
"""


def clean(text):
    df = pd.read_csv(io.StringIO(text), sep=";", dtype=str, na_values=["N/A", "-", "?"])
    df = df.rename(columns={"Bestellnr": "id", "E-Mail": "email", "Datum": "date", "Betrag": "amount"})
    df["id"] = df["id"].astype(int)
    df["email"] = df["email"].str.strip().str.casefold()
    d = df["date"].str.strip()
    first = pd.to_datetime(d, format="%d.%m.%Y", errors="coerce")
    second = pd.to_datetime(d, format="%Y-%m-%d", errors="coerce")
    df["date"] = first.fillna(second)
    amount = df["amount"].str.replace("€", "").str.strip()
    amount = amount.str.replace(".", "").str.replace(",", ".")
    df["amount"] = pd.to_numeric(amount, errors="coerce")
    df = df.dropna(subset=["email", "date"])
    df = df.drop_duplicates(subset=["email", "date", "amount"], keep="first")
    df = df[["id", "email", "date", "amount"]]
    return df.reset_index(drop=True)


print(clean(RAW))
