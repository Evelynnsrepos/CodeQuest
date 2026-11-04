import csv, io, unicodedata
from datetime import datetime

RAW = """Bestellnr;Kunde;E-Mail;Datum;Betrag;Stadt
1001;Ada Lovelace;ada@example.de;04.11.2026;12,50 €;Köln
1002; ada lovelace ;ADA@example.de;04.11.2026;12,50 €;koeln
1003;Linus;linus@example.de;2026-11-05;1.234,00 €;Muenchen
1004;Grace;N/A;05.11.2026;-;Berlin
1005;Test;test@example.de;31.02.2026;99999,00 €;?
"""
MISSING = {"", "na", "n/a", "null", "none", "-", "?", "unknown"}
FORMATS = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y", "%m/%d/%Y", "%d %b %Y"]
CITY = {"koeln": "Köln", "cologne": "Köln", "muenchen": "München", "munich": "München", "berlin": "Berlin"}


def tidy(s):
    return " ".join(s.replace("\u200b", "").split())


def fold(s):
    s = tidy(s).casefold()
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def number(s):
    s = s.replace("€", "").replace(" ", "").replace("\xa0", "").replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def iso(s):
    for f in FORMATS:
        try:
            return datetime.strptime(s, f).date().isoformat()
        except ValueError:
            pass
    return None


def city(s):
    f = fold(s)
    if f in CITY:
        return CITY[f]
    return next((v for v in CITY.values() if fold(v) == f), None)


def clean_orders(text):
    text = text.lstrip("\ufeff")
    first = text.split("\n", 1)[0]
    delim = max([",", ";", "\t"], key=first.count)
    raw = list(csv.DictReader(io.StringIO(text), delimiter=delim))
    rows = [{k: (None if v is None or v.strip().casefold() in MISSING else tidy(v)) for k, v in r.items()} for r in raw]
    report = {"read": len(raw), "rejected": [], "duplicates": [], "kept": 0}
    seen, clean = set(), []
    for r in rows:
        row = {
            "id": int(r["Bestellnr"]),
            "customer": r["Kunde"],
            "email": r["E-Mail"].casefold() if r["E-Mail"] else None,
            "date": iso(r["Datum"]) if r["Datum"] else None,
            "amount": number(r["Betrag"]) if r["Betrag"] else None,
            "city": city(r["Stadt"]) if r["Stadt"] else None,
        }
        if row["email"] is None or row["date"] is None:
            report["rejected"].append(row["id"])
            continue
        key = (row["email"], row["date"], row["amount"])
        if key in seen:
            report["duplicates"].append(row["id"])
            continue
        seen.add(key)
        clean.append(row)
    report["kept"] = len(clean)
    return clean, report


clean, report = clean_orders(RAW)
for row in clean:
    print(row)
print(report)
