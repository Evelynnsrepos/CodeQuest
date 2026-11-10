---
title: LM Studio's mcp.json
minutes: 30
xp: 35
hint: stdio_server: entry = {"command": command, "args": args}, then if env is not None: entry["env"] = env, then return entry
hint: http_server: entry = {"url": url}, then if token is not None: entry["headers"] = {"Authorization": "Bearer " + token}, then return entry
hint: filesystem_config: server = stdio_server("npx", ["-y", "@modelcontextprotocol/server-filesystem", folder])
hint: Then: return {"mcpServers": {"filesystem": server}}
---
# The config file, line by line

⏱️ About 30 minutes

> **Warm-up:** LM Studio has to know which MCP servers exist and how to reach them. For a stdio server, what's the minimum it needs to know? For an HTTP server?

LM Studio (0.3.17 and later) reads its MCP servers from **`mcp.json`**, which you open from the *Program* tab in the right sidebar (*Install → Edit mcp.json*). On Linux the file lives at `~/.lmstudio/mcp.json`. It uses the same notation as Cursor and Claude Desktop, so examples from server READMEs mostly work unchanged:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/evilynn/notes"]
    },
    "my-api": {
      "url": "https://example.com/mcp",
      "headers": {"Authorization": "Bearer YOUR_TOKEN"}
    }
  }
}
```

Every line:

| Line | Meaning |
|---|---|
| `"mcpServers"` | the one top-level key; inside it, one entry per server |
| `"filesystem"` | a name you choose; shows up in LM Studio's UI and in tool names |
| `"command"` | **stdio**: the program LM Studio starts. `npx` downloads and runs a Node package. |
| `"args"` | its arguments, one string each. `-y` answers npx's install prompt; then the package; then, for the filesystem server, **the folders it may access**. Only those. |
| `"env"` | optional environment variables for the server, often API keys |
| `"url"` | **HTTP**: the server's endpoint, instead of `command` |
| `"headers"` | optional HTTP headers, usually authentication |

**NixOS notes.** `npx` comes with `nodejs` (`environment.systemPackages = [ pkgs.nodejs ];` or a home-manager equivalent). An app started from your launcher may not see your shell's PATH, so if a server fails with "command not found", use the full path, for example `"command": "/run/current-system/sw/bin/npx"` (find yours with `which npx`). Python servers are often started with `uvx` (from the `uv` package) instead of `npx`.

`npx -y` and `uvx` download the newest version of a package every time it isn't cached. That's convenient, and it's also why the next lesson is about security.

## 🐍 Python you need

The same pattern as LLMs 3 lesson 5: build a dictionary, add an optional key only when it was given.

| You write | Say it | What it does |
|---|---|---|
| `def f(command, args, env=None):` | | `env` is `None` unless the caller gives it |
| `{"command": command, "args": args}` | | keys in quotes, values from the boxes |
| `if env is not None:` | | only when it was given |
| `entry["env"] = env` | | add one more key |
| `"Bearer " + token` | | glues `Bearer ` (with a space) and the token |
| `["-y", "@modelcontextprotocol/server-filesystem", folder]` | | a list: two fixed texts and the folder from the box |
| `{"mcpServers": {"filesystem": server}}` | | a dictionary inside a dictionary |

### 👀 Worked example: a contact entry

```python
def contact(name, phone, email=None):
    entry = {"name": name, "phone": phone}
    if email is not None:
        entry["email"] = email
    return entry

def address_book(name):
    person = contact(name, "0123")
    return {"contacts": {"best friend": person}}

print(address_book("Ana"))
# {'contacts': {'best friend': {'name': 'Ana', 'phone': '0123'}}}
```

`address_book` calls `contact` and wraps the result, exactly like `filesystem_config` will call `stdio_server`.

## 🎯 Your quest

**Part 1:** `stdio_server(command, args, env=None)`. Replace `return {}` with:

1. `entry = {"command": command, "args": args}`
2. `if env is not None:`
3. `    entry["env"] = env`
4. `return entry`

**Part 2:** `http_server(url, token=None)`. Replace `return {}` with:

1. `entry = {"url": url}`
2. `if token is not None:`
3. `    entry["headers"] = {"Authorization": "Bearer " + token}`
4. `return entry`

**Part 3:** `filesystem_config(folder)`. Replace `return {}` with:

1. `server = stdio_server("npx", ["-y", "@modelcontextprotocol/server-filesystem", folder])`
2. `return {"mcpServers": {"filesystem": server}}`

The program prints the JSON you could paste into LM Studio.

## Review

<details><summary>Who starts a stdio MCP server?</summary>The client (LM Studio), using the command and args from its config.</details>
<details><summary>Why must a stdio server never print debug text to stdout?</summary>stdout carries the JSON-RPC messages, one per line. Extra text corrupts the stream; logs belong on stderr.</details>
