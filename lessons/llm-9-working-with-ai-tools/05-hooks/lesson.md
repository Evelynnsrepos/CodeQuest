---
title: Hooks: rules the model can't skip
xp: 55
---
# A guard that runs before every tool call

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

## 🎯 Your quest

1. `guard(event)`: `event` is the parsed JSON dict. Return `(exit_code, stderr)`. Block (2) if it's `Bash` and the command contains `rm -rf`, or if it's `Read` and `tool_input["file_path"]` ends with `.env`. Otherwise `(0, "")`.
2. `matcher_hits(matcher, tool_name)`: `"*"`, `""` → all. Only letters, digits, `_`, `-`, spaces, `,`, `|` → exact names separated by `|` or `,`. Anything else → `re.search(matcher, tool_name)`.

**Remember:** CLAUDE.md asks nicely; hooks enforce.

## Review

<details><summary>Order permission rules are checked in?</summary>deny, ask, allow.</details>
