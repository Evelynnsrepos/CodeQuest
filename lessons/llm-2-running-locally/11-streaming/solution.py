import json


def collect_stream(raw):
    text = ""
    for line in raw.splitlines():
        if not line.startswith("data: "):
            continue
        payload = line[len("data: "):]
        if payload == "[DONE]":
            break
        delta = json.loads(payload)["choices"][0]["delta"]
        text += delta.get("content", "")
    return text


raw = """data: {"choices": [{"index": 0, "delta": {"role": "assistant", "content": ""}}]}

data: {"choices": [{"index": 0, "delta": {"content": "Hal"}}]}

data: {"choices": [{"index": 0, "delta": {"content": "lo, "}}]}

data: {"choices": [{"index": 0, "delta": {"content": "Evelynn!"}, "finish_reason": "stop"}]}

data: [DONE]
"""
print(collect_stream(raw))
