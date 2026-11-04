import json


def alpaca_to_chat(record, system=None):
    messages = []
    return {"messages": messages}


def to_jsonl(records):
    return ""


def validate_line(line):
    return None


raw = [
    {"instruction": "Summarize the text.", "input": "LoRA freezes the base model and trains small matrices.", "output": "LoRA trains a few small add-on matrices."},
    {"instruction": "Say hi in German.", "input": "", "output": "Hallo!"},
]
lines = to_jsonl([alpaca_to_chat(r, "You are concise.") for r in raw])
print(lines)
for line in lines.splitlines() + ['{"messages": [{"role": "user", "content": "hi"}]}', "not json"]:
    print(validate_line(line))
