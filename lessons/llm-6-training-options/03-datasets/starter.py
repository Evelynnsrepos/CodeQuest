import json


def alpaca_to_chat(record, system=None):
    messages = []
    # if system is not None:
    #     messages.append({"role": "system", "content": system})
    # user = record["instruction"]
    # if record.get("input", "") != "":
    #     user = user + "\n\n" + record["input"]
    # messages.append({"role": "user", "content": user})
    # messages.append({"role": "assistant", "content": record["output"]})
    # return {"messages": messages}


def to_jsonl(records):
    # lines = []
    # for r in records:
    #     lines.append(json.dumps(r))
    # return "\n".join(lines)
    return ""


def validate_line(line):
    # try:
    #     data = json.loads(line)
    # except ValueError:
    #     return "not valid JSON"
    # if not isinstance(data, dict):
    #     return "needs a messages list with at least 2 messages"
    # messages = data.get("messages")
    # if not isinstance(messages, list) or len(messages) < 2:
    #     return "needs a messages list with at least 2 messages"
    # for m in messages:
    #     if m.get("role") not in ["system", "user", "assistant"]:
    #         return "unknown role"
    #     content = m.get("content")
    #     if not isinstance(content, str) or content == "":
    #         return "empty content"
    # if messages[-1]["role"] != "assistant":
    #     return "last message must be from the assistant"
    return None


raw = [
    {"instruction": "Summarize the text.", "input": "LoRA freezes the base model and trains small matrices.", "output": "LoRA trains a few small add-on matrices."},
    {"instruction": "Say hi in German.", "input": "", "output": "Hallo!"},
]
chats = []
for r in raw:
    chats.append(alpaca_to_chat(r, "You are concise."))
lines = to_jsonl(chats)
print(lines)
for line in lines.splitlines() + ['{"messages": [{"role": "user", "content": "hi"}]}', "not json"]:
    print(validate_line(line))
