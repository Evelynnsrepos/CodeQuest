def to_items(rows):
    return rows


def run_node(items, fn):
    return items


emails = to_items([{"subject": "Hi"}, {"subject": "Your order"}])
print(run_node(emails, lambda j: {"subject": j["subject"].upper()}))
