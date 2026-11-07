import json


def extract_json(reply):
    fence = "`" * 3
    first = reply.find(fence)
    if first != -1:
        second = reply.find(fence, first + 3)
        text = reply[first + 3:second]
        if text.startswith("json"):
            text = text[4:]
    else:
        start = reply.find("{")
        end = reply.rfind("}")
        if start == -1 or end < start:
            return None
        text = reply[start:end + 1]
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


print(extract_json('Sure! Here is the JSON:\n```json\n{"label": "work", "urgent": true}\n```\nHope that helps!'))
