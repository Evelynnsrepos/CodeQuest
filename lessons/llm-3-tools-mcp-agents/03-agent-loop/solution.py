import json

NOTES = {"2026-10-30.md": "Bought milk.", "2026-11-02.md": "Learned what a KV cache is. It grows with every token."}


def list_files():
    return ", ".join(sorted(NOTES))


def read_file(name):
    return NOTES.get(name, "error: no such file")


TOOLS = {"list_files": list_files, "read_file": read_file}


def run_tool_calls(message, tools):
    results = []
    for call in message["tool_calls"]:
        name = call["function"]["name"]
        if name not in tools:
            content = "error: unknown tool " + name
        else:
            try:
                args = json.loads(call["function"]["arguments"])
            except ValueError:
                content = "error: invalid arguments"
            else:
                content = str(tools[name](**args))
        results.append({"role": "tool", "tool_call_id": call["id"], "content": content})
    return results


def scripted_model(script):
    """Stands in for LM Studio: returns the next recorded reply each time it's called."""
    replies = iter(script)
    def model(messages):
        print("  model sees", len(messages), "messages")
        return next(replies)
    return model


def tool_call(i, name, args):
    return {"role": "assistant", "content": None,
            "tool_calls": [{"id": i, "type": "function", "function": {"name": name, "arguments": json.dumps(args)}}]}


def run_agent(messages, model, tools, max_steps):
    for _ in range(max_steps):
        reply = model(messages)
        messages.append(reply)
        if reply.get("tool_calls"):
            messages.extend(run_tool_calls(reply, tools))
        else:
            return reply["content"]
    return "stopped: too many steps"


script = [
    tool_call("c1", "list_files", {}),
    tool_call("c2", "read_file", {"name": "2026-11-02.md"}),
    {"role": "assistant", "content": "Your newest note says you learned that the KV cache grows with every token."},
]
messages = [{"role": "system", "content": "You can read the user's notes."},
            {"role": "user", "content": "Summarize my newest note."}]
print(run_agent(messages, scripted_model(script), TOOLS, 5))
print(len(messages), "messages at the end")
