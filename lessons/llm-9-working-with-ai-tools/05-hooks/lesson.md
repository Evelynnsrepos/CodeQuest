---
title: Hooks: rules the model can't skip
minutes: 40
xp: 55
hint: guard: tool = event.get("tool_name") and inp = event.get("tool_input", {})
hint: guard: if tool == "Bash" and "rm -rf" in inp.get("command", ""): return (2, "Blocked: rm -rf is not allowed")
hint: matcher_hits: simple = True, then for ch in matcher: if not (ch.isalnum() or ch in "_- ,|"): simple = False
hint: matcher_hits: if simple: names = matcher.replace(",", "|").split("|"), then loop and compare n.strip() == tool_name
hint: Last line: return re.search(matcher, tool_name) is not None
---
# A guard that runs before every tool call

⏱️ About 40 minutes

> **Warm-up:** you told the agent "never touch `.env`". It's convinced it needs to read `.env` to fix a bug. What stops it?

**In one sentence:** a hook is a command the harness runs automatically on an event (like "before a tool runs"), and a `PreToolUse` hook can block the call no matter what the model wants.

## 🪜 Plain words

Hooks live in settings (`"hooks": {...}`). The most useful events:

| Event | When | Typical use |
|---|---|---|
| `PreToolUse` | before a tool runs | block dangerous commands |
| `PostToolUse` | after a tool succeeds | format/lint after every edit |
| `SessionStart` | session begins | load extra context |
| `UserPromptSubmit` | you hit enter | add info to your prompt |
| `Stop` | Claude finishes a reply | run tests, notify you |

A **command hook** gets the event as **JSON on stdin**, with fields like `tool_name` and `tool_input` (for Bash: `tool_input.command`). It answers with its **exit code**:

- **0**: fine, carry on (normal permission rules still apply)
- **2**: **block**. What you print to **stderr** is shown to Claude as the reason, so it can try something else.

The **matcher** picks which tools trigger it: `"Bash"` = exactly Bash, `"Edit|Write"` = either, `"*"` or empty = all. Anything with other characters (like `mcp__.*`) is treated as a regular expression.

## 🪜 With numbers

Settings:

```json
{"hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [{"type": "command", "command": "python3 guard.py"}]}]}}
```

Claude wants to run `rm -rf build`. The harness sends `{"tool_name": "Bash", "tool_input": {"command": "rm -rf build"}, ...}` to `guard.py`. It prints `Blocked: rm -rf is not allowed` to stderr and exits **2**. The command never runs; Claude reads the reason.

## 🔀 What if it were different?

<div class="wrong"><b>Exit 1 instead of 2</b>: that's a non-blocking error; the tool call still runs.</div>
<div class="wrong"><b>Print the reason to stdout</b>: with exit 2, Claude Code shows stderr. Your explanation gets lost.</div>
<div class="wrong"><b>Matcher "Bash|Edit"</b> when you meant only Bash: edits trigger your guard too (harmless here, but slower and confusing).</div>
<div class="right">matcher "Bash", read stdin JSON, stderr + exit 2 to block, exit 0 otherwise ✓</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `event.get("tool_name")` | "event get tool name" | the value under that key, or `None` if it's missing (no crash) |
| `inp.get("command", "")` | | the command, or empty text if there is none |
| `"rm -rf" in text` | "rm -rf is in text" | true when that piece appears anywhere in the text |
| `return (2, "Blocked: ...")` | | gives back a pair: the exit code and the reason |
| `ch.isalnum()` | "ch is alphanumeric" | true for a letter or a digit |
| `ch in "_- ,\|"` | "ch is one of these" | `in` on a text checks single characters too: true for `_`, `-`, space, `,` or `\|` |
| `not (...)` | "not" | flips true and false |
| `s.replace(",", "\|")` | "replace comma with bar" | `"Edit,Write"` → `"Edit\|Write"`, so you only have to split at one character |
| `n.strip()` | "n strip" | removes spaces at both ends: `" Write"` → `"Write"` |
| `re.search(p, s) is not None` | | `re` is Python's search-pattern toolbox. `re.search` gives `None` when the pattern isn't found, so this is true when it **is** found. |

### 👀 Worked example: is this matcher a plain list?

```python
matcher = "Edit, Write"
simple = True
for ch in matcher:
    if not (ch.isalnum() or ch in "_- ,|"):
        simple = False
print(simple)
```

1. `simple` starts `True`: innocent until proven guilty.
2. `E`, `d`, `i`, `t` are letters. `,` and space are in the allowed list. `W`, `r`, `i`, `t`, `e` are letters. Nothing sets `simple` to `False`.
3. Prints `True`. Then `"Edit, Write".replace(",", "|")` is `"Edit| Write"`, `.split("|")` is `["Edit", " Write"]`, and `.strip()` turns `" Write"` into `"Write"`.

For `matcher = "mcp__memory__.*"`, the `.` and `*` are not allowed characters, so `simple` becomes `False` and the matcher is used as a search pattern.

## 🎯 Your quest

1. `guard(event)`: `event` is the parsed JSON dict. Return `(exit_code, stderr)`. Block (2) if it's `Bash` and the command contains `rm -rf`, or if it's `Read` and `tool_input["file_path"]` ends with `.env`. Otherwise `(0, "")`.
2. `matcher_hits(matcher, tool_name)`: `"*"`, `""` → all. Only letters, digits, `_`, `-`, spaces, `,`, `|` → exact names separated by `|` or `,`. Anything else → `re.search(matcher, tool_name)`.

**Part 1:** `guard`. Replace `return (0, "")` with:

1. `tool = event.get("tool_name")`
2. `inp = event.get("tool_input", {})`
3. `if tool == "Bash" and "rm -rf" in inp.get("command", ""):`
4. `    return (2, "Blocked: rm -rf is not allowed")`
5. `if tool == "Read" and inp.get("file_path", "").endswith(".env"):`
6. `    return (2, "Blocked: .env files hold secrets")`
7. `return (0, "")`

**Part 2:** `matcher_hits`. Replace `return True` with:

1. `if matcher == "*" or matcher == "":`
2. `    return True`
3. `simple = True`
4. `for ch in matcher:`
5. `    if not (ch.isalnum() or ch in "_- ,|"):`
6. `        simple = False`
7. `if simple:`
8. `    names = matcher.replace(",", "|").split("|")`
9. `    for n in names:`
10. `        if n.strip() == tool_name:`
11. `            return True`
12. `    return False`
13. `return re.search(matcher, tool_name) is not None`

**Remember:** CLAUDE.md asks nicely; hooks enforce.

## Review

<details><summary>Order permission rules are checked in?</summary>deny, ask, allow.</details>
