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


def clean_orders(text):
    return [], {"read": 0, "rejected": [], "duplicates": [], "kept": 0}


clean, report = clean_orders(RAW)
for row in clean:
    print(row)
print(report)
