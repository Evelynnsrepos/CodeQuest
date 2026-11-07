---
title: stdio vs HTTP transports
minutes: 35
xp: 35
hint: Loop: for line in raw.splitlines(): and first skip empty ones: if line.strip() == "": continue
hint: try: message = json.loads(line) except ValueError: bad_lines = bad_lines + 1 and continue
hint: if "id" in message: responses[message["id"]] = message, else: notifications.append(message["method"])
---
# How the messages travel

⏱️ About 35 minutes

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

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `raw.splitlines()` | | a list with one text per line |
| `line.strip() == ""` | | the line is empty (or only spaces) |
| `continue` | | skip to the next line |
| `try:` / `except ValueError:` | | `json.loads` raises a `ValueError` for text that isn't JSON |
| `bad_lines = bad_lines + 1` | | count one more bad line |
| `"id" in message` | | does the message have an `"id"` key? |
| `responses[message["id"]] = message` | | store the message under its id |
| `notifications.append(message["method"])` | | collect the method name |

### 👀 Worked example: sorting the post

```python
import json

post = '{"to": "Ana"}\nhello?\n\n{"note": "flyer"}'
letters = {}
flyers = []
junk = 0
for line in post.splitlines():
    if line.strip() == "":
        continue
    try:
        item = json.loads(line)
    except ValueError:
        junk = junk + 1
        continue
    if "to" in item:
        letters[item["to"]] = item
    else:
        flyers.append(item["note"])
print(letters, flyers, junk)   # {'to': ...} ['flyer'] 1
```

| line | what happens |
|---|---|
| `{"to": "Ana"}` | valid JSON with `"to"` → a letter for Ana |
| `hello?` | not JSON → junk = 1 |
| (empty) | skipped |
| `{"note": "flyer"}` | no `"to"` → a flyer |

## 🎯 Your quest

Write `read_stdio(raw)`. Between the first line and `return`, add:

1. `for line in raw.splitlines():`
2. `    if line.strip() == "":`
3. `        continue`
4. `    try:`
5. `        message = json.loads(line)`
6. `    except ValueError:`
7. `        bad_lines = bad_lines + 1`
8. `        continue`
9. `    if "id" in message:`
10. `        responses[message["id"]] = message`
11. `    else:`
12. `        notifications.append(message["method"])`

## Review

<details><summary>Name MCP's three roles.</summary>Host (the app), client (the connector inside it, one per server) and server (the separate program offering tools).</details>
<details><summary>What's the difference between a JSON-RPC request and a notification?</summary>A request has an id and expects a response; a notification has no id and gets none.</details>
<details><summary>Which method lists a server's tools, and which calls one?</summary>tools/list and tools/call.</details>
