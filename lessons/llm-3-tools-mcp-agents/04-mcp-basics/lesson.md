---
title: MCP, the plug standard for tools
xp: 35
---
# Model Context Protocol

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

## Your quest

1. `request(id, method, params)`: return a JSON-RPC request dictionary with `"jsonrpc": "2.0"`, `"id"`, `"method"` and, only if `params` isn't `None`, `"params"`.
2. `notification(method)`: a dictionary with `"jsonrpc"` and `"method"` only.
3. `tool_call_request(id, name, arguments)`: a `tools/call` request built with `request`.
4. `text_of(response)`: join the `"text"` of every content item of type `"text"` in a `tools/call` response, separated by newlines.

## Review

<details><summary>Describe the agent loop in one sentence.</summary>Call the model; if it requests tools, run them, append the results and call it again; stop when it answers in text or after a step limit.</details>
<details><summary>Why does an agent need a step limit?</summary>A confused model can keep calling tools forever.</details>
