---
title: MCP, the plug standard for tools
minutes: 35
xp: 35
hint: request: message = {"jsonrpc": "2.0", "id": id, "method": method}, then if params is not None: message["params"] = params, then return message
hint: notification: return {"jsonrpc": "2.0", "method": method}
hint: tool_call_request: return request(id, "tools/call", {"name": name, "arguments": arguments})
hint: text_of: texts = [], for item in response["result"]["content"]: if item["type"] == "text": texts.append(item["text"]), then return "\n".join(texts)
---
# Model Context Protocol

⏱️ About 35 minutes

> **Warm-up:** in the last lessons, the tools were Python functions inside the same program. What if you want the *same* file-reading tool in LM Studio, in Claude and in your editor, without rewriting it three times?

That's what the **Model Context Protocol (MCP)** solves: a standard way for apps to discover and call tools that live in separate programs. Write a tool server once; every MCP-speaking app can use it.

Three roles:

| Role | What it is | Example |
|---|---|---|
| **Host** | The app you use, which holds the model and the chat | LM Studio, Claude Desktop, an editor |
| **Client** | The connector inside the host, one per server | LM Studio's MCP client |
| **Server** | A separate small program offering capabilities | the filesystem server, a GitHub server |

A server can offer **tools** (functions the model may call), **resources** (data the app can read, like files) and **prompts** (templates). Tools are by far the most used.

Under the hood, client and server exchange **JSON-RPC 2.0** messages. A **request** has an `id`, a `method` and `params`; the **response** carries the same `id` and either a `result` or an `error`. A **notification** has no `id` and gets no response.

```json
→ {"jsonrpc": "2.0", "id": 1, "method": "initialize",
   "params": {"protocolVersion": "2025-06-18", "capabilities": {},
              "clientInfo": {"name": "lmstudio", "version": "0.3"}}}
← {"jsonrpc": "2.0", "id": 1, "result": {"protocolVersion": "2025-06-18", "capabilities": {"tools": {}}, "serverInfo": {...}}}
→ {"jsonrpc": "2.0", "method": "notifications/initialized"}
→ {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}
← {"jsonrpc": "2.0", "id": 2, "result": {"tools": [{"name": "read_text_file", "description": "...", "inputSchema": {...}}]}}
→ {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "read_text_file", "arguments": {"path": "/home/evilynn/notes/todo.md"}}}
← {"jsonrpc": "2.0", "id": 3, "result": {"content": [{"type": "text", "text": "- learn MCP"}], "isError": false}}
```

The host turns the `tools/list` result into the `tools` array of the chat request (lesson 1), and each tool call from the model into a `tools/call`. The model never talks to the server; the host is always in the middle.

The protocol version string changes as the spec evolves; modelcontextprotocol.io lists the current one.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `def request(id, method, params=None):` | "params is None unless given" | an input with a **default**: `request(2, "tools/list")` works without params |
| `{"jsonrpc": "2.0", "id": id}` | | the key `"id"` (quotes) gets the value from the box `id` (no quotes) |
| `if params is not None:` | | only when params were given |
| `message["params"] = params` | | adds one more key |
| `request(id, "tools/call", {...})` | | your third function calls your first one |
| `response["result"]["content"]` | | a list of content items |
| `"\n".join(texts)` | "newline join" | glues the texts with a line break between them |

### 👀 Worked example: building a letter

```python
def letter(to, subject, ps=None):
    message = {"to": to, "subject": subject}
    if ps is not None:
        message["ps"] = ps
    return message

print(letter("Ana", "Hi"))                # {'to': 'Ana', 'subject': 'Hi'}
print(letter("Ana", "Hi", "see you"))     # {'to': 'Ana', 'subject': 'Hi', 'ps': 'see you'}
```

Without a `ps`, the dictionary simply has no `"ps"` key. That's exactly how JSON-RPC requests without `params` look.

And joining only some items:

```python
lines = []
for item in [{"kind": "word", "v": "Hi"}, {"kind": "pic", "v": "🐱"}, {"kind": "word", "v": "there"}]:
    if item["kind"] == "word":
        lines.append(item["v"])
print("\n".join(lines))   # Hi, then there on the next line
```

## 🎯 Your quest

**Part 1:** `request(id, method, params=None)`. Replace `return {}` with:

1. `message = {"jsonrpc": "2.0", "id": id, "method": method}`
2. `if params is not None:`
3. `    message["params"] = params`
4. `return message`

**Part 2:** `notification(method)`. Replace `return {}` with:

- `return {"jsonrpc": "2.0", "method": method}`

**Part 3:** `tool_call_request(id, name, arguments)`. Replace `return {}` with:

- `return request(id, "tools/call", {"name": name, "arguments": arguments})`

**Part 4:** `text_of(response)`. Replace `return ""` with:

1. `texts = []`
2. `for item in response["result"]["content"]:`
3. `    if item["type"] == "text":`
4. `        texts.append(item["text"])`
5. `return "\n".join(texts)`

## Review

<details><summary>Describe the agent loop in one sentence.</summary>Call the model; if it requests tools, run them, append the results and call it again; stop when it answers in text or after a step limit.</details>
<details><summary>Why does an agent need a step limit?</summary>A confused model can keep calling tools forever.</details>
