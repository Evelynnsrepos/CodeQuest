---
title: Tools and agents
xp: 30
---
# Models that do things

> **Warm-up:** an LLM can't know today's weather or open your files. How do chatbots do those things anyway?

The model can't run code itself, but it can **ask** for it. You describe **tools** to it (name, what it does, which inputs). When it wants one, it answers with a structured request like `{"tool": "weather", "args": {"city": "Berlin"}}` instead of text. **Your code** runs the tool and sends back the result, and the model continues. An **agent** is just this in a loop until the model gives a final answer.

**MCP** (Model Context Protocol) is a standard way to package tools so any app (Claude, LM Studio, editors) can use them.

Two dangers: an agent can loop forever, so cap the steps; and text it reads (web pages, emails) can contain instructions meant to trick it (**prompt injection**), so don't give an agent tools that can do damage without your approval.

**Go deeper:** LLMs 3 (tools, MCP, agents), LLMs 9 lesson 09 (prompt injection), AI engineer 2 lesson 11 (traces).

<div class="quiz" data-answer="1" data-why="The model only writes a request like {&quot;tool&quot;: &quot;weather&quot;}. Your code runs it and sends back the result."><p><b>Predict first:</b> the model wants the weather in Berlin. Who actually runs the weather tool?</p><button>the model itself</button><button>your code, after the model asks</button></div>

## Your quest

`run_agent(model, tools, max_steps=5)`: keep a list `history`. Each step call `model(history)`:
- if it returns `{"answer": text}`, return `text`;
- if it returns `{"tool": name, "args": {...}}`, call `tools[name](**args)` and append `(name, result)` to `history`.

After `max_steps` steps without an answer, return `"gave up"`.

**Remember:** the model asks, your code acts, in a loop with a limit.
