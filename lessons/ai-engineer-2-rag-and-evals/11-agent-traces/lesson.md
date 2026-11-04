---
title: Agents you can debug: traces
xp: 60
---
# What did the agent actually do?

> **Warm-up:** your agent answered wrong. Was it the model's plan, a tool's result, or a tool error? How would you find out?

An agent (LLMs 3) is a loop: the model picks a tool, your code runs it, the result goes back, repeat until a final answer. When it fails, you need a **trace**: one record ("span") per step, with what went in, what came out, how long it took and any error. Tools like **Langfuse**, **Arize Phoenix** and **OpenTelemetry** store and show these; underneath they're lists of dicts like the ones you'll build.

A span here:

```python
{"step": 1, "type": "tool", "name": "search_notes", "args": {"q": "nix gc"},
 "result": "...", "error": None, "ms": 12.5}
```

Then **failure analysis**: run the agent over many tasks, collect traces, and count **where** things go wrong: which tool errors most, how often the agent hits the step limit, which tasks loop on the same call. You fix the biggest bucket first.

## Your quest

`run_agent(task, model, tools, max_steps=5)` runs this loop and returns `(answer, trace)`:

- `model(task, trace)` returns either `{"tool": name, "args": {...}}` or `{"answer": text}`.
- For a tool call: run `tools[name](**args)`, timing it with `time.perf_counter()`. Record a span with `type "tool"`, the result (or `None`) and the error as `f"{type(e).__name__}: {e}"` (or `None`). An unknown tool name is an error span `"KeyError: <name>"` too. Keep going after errors: the model sees them in the trace.
- For an answer: record a span `{"step": n, "type": "answer", "name": None, "args": None, "result": text, "error": None, "ms": 0.0}` and return.
- After `max_steps` model calls without an answer, return `(None, trace)`.
- Steps are numbered from 1.

Then `failure_summary(traces)` over a list of `(answer, trace)` pairs returns `{"runs": n, "no_answer": n, "tool_errors": {tool_name: count}}`.

**Remember:** trace every step; count failures by kind before fixing.

## Review

<details><summary>Why parametrize an eval test per golden item?</summary>A failure then names exactly which question broke.</details>
