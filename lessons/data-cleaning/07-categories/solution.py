import unicodedata


def fold(s):
    s = " ".join(s.split()).casefold()
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def canonical(s, mapping):
    f = fold(s)
    if f in mapping:
        return mapping[f]
    for value in mapping.values():
        if fold(value) == f:
            return value
    return None


def unknowns(values, mapping):
    return sorted({fold(v) for v in values if v and v.strip() and canonical(v, mapping) is None})


CITY = {"koeln": "Köln", "cologne": "Köln", "munich": "München", "muenchen": "München"}
vals = ["Köln", " KOELN", "cologne", "Munchen", "München ", "Berlin", ""]
print([canonical(v, CITY) for v in vals], unknowns(vals, CITY))
