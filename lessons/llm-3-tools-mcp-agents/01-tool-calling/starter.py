import json

ROLL_DICE = {
    "type": "function",
    "function": {
        "name": "",
        "description": "",
        "parameters": {},
    },
}

print(json.dumps(ROLL_DICE, indent=2))
