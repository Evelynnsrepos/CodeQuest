def duplicate_keys(rows, key):
    seen, dup = set(), set()
    for r in rows:
        k = str(r[key]).strip()
        (dup if k in seen else seen).add(k)
    return sorted(dup)


def left_join(left, right, left_key, right_key):
    by_id = {str(r[right_key]).strip(): r for r in right}
    cols = [c for r in right for c in r if c != right_key]
    cols = list(dict.fromkeys(cols))
    out = []
    for row in left:
        match = by_id.get(str(row[left_key]).strip())
        extra = {c: (match.get(c) if match else None) for c in cols}
        out.append({**row, **extra})
    return out


def orphans(left, right, left_key, right_key):
    ids = {str(r[right_key]).strip() for r in right}
    return [row for row in left if str(row[left_key]).strip() not in ids]


customers = [{"id": 1, "city": "Berlin"}, {"id": 2, "city": "Köln"}]
orders = [{"order": "A", "customer_id": "1"}, {"order": "B", "customer_id": " 2"}, {"order": "C", "customer_id": "9"}]
print(left_join(orders, customers, "customer_id", "id"))
print(orphans(orders, customers, "customer_id", "id"), duplicate_keys(customers + [{"id": "1"}], "id"))
