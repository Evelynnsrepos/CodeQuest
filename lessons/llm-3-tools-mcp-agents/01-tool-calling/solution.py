import json

ROLL_DICE = {
    "type": "function",
    "function": {
        "name": "roll_dice",
        "description": "Roll dice and return the results.",
        "parameters": {
            "type": "object",
            "properties": {
                "sides": {"type": "integer", "description": "Number of sides on each die, e.g. 6 or 20"},
                "count": {"type": "integer", "description": "How many dice to roll (default 1)"},
            },
            "required": ["sides"],
        },
    },
}

print(json.dumps(ROLL_DICE, indent=2))
