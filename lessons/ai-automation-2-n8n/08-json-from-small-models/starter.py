import json
import re


def extract_json(reply):
    return json.loads(reply)


print(extract_json('Sure! Here is the JSON:\n```json\n{"label": "work", "urgent": true}\n```\nHope that helps!'))
