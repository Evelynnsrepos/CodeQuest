---
title: n8n as an MCP server
xp: 30
---
# Let Claude or LM Studio call your workflows

⏱️ About 12 minutes · one function

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

## 🎯 Your quest

Write `mcp_entry(name, url, token)` that returns the dict above with `name` as the server name, `url` in place of `<MCP_URL>` and `token` in place of `<MCP_BEARER_TOKEN>`. Keep the text `${AUTH_TOKEN}` exactly as it is.

<details><summary>💡 Hint</summary>In a normal Python string, <code>"Authorization: Bearer ${AUTH_TOKEN}"</code> is just text. Don't make it an f-string, or Python will try to fill <code>{AUTH_TOKEN}</code> itself.</details>

**Remember:** Server Trigger = n8n offers tools; Client Tool = n8n uses tools. Always add auth.

## Review

<details><summary>Lesson 10: 50 items, 6 s each, 2 at once. Minutes?</summary>ceil(50 ÷ 2) = 25 rounds × 6 = 150 s ÷ 60 = 2.5 minutes.</details>
