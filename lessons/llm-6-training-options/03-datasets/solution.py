import json


def alpaca_to_chat(record, system=None):
    messages = []
    if system is not None:
        messages.append({"role": "system", "content": system})
    user = record["instruction"]
    if record.get("input"):
        user += "\n\n" + record["input"]
    messages.append({"role": "user", "content": user})
    messages.append({"role": "assistant", "content": record["output"]})
    return {"messages": messages}


def to_jsonl(records):
    return "\n".join(json.dumps(r) for r in records)


def validate_line(line):
    try:
        data = json.loads(line)
    except ValueError:
        return "not valid JSON"
    messages = data.get("messages") if isinstance(data, dict) else None
    if not isinstance(messages, list) or len(messages) < 2:
        return "needs a messages list with at least 2 messages"
    for m in messages:
        if m.get("role") not in ("system", "user", "assistant"):
            return "unknown role"
        if not isinstance(m.get("content"), str) or not m["content"]:
            return "empty content"
    if messages[-1]["role"] != "assistant":
        return "last message must be from the assistant"
    return None


raw = [
    {"instruction": "Summarize the text.", "input": "LoRA freezes the base model and trains small matrices.", "output": "LoRA trains a few small add-on matrices."},
    {"instruction": "Say hi in German.", "input": "", "output": "Hallo!"},
]
lines = to_jsonl([alpaca_to_chat(r, "You are concise.") for r in raw])
print(lines)
for line in lines.splitlines() + ['{"messages": [{"role": "user", "content": "hi"}]}', "not json"]:
    print(validate_line(line))
