def total_tokens(msgs, tokens):
    """Given: the size of all messages together."""
    count = 0
    for m in msgs:
        count = count + tokens(m)
    return count


def decide(tool_name, policy):
    # return policy.get(tool_name, "ask")
    return "allow"


def trim_history(messages, budget, tokens):
    # system = messages[0]
    # rest = list(messages[1:])
    # while total_tokens([system] + rest, tokens) > budget and len(rest) > 1:
    #     rest.pop(0)
    #     while len(rest) > 1 and rest[0]["role"] == "tool":
    #         rest.pop(0)
    # return [system] + rest
    return messages


def tokens(message):
    return len(message["content"]) // 4 + 1


policy = {"read_file": "allow", "write_file": "ask", "delete_everything": "deny"}
for name in ["read_file", "write_file", "delete_everything", "run_shell"]:
    print(name, decide(name, policy))

history = [
    {"role": "system", "content": "You are a helpful assistant." * 2},
    {"role": "user", "content": "Read my notes." * 10},
    {"role": "assistant", "content": "calling read_file"},
    {"role": "tool", "content": "x" * 400},
    {"role": "user", "content": "Now summarize them."},
]
short = trim_history(history, 60, tokens)
for m in short:
    print(m["role"])
print(total_tokens(short, tokens), "tokens")
