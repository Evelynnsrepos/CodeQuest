import unicodedata


def fold(s):
    return s


def canonical(s, mapping):
    return None


def unknowns(values, mapping):
    return []


CITY = {"koeln": "Köln", "cologne": "Köln", "munich": "München", "muenchen": "München"}
vals = ["Köln", " KOELN", "cologne", "Munchen", "München ", "Berlin", ""]
print([canonical(v, CITY) for v in vals], unknowns(vals, CITY))
