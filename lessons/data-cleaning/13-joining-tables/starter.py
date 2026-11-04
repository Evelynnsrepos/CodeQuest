def duplicate_keys(rows, key):
    return []


def left_join(left, right, left_key, right_key):
    return left


def orphans(left, right, left_key, right_key):
    return []


customers = [{"id": 1, "city": "Berlin"}, {"id": 2, "city": "Köln"}]
orders = [{"order": "A", "customer_id": "1"}, {"order": "B", "customer_id": " 2"}, {"order": "C", "customer_id": "9"}]
print(left_join(orders, customers, "customer_id", "id"))
print(orphans(orders, customers, "customer_id", "id"), duplicate_keys(customers + [{"id": "1"}], "id"))
