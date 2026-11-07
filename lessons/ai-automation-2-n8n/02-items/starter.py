def to_items(rows):
    # items = []
    # for row in rows:
    #     items.append({"json": row})
    # return items
    return rows


def run_node(items, fn):
    # new_items = []
    # for item in items:
    #     result = fn(item["json"])
    #     new_items.append({"json": result})
    # return new_items
    return items


def shout_subject(j):
    return {"subject": j["subject"].upper()}


emails = to_items([{"subject": "Hi"}, {"subject": "Your order"}])
print(run_node(emails, shout_subject))
