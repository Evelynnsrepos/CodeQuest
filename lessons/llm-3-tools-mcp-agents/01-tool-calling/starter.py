import json

ROLL_DICE = {
    "type": "function",
    "function": {
        "name": "",
        "description": "",
        "parameters": {},  # replace {} with type, properties and required (see the quest)
    },
}

print(json.dumps(ROLL_DICE, indent=2))
