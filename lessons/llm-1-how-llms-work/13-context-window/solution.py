def total(msgs):
    return sum(count for role, count in msgs)


def rolling_window(messages, max_tokens):
    system, rest = messages[0], list(messages[1:])
    while rest and total([system] + rest) > max_tokens:
        rest.pop(0)
    return [system] + rest


chat = [("system", 300), ("user", 1200), ("assistant", 2500), ("user", 400),
        ("tool", 3000), ("assistant", 900), ("user", 200)]
print("total:", total(chat))
kept = rolling_window(chat, 8192)
print("kept:", kept)
print("dropped:", len(chat) - len(kept))
