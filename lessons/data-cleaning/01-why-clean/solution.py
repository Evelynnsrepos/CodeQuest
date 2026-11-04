def count_empty(rows, col):
    return sum(1 for r in rows if r.get(col) is None or str(r.get(col)).strip() == "")


def profile(rows):
    if not rows:
        return {}
    return {col: count_empty(rows, col) for col in rows[0]}


rows = [
    {"name": "Ada", "city": "Berlin", "age": "36"},
    {"name": "  ", "city": "Hamburg", "age": None},
    {"name": "Linus", "city": "", "age": ""},
]
print(count_empty(rows, "name"), profile(rows))
