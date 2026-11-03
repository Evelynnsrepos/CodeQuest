---
title: LM Studio's mcp.json
xp: 35
---
# The config file, line by line

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

## Your quest

1. `stdio_server(command, args, env=None)`: return the entry dictionary, with `"env"` only if `env` is given.
2. `http_server(url, token=None)`: return `{"url": url}`, plus `"headers": {"Authorization": "Bearer " + token}` if a token is given.
3. `filesystem_config(folder)`: return a whole config with one server named `"filesystem"`, started with `npx`, limited to `folder`.

The program prints the JSON you could paste into LM Studio.

## Review

<details><summary>Who starts a stdio MCP server?</summary>The client (LM Studio), using the command and args from its config.</details>
<details><summary>Why must a stdio server never print debug text to stdout?</summary>stdout carries the JSON-RPC messages, one per line. Extra text corrupts the stream; logs belong on stderr.</details>
