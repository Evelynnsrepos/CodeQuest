---
title: Agents you can debug: traces
minutes: 50
xp: 60
hint: run_agent: trace = [], for step in range(1, max_steps + 1): action = model(task, trace). If "answer" in action: append the answer span and return
hint: Tool call: name = action["tool"], args = action.get("args", {}), start = time.perf_counter(), result = None, error = None
hint: try: raise KeyError(name) if the tool is unknown, else result = tools[name](**args). except KeyError as e: and except Exception as e: build the error text
hint: After the try: ms = (time.perf_counter() - start) * 1000, append the tool span. After the loop: return None, trace
hint: failure_summary: count answers that are None, and for every tool span with an error: errors[name] = errors.get(name, 0) + 1
---
# What did the agent actually do?

⏱️ About 50 minutes

> **Warm-up:** your agent answered wrong. Was it the model's plan, a tool's result, or a tool error? How would you find out?

An agent (LLMs 3) is a loop: the model picks a tool, your code runs it, the result goes back, repeat until a final answer. When it fails, you need a **trace**: one record ("span") per step, with what went in, what came out, how long it took and any error. Tools like **Langfuse**, **Arize Phoenix** and **OpenTelemetry** store and show these; underneath they're lists of dicts like the ones you'll build.

A span here:

```python
{"step": 1, "type": "tool", "name": "search_notes", "args": {"q": "nix gc"},
 "result": "...", "error": None, "ms": 12.5}
```

Then **failure analysis**: run the agent over many tasks, collect traces, and count **where** things go wrong: which tool errors most, how often the agent hits the step limit, which tasks loop on the same call. You fix the biggest bucket first.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `for step in range(1, max_steps + 1):` | | 1, 2, ..., max_steps: steps counted from 1 |
| `"answer" in action` | | does the model's reply have an `"answer"` key? |
| `time.perf_counter()` | | a precise clock in seconds; the difference of two readings is how long something took |
| `* 1000` | | seconds → milliseconds |
| `raise KeyError(name)` | | makes the "unknown tool" error ourselves, so it's handled like other errors |
| `tools[name](**args)` | | calls the tool with the arguments unpacked (AI automation 1, lesson 10) |
| `except KeyError as e:` | | catches that error and calls it `e`. `e.args[0]` is the name we gave it. |
| `except Exception as e:` | | catches any other error |
| `type(e).__name__` | | the error's kind as text: `"ValueError"`, `"KeyError"` |
| `span["error"]` in an `if` | | an error text counts as true, `None` as false |

### 👀 Worked example: a run with one error

The model asks for `"web"` (not in `tools`), then `"search"`, then answers:

1. Step 1: `"web"` isn't a tool → `raise KeyError("web")` → caught → error `"KeyError: web"`, result `None`. The span is recorded, and the loop goes on.
2. Step 2: `search(q=...)` works → result `["nix-gc"]`, error `None`.
3. Step 3: `{"answer": "..."}` → the answer span → return.

`failure_summary([(answer, trace)])` then gives `{"runs": 1, "no_answer": 0, "tool_errors": {"web": 1}}`.

## 🎯 Your quest

`run_agent(task, model, tools, max_steps=5)` runs this loop and returns `(answer, trace)`:

- `model(task, trace)` returns either `{"tool": name, "args": {...}}` or `{"answer": text}`.
- For a tool call: run `tools[name](**args)`, timing it with `time.perf_counter()`. Record a span with `type "tool"`, the result (or `None`) and the error as `f"{type(e).__name__}: {e}"` (or `None`). An unknown tool name is an error span `"KeyError: <name>"` too. Keep going after errors: the model sees them in the trace.
- For an answer: record a span `{"step": n, "type": "answer", "name": None, "args": None, "result": text, "error": None, "ms": 0.0}` and return.
- After `max_steps` model calls without an answer, return `(None, trace)`.
- Steps are numbered from 1.

Then `failure_summary(traces)` over a list of `(answer, trace)` pairs returns `{"runs": n, "no_answer": n, "tool_errors": {tool_name: count}}`.

**Part 1:** `run_agent`. Replace `return None, []` with:

1. `trace = []`
2. `for step in range(1, max_steps + 1):`
3. `    action = model(task, trace)`
4. `    if "answer" in action:`
5. `        span = {"step": step, "type": "answer", "name": None, "args": None, "result": action["answer"], "error": None, "ms": 0.0}`
6. `        trace.append(span)`
7. `        return action["answer"], trace`
8. `    name = action["tool"]`
9. `    args = action.get("args", {})`
10. `    start = time.perf_counter()`
11. `    result = None`
12. `    error = None`
13. `    try:`
14. `        if name not in tools:`
15. `            raise KeyError(name)`
16. `        result = tools[name](**args)`
17. `    except KeyError as e:`
18. `        error = type(e).__name__ + ": " + str(e.args[0])`
19. `    except Exception as e:`
20. `        error = type(e).__name__ + ": " + str(e)`
21. `    ms = (time.perf_counter() - start) * 1000`
22. `    span = {"step": step, "type": "tool", "name": name, "args": args, "result": result, "error": error, "ms": ms}`
23. `    trace.append(span)`
24. `return None, trace`

**Part 2:** `failure_summary`. Replace its `return` line with:

1. `errors = {}`
2. `no_answer = 0`
3. `for answer, trace in traces:`
4. `    if answer is None:`
5. `        no_answer = no_answer + 1`
6. `    for span in trace:`
7. `        if span["type"] == "tool" and span["error"]:`
8. `            errors[span["name"]] = errors.get(span["name"], 0) + 1`
9. `return {"runs": len(traces), "no_answer": no_answer, "tool_errors": errors}`

**Remember:** trace every step; count failures by kind before fixing.

## Review

<details><summary>Why parametrize an eval test per golden item?</summary>A failure then names exactly which question broke.</details>
