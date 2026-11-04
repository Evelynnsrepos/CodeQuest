import statistics

MISSING = {"", "na", "n/a", "null", "none", "-", "?", "unknown"}


def is_missing(v):
    return False


def normalize_missing(rows):
    return rows


def fill_median(rows, col):
    return rows


def drop_missing(rows, cols):
    return rows


rows = [{"name": "Ada", "age": "N/A"}, {"name": "-", "age": "34"}, {"name": "Lin", "age": " "}]
print(normalize_missing(rows))
print(fill_median([{"x": 1}, {"x": None}, {"x": 100}, {"x": 3}], "x"))
