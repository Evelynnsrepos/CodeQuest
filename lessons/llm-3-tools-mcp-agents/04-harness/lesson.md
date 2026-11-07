---
title: The harness around the model
minutes: 40
xp: 40
hint: decide has one line: return policy.get(tool_name, "ask")
hint: trim_history: system = messages[0] and rest = list(messages[1:])
hint: while total_tokens([system] + rest, tokens) > budget and len(rest) > 1: and inside it rest.pop(0)
hint: Still inside that while, a second while: while len(rest) > 1 and rest[0]["role"] == "tool": rest.pop(0)
hint: At the end: return [system] + rest
---
# What an AI harness is

⏱️ About 40 minutes

> **Warm-up:** the model only ever outputs text. So who actually reads your files, runs the commands, and decides when the job is finished?

The **harness**. A model on its own is a function: messages in, next tokens out. A **harness** is the program around it that turns that function into an assistant or agent. The agent loop from the last lesson is the core of a harness. A real one also handles:

| Part | Job |
|---|---|
| **Prompt assembly** | builds the system prompt, applies the chat template, adds the tool definitions and project instructions |
| **Tool runtime** | actually runs the tool calls (files, shell, browser, MCP servers) and returns results |
| **The loop** | call, act, observe, repeat, with a step limit |
| **Permissions** | decides which calls run automatically, which need your OK, and which are never allowed |
| **Context management** | keeps the conversation inside the context window: trims or summarizes old turns, shortens big tool outputs |
| **Memory and state** | saves notes, files or summaries between sessions |
| **Sandboxing** | runs commands in a container or a restricted folder so mistakes can't hurt your system |

Examples: **Claude Code**, Codex CLI and Cursor's agent are coding harnesses; **LM Studio's chat with MCP** is a simple harness; the `run_agent` you wrote is a tiny one. The same model can be great in one harness and weak in another, because the harness decides what the model sees and what it's allowed to do. That's why benchmark results for agents always name the harness ("model X in harness Y").

The word also has an older meaning in machine learning: an **evaluation harness** (like EleutherAI's `lm-evaluation-harness`) is a program that feeds a model benchmark questions and scores the answers. Same idea: code around the model that drives it.

## 🐍 Python you need

`total_tokens(msgs, tokens)` is given: it adds up `tokens(m)` for every message in the list.

| You write | Say it | What it does |
|---|---|---|
| `policy.get(name, "ask")` | "policy get name, else ask" | the entry for that tool, or `"ask"` if the tool isn't in the policy |
| `list(messages[1:])` | | a **copy** of everything after the first message, so the input isn't changed |
| `[system] + rest` | | the system prompt back in front |
| `while a and b:` | | repeats while **both** are true |
| `len(rest) > 1` | | more than one message left: the newest must always stay |
| `rest.pop(0)` | | removes the oldest message |
| `rest[0]["role"] == "tool"` | | is the oldest one left a tool result? |
| a `while` inside a `while` | | after each drop, clean up any tool results that lost their call |

### 👀 Worked example: clearing a queue of orders

Remove the oldest orders until 3 or fewer are left. A "side" order can't stay without its main order, so remove sides that end up first:

```python
orders = ["main", "side", "side", "main", "main"]
while len(orders) > 3 and len(orders) > 1:
    orders.pop(0)
    while len(orders) > 1 and orders[0] == "side":
        orders.pop(0)
print(orders)   # ['main', 'main']
```

1. 5 orders > 3 → pop "main". Now the first one is "side" → inner loop pops it, and the next "side" too. Left: `["main", "main"]`.
2. 2 > 3? No. Stop.

Without the inner loop you'd stop at `["side", "main", "main"]`: a side with no main.

## 🎯 Your quest

**Part 1:** `decide(tool_name, policy)`. Replace `return "allow"` with:

- `return policy.get(tool_name, "ask")`

**Part 2:** `trim_history(messages, budget, tokens)`. Replace `return messages` with:

1. `system = messages[0]`
2. `rest = list(messages[1:])`
3. `while total_tokens([system] + rest, tokens) > budget and len(rest) > 1:`
4. `    rest.pop(0)`
5. `    while len(rest) > 1 and rest[0]["role"] == "tool":`
6. `        rest.pop(0)`
7. `return [system] + rest`

## Review

<details><summary>Why does an agent need a step limit?</summary>A confused model can call tools forever; the limit stops the loop.</details>
<details><summary>Where in the agent loop does a human approval fit?</summary>Between the model asking for a tool call and the harness running it.</details>
