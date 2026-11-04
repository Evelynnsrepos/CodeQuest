import re, unicodedata

EMAIL = r"[\w.+-]+@[\w-]+(\.[\w-]+)+"
IBAN = r"\b[A-Z]{2}\d{2}(?: ?[A-Z0-9]{4}){3,7}(?: ?[A-Z0-9]{1,4})?\b"
PHONE = r"\+?\d[\d /-]{7,}\d"


def clean_text(s):
    return s


def redact(s):
    return s


def pii_counts(s):
    return {"EMAIL": 0, "IBAN": 0, "PHONE": 0}


msg = "Hi, I'm Ada (ada.l+news@mail.example.de, +49 170 1234567).\x00 Please refund to DE89 3704 0044 0532 0130 00."
print(redact(clean_text(msg)))
print(pii_counts(msg))
