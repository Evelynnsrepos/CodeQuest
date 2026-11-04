def to_items(rows):
    return [{"json": row} for row in rows]


def run_node(items, fn):
    return [{"json": fn(item["json"])} for item in items]


emails = to_items([{"subject": "Hi"}, {"subject": "Your order"}])
print(run_node(emails, lambda j: {"subject": j["subject"].upper()}))
