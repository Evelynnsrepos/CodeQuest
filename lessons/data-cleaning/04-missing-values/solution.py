import statistics

MISSING = {"", "na", "n/a", "null", "none", "-", "?", "unknown"}


def is_missing(v):
    return v is None or (isinstance(v, str) and v.strip().casefold() in MISSING)


def normalize_missing(rows):
    return [{k: (None if is_missing(v) else v) for k, v in r.items()} for r in rows]


def fill_median(rows, col):
    known = [r[col] for r in rows if r[col] is not None]
    m = statistics.median(known)
    return [dict(r, **{col: m}) if r[col] is None else dict(r) for r in rows]


def drop_missing(rows, cols):
    return [r for r in rows if all(r.get(c) is not None for c in cols)]


rows = [{"name": "Ada", "age": "N/A"}, {"name": "-", "age": "34"}, {"name": "Lin", "age": " "}]
print(normalize_missing(rows))
print(fill_median([{"x": 1}, {"x": None}, {"x": 100}, {"x": 3}], "x"))
