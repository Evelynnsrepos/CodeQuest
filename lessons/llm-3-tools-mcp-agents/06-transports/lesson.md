---
title: stdio vs HTTP transports
xp: 35
---
# How the messages travel

> **Warm-up:** the JSON-RPC messages from the last lesson have to get from LM Studio to the server and back somehow. What are two ways two programs can talk to each other?

MCP defines two standard **transports**:

**stdio** (local servers)
- The client **starts the server itself** as a child process, using the `command` and `args` from its config.
- Messages go over the server's **stdin** (client → server) and **stdout** (server → client), **one JSON message per line**.
- **stderr** is free for logs. A server that `print()`s debug text to stdout corrupts the stream, a classic bug.
- The server runs with *your* user's permissions on *your* machine, and stops when the client stops it.

**Streamable HTTP** (local or remote servers)
- The server is already running somewhere and has a URL such as `https://example.com/mcp`.
- The client sends each message as an HTTP **POST** to that one endpoint. The server answers with JSON, or with an SSE stream (LLMs 2, lesson 11) when it has several messages to send.
- Needs proper authentication (usually OAuth or an API key header), since anyone who can reach the URL can try to use it.
- (Older servers used a separate "HTTP+SSE" transport, which Streamable HTTP replaced in 2025. You may still meet it.)

| | stdio | Streamable HTTP |
|---|---|---|
| Who starts the server | the client | someone else, beforehand |
| Where it runs | your machine | anywhere |
| Config needs | `command`, `args`, `env` | `url`, maybe `headers` |
| Typical use | filesystem, git, local scripts | hosted services (GitHub, Notion, …) |

Because many messages travel over one channel, the client matches each response to its request by `id`. Messages without an `id` are notifications.

## Your quest

Write `read_stdio(raw)` for the text a stdio server wrote to its stdout. Go through the lines and return a tuple `(responses, notifications, bad_lines)`:

- `responses`: a dictionary from `id` to the message, for every message that has an `"id"`
- `notifications`: a list of the `"method"` of every message without an `"id"`
- `bad_lines`: how many non-empty lines weren't valid JSON (a buggy server printing to stdout)

Skip empty lines.

## Review

<details><summary>Name MCP's three roles.</summary>Host (the app), client (the connector inside it, one per server) and server (the separate program offering tools).</details>
<details><summary>What's the difference between a JSON-RPC request and a notification?</summary>A request has an id and expects a response; a notification has no id and gets none.</details>
<details><summary>Which method lists a server's tools, and which calls one?</summary>tools/list and tools/call.</details>
