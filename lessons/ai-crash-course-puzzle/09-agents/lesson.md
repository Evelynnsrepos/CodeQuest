---
title: Agents, a model in a loop
minutes: 25
xp: 30
hint: Each turn: action = model(history). If it has an answer, return action["answer"].
hint: Otherwise: tool = tools[action["tool"]], result = tool(action["args"]), history.append((action["tool"], result)).
distractor: result = tool(action)
distractor: return "gave up"
---
# Agents

⏱️ About 25 minutes · 🧩 5 gaps, 2 decoys

> **Warm-up:** how would *you* find out the weather in Berlin right now?

**In one sentence:** an **agent** is a model in a loop: it either answers, or asks to use a **tool**; your code runs the tool and shows the model the result; repeat.

## 💡 The idea

A model on its own can only write text. It can't look things up. So we give it tools (functions like `weather`), and run this loop:

1. Show the model everything so far (the **history**).
2. The model says either **"here's my answer"** or **"please run tool X with these inputs"**.
3. If it's an answer: done.
4. If it's a tool request: run the tool, add the result to the history, go back to 1.
5. Stop after a few turns anyway (`max_steps`), so a confused model can't loop forever.

Claude Code, ChatGPT with search and every "AI agent" are this loop with a smarter model and more tools.

## 🐍 The Python in this puzzle

The model's reply is a dictionary. Either `{"answer": "It's sunny"}` or `{"tool": "weather", "args": {"city": "Berlin"}}`.

| Piece | Say it | What it does |
|---|---|---|
| `model(history)` | "call model with history" | asks the model what to do next |
| `"answer" in action` | "answer in action" | `True` if the reply has an `"answer"` key |
| `action["tool"]` | "action at tool" | the tool's name, e.g. `"weather"` |
| `tools[...]` | "tools at that name" | looks up the actual function by its name |
| `tool(action["args"])` | "call the tool with the args" | runs it with just its inputs |
| `(a, b)` | "a pair" | two things kept together, a **tuple** |
| `history.append((name, result))` | | adds one pair to the history (two sets of brackets: one for append, one for the pair) |

## 🧩 Your puzzle

Inside the loop, in order:

1. Ask the model what to do.
2. If it answered, give back **the answer** (decoy: giving back `"gave up"` here would quit too early).
3. Look up the tool by its name.
4. Run it with **just the args** (decoy: `tool(action)` hands it the whole reply).
5. Remember the pair (tool name, result).

Run it: `It's 12 °C and rainy in Berlin.`

**Remember:** ask, run the tool, show the result, repeat.
