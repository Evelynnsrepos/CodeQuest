---
title: The agent loop
xp: 40
---
# Think, act, observe, repeat

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

## Your quest

Write `run_agent(messages, model, tools, max_steps)`:

- Call `model(messages)` to get the reply dictionary, and append it to `messages`.
- If the reply has `"tool_calls"` (use `reply.get("tool_calls")`), extend `messages` with `run_tool_calls(reply, tools)` and go round again.
- Otherwise return `reply["content"]`.
- If the loop runs `max_steps` times without a final answer, return `"stopped: too many steps"`.

`model` is a scripted stand-in for LM Studio that replays a recorded conversation. `run_tool_calls` is your solution from the last lesson.

## Review

<details><summary>What does finish_reason "tool_calls" mean?</summary>The model stopped to request one or more tool calls instead of answering.</details>
<details><summary>Why send tool errors back to the model instead of raising them?</summary>So the model can see what went wrong and correct itself in the next round.</details>
<details><summary>What links a tool result to its call?</summary>The tool_call_id, which must match the call's id.</details>
