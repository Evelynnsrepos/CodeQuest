---
title: The harness around the model
xp: 40
---
# What an AI harness is

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

## Your quest

Build two harness parts.

1. `decide(tool_name, policy)`: `policy` maps tool names to `"allow"`, `"ask"` or `"deny"`. Return the tool's entry, and `"ask"` for any tool not in the policy (unknown tools must never run silently).
2. `trim_history(messages, budget, tokens)`: `tokens(message)` gives a message's size. Keep `messages[0]` (the system prompt) and the newest message always. While the total is over `budget`, delete the oldest message after the system prompt, and then also delete any `"tool"` messages that are now right after the system prompt (a tool result without its call confuses the model). Never delete the newest message. Return the new list (don't change the input).

## Review

<details><summary>Why does an agent need a step limit?</summary>A confused model can call tools forever; the limit stops the loop.</details>
<details><summary>Where in the agent loop does a human approval fit?</summary>Between the model asking for a tool call and the harness running it.</details>
