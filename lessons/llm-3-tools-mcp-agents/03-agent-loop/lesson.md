---
title: The agent loop
minutes: 30
xp: 40
hint: for _ in range(max_steps): and inside it reply = model(messages) and messages.append(reply)
hint: Still inside: if reply.get("tool_calls"): messages.extend(run_tool_calls(reply, tools))
hint: else: return reply["content"]
hint: After the loop: return "stopped: too many steps"
---
# Think, act, observe, repeat

⏱️ About 30 minutes

> **Warm-up:** "Summarize the newest file in my notes folder" needs two tool calls, and the second depends on the first one's result. Who decides when to make the second call?

The model does, in a loop. An **agent** is nothing more than this:

```
messages = [system prompt, user request]
repeat (at most N times):
    reply = model(messages, tools)
    messages.append(reply)
    if reply has tool calls:
        run them, append each result as a tool message      ← observe
    else:
        return reply's text                                  ← done
```

Every round, the model sees the *whole history*: the request, its own earlier calls, and every result. That's how it can plan ("first list the files, then read the newest") and recover from errors ("unknown tool, let me try another").

Some things that matter in real agents:

- **A step limit.** A confused model can loop forever (call, fail, call again). Always cap the rounds.
- **Context growth.** Every tool result goes into the context window. A tool that returns a 50,000-token file can push the original request out (LLMs 1, lesson 13). Good tools return short, focused results.
- **Approvals.** LM Studio asks you before running a tool call unless you allow it. The agent loop is where a human-in-the-loop check fits.
- **Reasoning models** often "think" between calls, which improves planning but costs tokens.

This is exactly what boot.dev's *Build an AI Agent* course builds against a real API; in Module 4 you'll point the same loop at LM Studio.

## 🐍 Python you need

`run_tool_calls` is your solution from the last lesson. `scripted_model` and `tool_call` are given helpers: they pretend to be LM Studio by replaying a recorded conversation.

| You write | Say it | What it does |
|---|---|---|
| `for _ in range(max_steps):` | "repeat max-steps times" | `_` means "I don't need the counter" |
| `reply = model(messages)` | | asks the (fake) model for its next message |
| `messages.append(reply)` | | adds one message to the history |
| `reply.get("tool_calls")` | | the tool calls, or `None` if the reply has none. `if None:` counts as false. |
| `messages.extend(a_list)` | "messages extend" | adds **every** item of the list to the end (append would add the list as one item) |
| `return reply["content"]` inside the loop | | ends the whole function with the answer |
| `return ...` after the loop | | only reached if every round asked for tools |

### 👀 Worked example: asking until someone answers

```python
def ask_around(people, max_tries):
    for i in range(max_tries):
        answer = people[i]
        if answer == "?":
            print("they asked a question back, keep going")
        else:
            return answer
    return "nobody knew"

print(ask_around(["?", "?", "Paris"], 5))   # Paris
print(ask_around(["?", "?", "?"], 2))       # nobody knew
```

1. Round 0: `"?"`: no answer yet, go round again.
2. Round 1: `"?"`: again.
3. Round 2: `"Paris"`: a real answer → `return`, the function ends.

In the second call, the limit of 2 rounds is reached first, so the line after the loop runs. An agent works the same way, with tool calls instead of `"?"`.

## 🎯 Your quest

Write `run_agent(messages, model, tools, max_steps)`. Replace `return ""` with:

1. `for _ in range(max_steps):`
2. `    reply = model(messages)`
3. `    messages.append(reply)`
4. `    if reply.get("tool_calls"):`
5. `        messages.extend(run_tool_calls(reply, tools))`
6. `    else:`
7. `        return reply["content"]`
8. `return "stopped: too many steps"`

Press **Run** and watch "model sees … messages" grow: every round the model sees the whole history.

## Review

<details><summary>What does finish_reason "tool_calls" mean?</summary>The model stopped to request one or more tool calls instead of answering.</details>
<details><summary>Why send tool errors back to the model instead of raising them?</summary>So the model can see what went wrong and correct itself in the next round.</details>
<details><summary>What links a tool result to its call?</summary>The tool_call_id, which must match the call's id.</details>
