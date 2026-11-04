def errors(row, schema):
    return []


def split_valid(rows, schema):
    return rows, []


SCHEMA = {
    "email": {"type": str, "required": True, "check": lambda v: "@" in v},
    "age": {"type": int, "required": False, "check": lambda v: 0 <= v <= 120},
    "rating": {"type": int, "required": True},
}
rows = [{"email": "ada@x.de", "age": 36, "rating": 5}, {"email": "nope", "age": 150, "rating": "5"}, {"rating": 3}]
for r in rows:
    print(errors(r, SCHEMA))
