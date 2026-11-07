---
title: n8n as an MCP server
minutes: 25
xp: 30
hint: Build the inner dictionary first: entry = {} and then entry["command"] = "npx"
hint: entry["args"] = ["mcp-remote", url, "--header", "Authorization: Bearer ${AUTH_TOKEN}"] (url without quotes: it's the box)
hint: entry["env"] = {"AUTH_TOKEN": token}, then return {"mcpServers": {name: entry}}
---
# Let Claude or LM Studio call your workflows

⏱️ About 25 minutes · one function, five lines

> **Warm-up:** you built a workflow "add to shopping list". Could you ask an AI chat app to run it for you?

**In one sentence:** the **MCP Server Trigger** node turns a workflow into an MCP server whose tools any MCP client can call, and the **MCP Client Tool** node does the opposite: it lets an n8n AI Agent use other MCP servers.

## 🪜 MCP Server Trigger

- Plug tool nodes into it (for your own workflows: **Call n8n Workflow Tool**). It doesn't pass items on like other triggers; it only offers tools.
- Transports: **SSE** and **streamable HTTP**. Not stdio (that's why desktop apps need a small bridge, below).
- It has a **Test URL** (works while you're listening in the editor) and a **Production URL** (works once the workflow is published/active).
- Authentication: **Bearer** or **Header** auth (or n8n user OAuth). Always turn one on: without it, anyone who can reach the URL can run your tools. LLMs 3, lesson 08, covers MCP security.

## 🪜 Connecting a desktop app

Apps that only start stdio servers (like Claude Desktop) use the `mcp-remote` bridge through `npx`. n8n's docs give this shape:

```json
{"mcpServers": {"n8n": {
  "command": "npx",
  "args": ["mcp-remote", "<MCP_URL>", "--header", "Authorization: Bearer ${AUTH_TOKEN}"],
  "env": {"AUTH_TOKEN": "<MCP_BEARER_TOKEN>"}
}}}
```

The token goes in `env`, and `${AUTH_TOKEN}` in the args is filled from it, so the token appears only in one place. LM Studio's `mcp.json` (LLMs 3, lesson 07) uses the same `mcpServers` format.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `entry = {}` | | a new, empty dictionary |
| `entry["command"] = "npx"` | "entry at command becomes npx" | adds the key `command` with the text `"npx"` |
| `["mcp-remote", url]` | | a list. `"mcp-remote"` (in quotes) is fixed text; `url` (no quotes) is **whatever is in the box** `url` |
| `{"AUTH_TOKEN": token}` | | a dictionary whose value comes from the box `token` |
| `{name: entry}` | | a dictionary whose **key** comes from the box `name` |
| `"Bearer ${AUTH_TOKEN}"` | | just text. Python doesn't touch `${...}` in a normal string. Later, `mcp-remote` swaps it for the real token from `env`. |

The big difference to see: quotes or no quotes. `"url"` is the three letters u, r, l. `url` is the value inside the box called url.

### 👀 Worked example: a contact card

```python
def card(name, phone):
    info = {}
    info["type"] = "friend"
    info["numbers"] = ["home", phone]
    info["extra"] = {"PHONE": phone}
    return {"contacts": {name: info}}

print(card("Ana", "0123"))
```

1. `info` starts empty.
2. `"type"` gets the fixed text `"friend"`.
3. `"numbers"` gets a list: the fixed text `"home"`, then **what's in** `phone`: `"0123"`.
4. `"extra"` gets a small dictionary with the phone in it.
5. Returns `{"contacts": {"Ana": {"type": "friend", "numbers": ["home", "0123"], "extra": {"PHONE": "0123"}}}}`. The key `"Ana"` came from the box `name`.

## 🎯 Your quest

Write `mcp_entry(name, url, token)` that builds the dictionary above with your values. Replace `return {}` with:

1. `entry = {}`
2. `entry["command"] = "npx"`
3. `entry["args"] = ["mcp-remote", url, "--header", "Authorization: Bearer ${AUTH_TOKEN}"]`
4. `entry["env"] = {"AUTH_TOKEN": token}`
5. `return {"mcpServers": {name: entry}}`

The real token appears only in `env`, never in `args`.

**Remember:** Server Trigger = n8n offers tools; Client Tool = n8n uses tools. Always add auth.

## Review

<details><summary>Lesson 10: 50 items, 6 s each, 2 at once. Minutes?</summary>ceil(50 ÷ 2) = 25 rounds × 6 = 150 s ÷ 60 = 2.5 minutes.</details>
