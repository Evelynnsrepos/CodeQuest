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
    return pd.DataFrame()


print(clean(RAW))
