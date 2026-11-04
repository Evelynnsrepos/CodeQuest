def code_node(items):
    return [{"json": {**i["json"], "big": True}} for i in items if i["json"]["amount"] > 100]


orders = [{"json": {"id": 1, "amount": 40}}, {"json": {"id": 2, "amount": 250}}, {"json": {"id": 3, "amount": 120}}]
print(code_node(orders))
