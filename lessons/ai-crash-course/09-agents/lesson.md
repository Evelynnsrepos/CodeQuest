---
title: Tools and agents
xp: 30
hint: Start with history = [] and then for step in range(max_steps): and inside it action = model(history)
hint: if "answer" in action: return action["answer"] (12 spaces for the return)
hint: Otherwise: tool = tools[action["tool"]], result = tool(action["args"]), history.append((action["tool"], result)). After the loop: return "gave up"
---
# Models that do things

⏱️ About 30 minutes · one function with a loop

> **Warm-up:** an LLM can't know today's weather or open your files. How do chatbots do those things anyway?

**In one sentence:** the model can't run anything itself, but it can **ask** your code to run a **tool**; an **agent** is that ask-run-answer cycle in a loop, with a step limit.

## 💡 The idea in plain words

1. You tell the model which **tools** exist (name, what it does, which inputs).
2. When the model wants one, it doesn't answer with normal text. It answers with a structured request like `{"tool": "weather", "args": {"city": "Berlin"}}`.
3. **Your code** reads that request, runs the tool, and sends the result back.
4. The model continues: either it asks for another tool, or it gives a final answer like `{"answer": "It's 12 °C in Berlin."}`.

An **agent** is just steps 2–4 in a loop until the model gives a final answer.

**MCP** (Model Context Protocol) is a standard way to package tools so any app (Claude, LM Studio, editors) can use them.

Two dangers:

- An agent can **loop forever**, so always cap the number of steps.
- Text it reads (web pages, emails) can contain instructions meant to trick it (**prompt injection**), so don't give an agent tools that can do damage without your approval.

<div class="quiz" data-answer="1" data-why="The model only writes a request like {&quot;tool&quot;: &quot;weather&quot;}. Your code runs it and sends back the result."><p><b>Predict first:</b> the model wants the weather in Berlin. Who actually runs the weather tool?</p><button>the model itself</button><button>your code, after the model asks</button></div>

**Go deeper:** LLMs 3 (tools, MCP, agents), LLMs 9 lesson 09 (prompt injection), AI engineer 2 lesson 11 (traces).

## 🐍 Python you need

### Functions are values too

You can put a function into a box or a dictionary, and call it later with `( )`:

```python
def weather(args):
    return "12 °C in " + args["city"]

tools = {"weather": weather}      # the key "weather" holds the function itself (no brackets!)
tool = tools["weather"]           # take the function out of the dictionary
print(tool({"city": "Berlin"}))   # call it: shows 12 °C in Berlin
```

- `{"weather": weather}`: without `( )`, `weather` means *the function itself*, not its answer.
- `tool(...)`: with `( )`, the function runs.
- Each tool here takes **one** input, `args`: a dictionary of its inputs, e.g. `{"city": "Berlin"}`.

### The pieces table

| You write | Say it | What it does |
|---|---|---|
| `action = model(history)` | "action becomes model of history" | asks the model what to do next. You're given `model`; it gives back a dictionary. |
| `"answer" in action` | "answer in action" | `True` if the dictionary has the key `"answer"` (lesson 01) |
| `action["answer"]` | "action at answer" | the text of the final answer |
| `action["tool"]`, `action["args"]` | | the tool's name, and its inputs dictionary |
| `tools[action["tool"]]` | "tools at the tool's name" | read inside out: first `action["tool"]` gives `"weather"`, then `tools["weather"]` gives the function |
| `history.append((name, result))` | "append the pair name, result" | adds one **pair** (lesson 08's tuple) to the list. Note the **double** brackets: the outer ones belong to `append`, the inner ones make the pair. |
| `return "gave up"` | | the text to give back when the steps run out |

### 👀 Worked example: a calculator robot

Here the "model" is a list of instructions read one by one. It's the same loop shape as your agent: a step limit, look at what to do, stop on a final answer, otherwise run something and record it.

```python
def follow(orders, max_steps):
    log = []
    for step in range(max_steps):
        if step >= len(orders):
            return "out of orders"
        order = orders[step]
        if "answer" in order:
            return order["answer"]
        result = order["a"] + order["b"]
        log.append(("add", result))
    return "gave up"
```

(`step >= len(orders)` means "step is bigger than or equal to the number of orders": we've used them all up. Your agent doesn't need this line, because a real model always has something to say.)

`follow([{"a": 2, "b": 3}, {"answer": "done"}], 5)`:

1. step 0: order `{"a": 2, "b": 3}` has no `"answer"`, so compute 5 and log `("add", 5)`.
2. step 1: order `{"answer": "done"}` has an answer → give back `"done"`.

With `max_steps` = 1, it stops after step 0 and gives back `"gave up"`.

## 🎯 Your quest

Write `run_agent(model, tools, max_steps=5)`:

1. `history = []`
2. `for step in range(max_steps):` and inside it:
   - `action = model(history)`
   - `if "answer" in action:` → `return action["answer"]`
   - `tool = tools[action["tool"]]`
   - `result = tool(action["args"])`
   - `history.append((action["tool"], result))`
3. after the loop (4 spaces): `return "gave up"`

The `model` at the bottom of the editor first asks for the weather tool, then answers using the result. Press **Run**: it should print `It's 12 °C and rainy in Berlin.`

**Remember:** the model asks, your code acts, in a loop with a limit.
