def process_new(items, done, handle):
    for item_id, data in items:
        handle(data)
    return len(items)


done = {"mail-1"}
items = [("mail-1", "old news"), ("mail-2", "hello"), ("mail-3", "invoice")]
print(process_new(items, done, print), sorted(done))
