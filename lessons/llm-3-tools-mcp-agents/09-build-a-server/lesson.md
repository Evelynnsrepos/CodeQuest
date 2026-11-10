---
title: Build a tiny MCP server
minutes: 50
xp: 45
hint: Start: if "id" not in message: return None. Then id = message["id"], method = message["method"], params = message.get("params", {})
hint: initialize: if method == "initialize": info = {"name": "codequest-notes", "version": "1.0"} and return ok(id, {"protocolVersion": params["protocolVersion"], "capabilities": {"tools": {}}, "serverInfo": info})
hint: tools/list: if method == "tools/list": return ok(id, {"tools": TOOLS})
hint: tools/call: name = params["name"]; unknown name → return ok(id, text_result("unknown tool " + name, True)); otherwise try the call and except Exception as e: return ok(id, text_result("error: " + repr(e), True))
hint: Last line: return fail(id, -32601, "Method not found")
---
# The server side

⏱️ About 50 minutes

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

## 🐍 Python you need

The helpers `ok`, `fail` and `text_result` are given. They build the response dictionaries, so you only decide **which** one to send.

| You write | Say it | What it does |
|---|---|---|
| `if "id" not in message:` | | no id → it's a notification |
| `message.get("params", {})` | | the params, or an empty dictionary if there are none |
| `if method == "initialize":` … `return …` | | one `if` per method. A `return` ends the function, so later `if`s aren't checked. |
| `IMPLEMENTATIONS[name]` | | the Python function for that tool |
| `params.get("arguments", {})` | | the tool's arguments, or none |
| `f(**args)` | "f with args unpacked" | `read_note(**{"name": "todo.md"})` is `read_note(name="todo.md")` |
| `except Exception as e:` | | catches **any** error from the tool, so the server never crashes |
| `repr(e)` | | the error as text, like `KeyError('nope.md')` |
| `text_result("...", True)` | | a result with `"isError": True` |

### 👀 Worked example: a tiny help desk

Same shape: no id → no answer; known requests → an answer; a job that may fail → caught; anything else → an error.

```python
def double(n):
    return n * 2

JOBS = {"double": double}

def desk(msg):
    if "id" not in msg:
        return None
    id = msg["id"]
    kind = msg["kind"]
    if kind == "hello":
        return {"id": id, "answer": "hi!"}
    if kind == "job":
        name = msg["job"]
        if name not in JOBS:
            return {"id": id, "answer": "unknown job " + name, "failed": True}
        try:
            return {"id": id, "answer": str(JOBS[name](msg["n"]))}
        except Exception as e:
            return {"id": id, "answer": "error: " + repr(e), "failed": True}
    return {"id": id, "error": "no such desk"}
```

- `{"kind": "hello"}` (no id) → `None`.
- `{"id": 1, "kind": "hello"}` → `{"id": 1, "answer": "hi!"}`.
- `{"id": 2, "kind": "job", "job": "double", "n": 4}` → answer `"8"`.
- `{"id": 3, "kind": "job", "job": "double", "n": None}` → `None * 2` fails, the `except` catches it → `"failed": True`.
- `{"id": 4, "kind": "coffee"}` → falls through to the last line → error.

## 🎯 Your quest

Write `handle(message)`. Replace `return None` with:

1. `if "id" not in message:`
2. `    return None`
3. `id = message["id"]`
4. `method = message["method"]`
5. `params = message.get("params", {})`
6. `if method == "initialize":`
7. `    info = {"name": "codequest-notes", "version": "1.0"}`
8. `    return ok(id, {"protocolVersion": params["protocolVersion"], "capabilities": {"tools": {}}, "serverInfo": info})`
9. `if method == "tools/list":`
10. `    return ok(id, {"tools": TOOLS})`
11. `if method == "tools/call":`
12. `    name = params["name"]`
13. `    if name not in IMPLEMENTATIONS:`
14. `        return ok(id, text_result("unknown tool " + name, True))`
15. `    try:`
16. `        text = str(IMPLEMENTATIONS[name](**params.get("arguments", {})))`
17. `        return ok(id, text_result(text))`
18. `    except Exception as e:`
19. `        return ok(id, text_result("error: " + repr(e), True))`
20. `return fail(id, -32601, "Method not found")`

Every response gets `"jsonrpc": "2.0"` and the request's `"id"` from the `ok` and `fail` helpers.

## Review

<details><summary>What is the "lethal trifecta"?</summary>Private data access + exposure to untrusted content + a way to send data out. Together, one prompt injection can leak data.</details>
<details><summary>How does a filesystem server stop "../" tricks?</summary>It resolves every path (normalize, follow symlinks) and refuses anything outside its allowed folders.</details>
