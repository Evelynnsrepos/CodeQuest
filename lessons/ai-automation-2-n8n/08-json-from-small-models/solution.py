import json
import re


def extract_json(reply):
    m = re.search(r"```(?:json)?\s*(.*?)```", reply, re.S)
    if m:
        text = m.group(1)
    else:
        start, end = reply.find("{"), reply.rfind("}")
        if start == -1 or end < start:
            return None
        text = reply[start:end + 1]
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


print(extract_json('Sure! Here is the JSON:\n```json\n{"label": "work", "urgent": true}\n```\nHope that helps!'))
