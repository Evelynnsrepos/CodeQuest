---
title: Checkpoint: write mcp.json from scratch
xp: 60
---
# Checkpoint

The Module 3 checkpoint, from your plan: *from a blank mcp.json, add a filesystem MCP server yourself, restrict it to one folder, and get the model to summarize a file in it.*

Do it **without scrolling back** to lesson 6. If you get stuck, that's the signal to reread it, then close it and try again.

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
