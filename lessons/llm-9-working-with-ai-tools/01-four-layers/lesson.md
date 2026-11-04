---
title: The four layers of every AI setup
xp: 35
---
# Model, runner, harness, integrations

> **Warm-up:** when Claude Code "edits a file", which program actually writes to your disk: the model, or something else?

**In one sentence:** every AI setup is four layers stacked on each other (model, runner, harness, integrations), and once you can name the layer, you know which file or setting to change.

## 🪜 Plain words

| Layer | What it is | Examples | You change there |
|---|---|---|---|
| 1. **Model** | a file of numbers that predicts the next token; it can't do anything by itself | Qwen, Llama, Gemma, Claude | which model, size, quantization |
| 2. **Runner** | loads the weights onto the GPU/CPU and answers requests over an API | Ollama, llama.cpp, LM Studio, vLLM, Anthropic's API | GPU offload, context length, sampling, port |
| 3. **Harness** | the program you talk to: builds the prompt, runs the agent loop, calls tools | Claude Code, Open WebUI, Aider, LM Studio chat | system prompt, permissions, memory files |
| 4. **Integrations** | extra abilities plugged into the harness | MCP servers, tools, skills, hooks, subagents, plugins | install, write, enable, disable |

**Key idea:** the model only reads text and writes text. Every "the AI did something" was done by the **harness**, after the model asked for it.

## 🪜 Which integration?

The guide's rule of thumb, one question each:

| You need the model to… | Use |
|---|---|
| **know how** to do something | a **skill** or memory file (instructions) |
| **be able** to do something | a **tool** or **MCP server** (new abilities) |
| make something **always** happen, no matter what it decides | a **hook** (the harness runs it, the model can't skip it) |

## 🔀 What if you picked the wrong layer?

<div class="wrong"><b>"The model is too slow, let me change the system prompt"</b>: speed lives in the runner (GPU offload, quantization, context size). The harness can't fix it.</div>
<div class="wrong"><b>"Never run rm -rf" written in CLAUDE.md</b>: that's advice the model usually follows. A <b>hook</b> or a <b>deny rule</b> is enforced every time.</div>
<div class="right">speed → runner, behaviour → harness, abilities → integrations, guarantees → hooks/permissions ✓</div>

## 🎯 Your quest

1. `layer_of(name)`: return `"model"`, `"runner"`, `"harness"` or `"integration"` for the names in the table above (case-insensitive). Unknown → `"unknown"`.
2. `pick_integration(need)`: `need` is `"know how"`, `"be able"` or `"always"`; return `"skill"`, `"mcp"` or `"hook"`.

**Remember:** the model writes text; the harness does things.

## Review

<details><summary>What does the harness add on top of a model?</summary>Prompt assembly, the agent loop, tool running, permissions, context and memory.</details>
