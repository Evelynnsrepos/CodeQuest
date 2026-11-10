def code_node(items):
    new_items = []
    for item in items:
        if item["json"]["amount"] > 100:
            fields = dict(item["json"])
            fields["big"] = True
            new_items.append({"json": fields})
    return new_items


orders = [{"json": {"id": 1, "amount": 40}}, {"json": {"id": 2, "amount": 250}}, {"json": {"id": 3, "amount": 120}}]
print(code_node(orders))
