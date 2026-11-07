---
title: The four layers of every AI setup
minutes: 25
xp: 35
hint: layer_of: n = name.lower(), then for layer in LAYERS: and inside it if n in LAYERS[layer]: return layer
hint: After the loop (4 spaces): return "unknown"
hint: pick_integration: three ifs, like if need == "know how": and under it return "skill"
---
# Model, runner, harness, integrations

⏱️ About 25 minutes

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

## 🐍 Python you need

`LAYERS` is **given** in the starter: a dictionary where each layer name points to a list of names.

| You write | Say it | What it does |
|---|---|---|
| `name.lower()` | "name lower" | the same text in small letters: `"Ollama".lower()` is `"ollama"` |
| `for layer in LAYERS:` | "for each layer in layers" | goes through the dictionary's keys: `"model"`, `"runner"`, ... |
| `LAYERS[layer]` | "layers at layer" | the list stored under that key |
| `if n in some_list:` | "if n is in the list" | true when the list holds exactly that text |
| `return layer` | "return layer" | stops the function **right away** and gives back the answer |
| `if need == "always":` | "if need equals always" | two `=` compare; one `=` would store |

### 👀 Worked example: which shelf?

```python
SHELVES = {"fruit": ["apple", "pear"], "veg": ["carrot", "leek"]}

def shelf_of(item):
    n = item.lower()
    for shelf in SHELVES:
        if n in SHELVES[shelf]:
            return shelf
    return "unknown"

print(shelf_of("Carrot"))
```

1. `n` = `"carrot"` (small letters, so `"Carrot"` and `"carrot"` both work).
2. `shelf` = `"fruit"`: is `"carrot"` in `["apple", "pear"]`? No, keep going.
3. `shelf` = `"veg"`: is it in `["carrot", "leek"]`? Yes → `return "veg"`. The function stops here.
4. If no shelf had matched, the loop would end and `return "unknown"` would run.

## 🎯 Your quest

1. `layer_of(name)`: return `"model"`, `"runner"`, `"harness"` or `"integration"` for the names in the table above (case-insensitive). Unknown → `"unknown"`.
2. `pick_integration(need)`: `need` is `"know how"`, `"be able"` or `"always"`; return `"skill"`, `"mcp"` or `"hook"`.

**Part 1:** in `layer_of`, replace `return "unknown"` with the worked example's shape:

1. `n = name.lower()`
2. `for layer in LAYERS:`
3. `    if n in LAYERS[layer]:`
4. `        return layer`
5. `return "unknown"`

**Part 2:** in `pick_integration`, replace `return None` with:

1. `if need == "know how":`
2. `    return "skill"`
3. `if need == "be able":`
4. `    return "mcp"`
5. `if need == "always":`
6. `    return "hook"`

The starter has these lines as `#` comments. You can delete the `# ` in front of each.

**Remember:** the model writes text; the harness does things.

## Review

<details><summary>What does the harness add on top of a model?</summary>Prompt assembly, the agent loop, tool running, permissions, context and memory.</details>
