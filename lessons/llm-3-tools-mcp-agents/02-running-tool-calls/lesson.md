---
title: Running the tool calls
minutes: 45
xp: 35
hint: Inside the loop, first: name = call["function"]["name"]
hint: if name not in tools: content = "error: unknown tool " + name
hint: else: try: args = json.loads(call["function"]["arguments"]) except ValueError: args = None
hint: Still in the else: if args is None: content = "error: invalid arguments", else: content = str(tools[name](**args))
hint: Last line in the loop: results.append({"role": "tool", "tool_call_id": call["id"], "content": content})
---
# From tool call to tool result

⏱️ About 45 minutes

> **Warm-up:** the model's tool call arrives as text. What could go wrong if your program just trusts it?

When a model decides to use a tool, the reply has no normal text. Instead, the message carries `tool_calls`, and `finish_reason` is `"tool_calls"`:

```json
{"role": "assistant", "content": null,
 "tool_calls": [{"id": "call_1", "type": "function",
                 "function": {"name": "get_weather", "arguments": "{\"city\": \"Berlin\"}"}}]}
```

Watch out: `arguments` is a **string containing JSON**, not a dictionary. The model generated it token by token, so it can be broken JSON, name a tool that doesn't exist, or miss a required parameter. Your code is the one place where these mistakes get caught.

For each call you run the matching function and append one message per call:

```json
{"role": "tool", "tool_call_id": "call_1", "content": "12°C, light rain"}
```

The `tool_call_id` links the result to the call, which matters when a model makes several calls at once (**parallel tool calls**). Errors go back as tool results too: a message like `"error: unknown tool 'get_wether'"` lets the model correct itself on the next turn, instead of crashing your app.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `call["function"]["name"]` | | two lookups: the call's function part, then its name |
| `if name not in tools:` | | true when the dictionary has no such key |
| `TOOLS["add"]` | | the function stored under `"add"` |
| `TOOLS["add"](2, 3)` | | runs it: `5` |
| `f(**args)` | "f with args unpacked" | the two stars unpack a dictionary into named inputs: `add(**{"a": 2, "b": 3})` is `add(a=2, b=3)` |
| `json.loads(text)` | | turns JSON text into a dictionary. On broken JSON it raises a `ValueError`. |
| `try:` / `except ValueError:` | | if a line in `try` raises a `ValueError`, jump to `except` instead of crashing |
| `args = None` | | "no usable arguments" |
| `if args is None:` | | checks for that |
| `str(5)` | | the result as text, because a tool message's content is always text |

### 👀 Worked example: a vending machine

```python
import json

def cola(size):
    return "cola " + size

MACHINE = {"cola": cola}

def press(button, raw_options):
    if button not in MACHINE:
        return "error: no such button " + button
    try:
        options = json.loads(raw_options)
    except ValueError:
        options = None
    if options is None:
        return "error: bad options"
    return str(MACHINE[button](**options))

print(press("cola", '{"size": "large"}'))   # cola large
print(press("tea", '{}'))                   # error: no such button tea
print(press("cola", '{size: large'))        # error: bad options
```

1. Unknown button → an error **message**, not a crash.
2. `json.loads` fails on broken JSON → `except` sets `options = None` → another error message.
3. Otherwise `MACHINE["cola"](**{"size": "large"})` is `cola(size="large")`.

## 🎯 Your quest

Write `run_tool_calls(message, tools)`. Replace the `pass` line inside the loop with (8 spaces in front, more for the deeper lines):

1. `name = call["function"]["name"]`
2. `if name not in tools:`
3. `    content = "error: unknown tool " + name`
4. `else:`
5. `    try:`
6. `        args = json.loads(call["function"]["arguments"])`
7. `    except ValueError:`
8. `        args = None`
9. `    if args is None:`
10. `        content = "error: invalid arguments"`
11. `    else:`
12. `        content = str(tools[name](**args))`
13. `results.append({"role": "tool", "tool_call_id": call["id"], "content": content})`

Line 13 is back at 8 spaces: it runs for every call, whatever happened above.

## Review

<details><summary>Does the model execute tools itself?</summary>No. It writes a structured request; the client runs the tool and sends the result back as a message.</details>
<details><summary>Why does the tool's description matter so much?</summary>It's the only information the model has about what the tool does and when to use it.</details>
