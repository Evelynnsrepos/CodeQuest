import re, unicodedata

EMAIL = r"[\w.+-]+@[\w-]+(\.[\w-]+)+"
IBAN = r"\b[A-Z]{2}\d{2}(?: ?[A-Z0-9]{4}){3,7}(?: ?[A-Z0-9]{1,4})?\b"
PHONE = r"\+?\d[\d /-]{7,}\d"


def clean_text(s):
    s = unicodedata.normalize("NFC", s)
    return "".join(c for c in s if c in "\n\t" or unicodedata.category(c) != "Cc")


def _redact(s):
    counts = {}
    for name, pattern in (("EMAIL", EMAIL), ("IBAN", IBAN), ("PHONE", PHONE)):
        s, counts[name] = re.subn(pattern, f"[{name}]", s)
    return s, counts


def redact(s):
    return _redact(s)[0]


def pii_counts(s):
    return _redact(s)[1]


msg = "Hi, I'm Ada (ada.l+news@mail.example.de, +49 170 1234567).\x00 Please refund to DE89 3704 0044 0532 0130 00."
print(redact(clean_text(msg)))
print(pii_counts(msg))
