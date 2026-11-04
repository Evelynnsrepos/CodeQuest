import json


def collect_stream(raw):
    text = ""
    for line in raw.splitlines():
        pass
    return text


raw = """data: {"choices": [{"index": 0, "delta": {"role": "assistant", "content": ""}}]}

data: {"choices": [{"index": 0, "delta": {"content": "Hal"}}]}

data: {"choices": [{"index": 0, "delta": {"content": "lo, "}}]}

data: {"choices": [{"index": 0, "delta": {"content": "Evelynn!"}, "finish_reason": "stop"}]}

data: [DONE]
"""
print(collect_stream(raw))
