---
title: Running the tool calls
xp: 35
---
# From tool call to tool result

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

## Python you need

A dictionary can map names to functions: `TOOLS = {"add": add}` then `TOOLS["add"](2, 3)`. `**args` passes a dictionary as keyword arguments: `f(**{"a": 2, "b": 3})` is `f(a=2, b=3)`. `try:` / `except ValueError:` catches errors; `json.loads` raises a `ValueError` (a `JSONDecodeError`) on broken JSON.

## Your quest

Write `run_tool_calls(message, tools)`. For every entry in `message["tool_calls"]`, return a tool message `{"role": "tool", "tool_call_id": ..., "content": ...}` in the same order, where `content` is:

- `str(result)` of calling the function with the parsed arguments, or
- `"error: unknown tool NAME"` if the name isn't in `tools`, or
- `"error: invalid arguments"` if the arguments aren't valid JSON.

## Review

<details><summary>Does the model execute tools itself?</summary>No. It writes a structured request; the client runs the tool and sends the result back as a message.</details>
<details><summary>Why does the tool's description matter so much?</summary>It's the only information the model has about what the tool does and when to use it.</details>
