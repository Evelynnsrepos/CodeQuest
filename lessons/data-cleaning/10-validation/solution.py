def errors(row, schema):
    out = []
    for col, rule in schema.items():
        v = row.get(col)
        if v is None:
            if rule.get("required"):
                out.append(f"{col}: missing")
            continue
        if not isinstance(v, rule["type"]):
            out.append(f"{col}: not {rule['type'].__name__}")
            continue
        if "check" in rule and not rule["check"](v):
            out.append(f"{col}: invalid")
    return out


def split_valid(rows, schema):
    good, bad = [], []
    for r in rows:
        e = errors(r, schema)
        if e:
            bad.append((r, e))
        else:
            good.append(r)
    return good, bad


SCHEMA = {
    "email": {"type": str, "required": True, "check": lambda v: "@" in v},
    "age": {"type": int, "required": False, "check": lambda v: 0 <= v <= 120},
    "rating": {"type": int, "required": True},
}
rows = [{"email": "ada@x.de", "age": 36, "rating": 5}, {"email": "nope", "age": 150, "rating": "5"}, {"rating": 3}]
for r in rows:
    print(errors(r, SCHEMA))
