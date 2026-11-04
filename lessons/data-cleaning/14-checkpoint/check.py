co, RAW = ns.get("clean_orders"), ns.get("RAW")
assert co and RAW, "Keep clean_orders and RAW."
clean, report = co(RAW)
want = [
    {"id": 1001, "customer": "Ada Lovelace", "email": "ada@example.de", "date": "2026-11-04", "amount": 12.5, "city": "Köln"},
    {"id": 1003, "customer": "Linus", "email": "linus@example.de", "date": "2026-11-05", "amount": 1234.0, "city": "München"},
]
assert len(clean) == 2, f"Two rows should survive (1001 and 1003), got {len(clean)}."
for got, w in zip(clean, want):
    for k, v in w.items():
        assert got.get(k) == v, f"Order {w['id']}: {k} should be {v!r}, got {got.get(k)!r}."
assert report == {"read": 5, "rejected": [1004, 1005], "duplicates": [1002], "kept": 2}, f"Got report {report!r}."
bom = "\ufeff" + RAW.replace(";Köln", ";Cologne")
clean2, _ = co(bom)
assert clean2 and clean2[0]["city"] == "Köln", "Strip a BOM, and map 'Cologne' through CITY."
