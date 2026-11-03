---
title: Build a tiny MCP server
xp: 45
---
# The server side

> **Warm-up:** you've written the client side of the conversation. What does a server have to do when a `tools/call` request arrives?

A server is a loop: read a message, handle it, write the response. For the methods you know:

| Method | Server answers with |
|---|---|
| `initialize` | `{"protocolVersion": ..., "capabilities": {"tools": {}}, "serverInfo": {"name": ..., "version": ...}}` |
| `tools/list` | `{"tools": [{"name", "description", "inputSchema"}, ...]}` |
| `tools/call` | `{"content": [{"type": "text", "text": ...}], "isError": false}` |
| anything else | a JSON-RPC **error**: `{"code": -32601, "message": "Method not found"}` |

Notifications (no `id`) get no answer at all. Two kinds of failure are kept apart: a **protocol error** (unknown method, malformed request) is a JSON-RPC `error`; a **tool failure** (file not found, bad input) is a normal `result` with `"isError": true`, so the *model* can read the message and react.

In practice you don't write this by hand. The official Python SDK does the protocol work, and a whole server is a few lines (the API may have changed since this was written; check the `mcp` package docs):

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("notes")

@mcp.tool()
def count_words(text: str) -> int:
    """Count the words in a text."""
    return len(text.split())

if __name__ == "__main__":
    mcp.run()   # stdio by default
```

The SDK reads the function's name, docstring and type hints to build the `tools/list` entry. Knowing what it does underneath is what lets you debug it when LM Studio says "server failed to start".

## Your quest

Write `handle(message)`. It returns the response dictionary, or `None` for notifications.

- `initialize` → result as in the table, with `"protocolVersion"` echoed from the request's params, and `serverInfo` `{"name": "codequest-notes", "version": "1.0"}`
- `tools/list` → the `TOOLS` list
- `tools/call` → look up the tool in `IMPLEMENTATIONS`, call it with the arguments, and return its text. If the name is unknown, or the function raises any error, return a result with `"isError": True` and the error text.
- anything else with an `id` → error `-32601`

Every response has `"jsonrpc": "2.0"` and the request's `"id"`. The helpers `ok` and `fail` build them.

## Review

<details><summary>What is the "lethal trifecta"?</summary>Private data access + exposure to untrusted content + a way to send data out. Together, one prompt injection can leak data.</details>
<details><summary>How does a filesystem server stop "../" tricks?</summary>It resolves every path (normalize, follow symlinks) and refuses anything outside its allowed folders.</details>
