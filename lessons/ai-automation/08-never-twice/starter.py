def process_new(items, done, handle):
    # count = 0
    # for item_id, data in items:
    #     if item_id in done:
    #         continue
    #     handle(data)
    #     done.add(item_id)
    #     count = count + 1
    # return count
    for item_id, data in items:
        handle(data)
    return len(items)


done = {"mail-1"}
items = [("mail-1", "old news"), ("mail-2", "hello"), ("mail-3", "invoice")]
print(process_new(items, done, print), sorted(done))
