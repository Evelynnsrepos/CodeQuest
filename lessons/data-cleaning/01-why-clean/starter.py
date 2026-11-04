def count_empty(rows, col):
    return 0


def profile(rows):
    return {}


rows = [
    {"name": "Ada", "city": "Berlin", "age": "36"},
    {"name": "  ", "city": "Hamburg", "age": None},
    {"name": "Linus", "city": "", "age": ""},
]
print(count_empty(rows, "name"), profile(rows))
