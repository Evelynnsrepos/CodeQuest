---
title: Clean JSON from small local models
xp: 30
---
# Dig the JSON out of a chatty reply

⏱️ About 12 minutes · one function

> **Warm-up:** you ask a 4B model for `{"label": ..., "urgent": ...}` and get: "Sure! Here is the JSON: ```json {"label": "work", "urgent": true} ``` Hope that helps!". What breaks?

**In one sentence:** first **force** the format where you can, and then still **extract** and check the JSON in code, because small local models like to chat around it.

## 🪜 Force it (best)

- In the AI Agent or Basic LLM Chain node, turn on **Require Specific Output Format** and plug in a **Structured Output Parser** sub-node with an example or a JSON schema.
- Ollama and LM Studio can also constrain the model itself to valid JSON (Ollama's `format`, LM Studio's `response_format` with a JSON schema), so it can only produce matching tokens. Use this from an HTTP Request node when the parser keeps failing.
- `temperature` 0 to 0.3 for anything a machine reads.

## 🪜 Rescue it (always)

Checking the shape against a schema is LLMs 9, lesson 08. Here's the step before: get the JSON out at all. Look for a ```` ```json ```` fence first; otherwise take everything from the first `{` to the last `}`; then try `json.loads`.

## 🎯 Your quest

Press **Run** first: the starter's plain `json.loads` crashes on the chatty reply.


Write `extract_json(reply)`:

1. If the reply contains a fenced block ```` ```json ... ``` ```` (or just ```` ``` ... ``` ````), use what's inside the first one.
2. Otherwise, use the text from the first `{` to the last `}`.
3. Return `json.loads` of that, or `None` if there's nothing to parse or it isn't valid JSON.

<details><summary>💡 Hint 1</summary><code>m = re.search(r"```(?:json)?\s*(.*?)```", reply, re.S)</code>. <code>re.S</code> lets <code>.</code> match newlines too.</details>
<details><summary>💡 Hint 2</summary><code>start, end = reply.find("{"), reply.rfind("}")</code>. If either is <code>-1</code>, there's no object. Wrap <code>json.loads</code> in <code>try</code>/<code>except json.JSONDecodeError</code>.</details>

**Remember:** force the format, then extract, then validate.

## Review

<details><summary>Lesson 7: how many tools should a small local model's agent get?</summary>About 2 to 4, each with a clear description.</details>
