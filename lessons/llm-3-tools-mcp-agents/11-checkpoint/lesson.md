---
title: Checkpoint: write mcp.json from scratch
minutes: 30
xp: 60
hint: MCP_JSON starts with { "mcpServers": { "notes": { and ends with } } }. Only double quotes.
hint: Inside notes: "command": "npx", then "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/YOU/llm-notes"]
hint: Commas between items, never after the last one. The folder must start with /, not ~
hint: stdio servers are started by the client from command and args. A desktop app may not see your terminal's PATH.
---
# Checkpoint

⏱️ About 30 minutes

The Module 3 checkpoint, from your plan: *from a blank mcp.json, add a filesystem MCP server yourself, restrict it to one folder, and get the model to summarize a file in it.*

Do it **without scrolling back** to lesson 7. If you get stuck, that's the signal to reread it, then close it and try again.

## 🧩 How to answer

`MCP_JSON` is **text**: the JSON goes between the `"""` and the `"""`, exactly as it would look in the file. JSON rules (lesson 7):

- Only **double** quotes `"`.
- A comma between items, but **not** after the last one.
- Every `{` and `[` needs its closing `}` and `]`.

The other three are plain text answers, like `transport = "stdio"`.

### 👀 Worked example: a different server

This one is **not** the answer (other name, other folder), but it has the right shape:

```python
MCP_JSON = """
{
  "mcpServers": {
    "photos": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/anna/Pictures/holiday"]
    }
  }
}
"""
```

Read it from the outside in: the whole file → `mcpServers` (the list of servers) → one server named `photos` → how to start it. In `args`: `-y` (say yes to installing), then the package, then the **one** folder it may use.

Try first without looking. If you get stuck, change the name and folder in this example.

## Your quest

1. `MCP_JSON`: write the complete contents of an `mcp.json`, as raw JSON text inside the triple quotes, with **one** server named `"notes"` that:
   - starts the official filesystem server (`@modelcontextprotocol/server-filesystem`) with `npx` (a full path to `npx` is fine too),
   - answers npx's install question automatically,
   - may access exactly **one** folder, given as an absolute path, and not your whole home folder.
2. `transport`: `"stdio"` or `"http"`, which one does your server use?
3. `who_starts_it`: `"me"` (in a terminal, beforehand) or `"lmstudio"`?
4. `if_command_not_found`: on NixOS, LM Studio says `npx: command not found` although `npx` works in your terminal. What's the most likely fix, as a letter?
   - `"a"` reinstall LM Studio
   - `"b"` use the full path to `npx` in `"command"`
   - `"c"` switch to an HTTP server

## On your machine (the real checkpoint)

1. Make a folder, e.g. `~/llm-notes`, and put a text file in it.
2. In LM Studio open *Program → Install → Edit mcp.json* and paste your JSON, with that folder's real path.
3. Load a model with tool support, set a low temperature, and ask: *"Summarize the file in my notes folder."*
4. Watch the approval dialogs: which tools does it call, with which arguments? Then ask it to read `/etc/hostname`, and watch the server refuse.

## What's next

LLMs 4 is the Python and math gate to training: vectors and matrices, derivatives, probability, and a script that calls your LM Studio server.
