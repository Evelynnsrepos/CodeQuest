def total(msgs):
    count = 0
    for role, tokens in msgs:
        count = count + tokens
    return count


def rolling_window(messages, max_tokens):
    system = messages[0]
    rest = list(messages[1:])  # a copy of everything after the system prompt
    while len(rest) > 0 and total([system] + rest) > max_tokens:
        rest.pop(0)
    return [system] + rest


chat = [("system", 300), ("user", 1200), ("assistant", 2500), ("user", 400),
        ("tool", 3000), ("assistant", 900), ("user", 200)]
print("total:", total(chat))
kept = rolling_window(chat, 8192)
print("kept:", kept)
print("dropped:", len(chat) - len(kept))
