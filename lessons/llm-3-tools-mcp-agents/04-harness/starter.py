def decide(tool_name, policy):
    return "allow"


def trim_history(messages, budget, tokens):
    return messages


def tokens(message):
    return len(message["content"]) // 4 + 1


policy = {"read_file": "allow", "write_file": "ask", "delete_everything": "deny"}
for name in ["read_file", "write_file", "delete_everything", "run_shell"]:
    print(name, "->", decide(name, policy))

history = [
    {"role": "system", "content": "You are a helpful assistant." * 2},
    {"role": "user", "content": "Read my notes." * 10},
    {"role": "assistant", "content": "calling read_file"},
    {"role": "tool", "content": "x" * 400},
    {"role": "user", "content": "Now summarize them."},
]
short = trim_history(history, 60, tokens)
print([m["role"] for m in short], sum(tokens(m) for m in short), "tokens")
