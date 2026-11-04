dk, lj, orph = ns.get("duplicate_keys"), ns.get("left_join"), ns.get("orphans")
assert dk and lj and orph, "Keep duplicate_keys, left_join and orphans."
customers = [{"id": 1, "city": "Berlin"}, {"id": 2, "city": "Köln"}]
orders = [{"order": "A", "customer_id": "1"}, {"order": "B", "customer_id": " 2"}, {"order": "C", "customer_id": "9"}]
assert dk(customers + [{"id": " 1"}, {"id": 2}, {"id": 3}], "id") == ["1", "2"], "duplicate_keys: compare as stripped strings, sorted."
j = lj(orders, customers, "customer_id", "id")
assert j == [{"order": "A", "customer_id": "1", "city": "Berlin"}, {"order": "B", "customer_id": " 2", "city": "Köln"},
             {"order": "C", "customer_id": "9", "city": None}], f"Got {j!r}."
assert orders[0] == {"order": "A", "customer_id": "1"}, "Don't change the original rows."
assert orph(orders, customers, "customer_id", "id") == [orders[2]], "orphans: order C points to customer 9, who doesn't exist."
