---
title: Clean JSON from small local models
minutes: 40
xp: 30
hint: Start: fence = "`" * 3 and first = reply.find(fence). Then if first != -1: (there is a fence)
hint: Inside that if: second = reply.find(fence, first + 3), text = reply[first + 3:second], and if text.startswith("json"): text = text[4:]
hint: else: start = reply.find("{") and end = reply.rfind("}"), if start == -1 or end < start: return None, then text = reply[start:end + 1]
hint: At the end: try: return json.loads(text) and except json.JSONDecodeError: return None
---
# Dig the JSON out of a chatty reply

⏱️ About 40 minutes · one function, in three parts

> **Warm-up:** you ask a 4B model for `{"label": ..., "urgent": ...}` and get: "Sure! Here is the JSON: ```json {"label": "work", "urgent": true} ``` Hope that helps!". What breaks?

**In one sentence:** first **force** the format where you can, and then still **extract** and check the JSON in code, because small local models like to chat around it.

## 🪜 Force it (best)

- In the AI Agent or Basic LLM Chain node, turn on **Require Specific Output Format** and plug in a **Structured Output Parser** sub-node with an example or a JSON schema.
- Ollama and LM Studio can also constrain the model itself to valid JSON (Ollama's `format`, LM Studio's `response_format` with a JSON schema), so it can only produce matching tokens. Use this from an HTTP Request node when the parser keeps failing.
- `temperature` 0 to 0.3 for anything a machine reads.

## 🪜 Rescue it (always)

Checking the shape against a schema is LLMs 9, lesson 08. Here's the step before: get the JSON out at all. Look for a ```` ```json ```` fence first; otherwise take everything from the first `{` to the last `}`; then try `json.loads`.

## 🐍 Python you need

A **fence** is three backticks in a row (the key left of 1 on many keyboards). Writing three backticks inside code is confusing to read, so we build them: `` "`" * 3 ``. A text times a number repeats it: `"ab" * 3` is `"ababab"`.

| You write | Say it | What it does |
|---|---|---|
| `reply.find("{")` | "find the first curly bracket" | the **position** of the first `{`, counting from 0. If there is none: `-1`. |
| `reply.find(fence, 10)` | "find the fence, starting at 10" | the same, but only looks from position 10 on |
| `reply.rfind("}")` | "find from the right" | the position of the **last** `}` |
| `!= -1` | "is not minus one" | "it was found" |
| `reply[5:12]` | "reply from 5 up to 12" | the characters at positions 5, 6, …, 11 (12 is **not** included) |
| `end + 1` | | so the slice includes the `}` itself |
| `text[4:]` | "text from 4 on" | cuts off the first 4 characters (the word `json`) |
| `json.loads(text)` | "JSON load string" | turns JSON text into Python dictionaries and lists. Spaces and line breaks around it are fine. |
| `except json.JSONDecodeError:` | | catches the error `json.loads` raises when the text isn't valid JSON |

### 👀 Worked example 1: first to last bracket

`reply = 'I say {"a": 1} ok'`. Positions: `I`=0, space=1, `s`=2, `a`=3, `y`=4, space=5, `{`=6 … `}`=13.

1. `start = reply.find("{")` → **6**.
2. `end = reply.rfind("}")` → **13**.
3. `reply[6:14]` (that's `end + 1`) → `{"a": 1}`.
4. `json.loads('{"a": 1}')` → the dictionary `{"a": 1}`.

If there were no `{`, `start` would be `-1`, and we return `None`. If the `}` came **before** the `{` (like `"} oops {"`), then `end < start`, and that's no object either.

### 👀 Worked example 2: between two fences

Say the reply is: three backticks, `json`, a line break, `{"x": 2}`, a line break, three backticks.

1. `first = reply.find(fence)` → 0: the first fence starts at position 0.
2. `second = reply.find(fence, first + 3)`: search again **after** the first fence (it's 3 characters long) → the closing fence.
3. `text = reply[first + 3:second]` → everything between the fences: `json`, line break, `{"x": 2}`, line break.
4. `text.startswith("json")` → true, so `text = text[4:]` drops the word. Left: line break, `{"x": 2}`, line break. `json.loads` ignores the line breaks.

## 🎯 Your quest

Press **Run** first: the starter's plain `json.loads` crashes on the chatty reply.

Write `extract_json(reply)`. Replace `return json.loads(reply)` with:

1. `` fence = "`" * 3 ``
2. `first = reply.find(fence)`
3. **Part 1, a fence was found** (worked example 2):
   - `if first != -1:`
   - `    second = reply.find(fence, first + 3)`
   - `    text = reply[first + 3:second]`
   - `    if text.startswith("json"):`
   - `        text = text[4:]`
4. **Part 2, no fence** (worked example 1):
   - `else:`
   - `    start = reply.find("{")`
   - `    end = reply.rfind("}")`
   - `    if start == -1 or end < start:`
   - `        return None`
   - `    text = reply[start:end + 1]`
5. **Part 3, parse it safely:**
   - `try:`
   - `    return json.loads(text)`
   - `except json.JSONDecodeError:`
   - `    return None`

**Remember:** force the format, then extract, then validate.

## Review

<details><summary>Lesson 7: how many tools should a small local model's agent get?</summary>About 2 to 4, each with a clear description.</details>
<details><summary>What does "hello".find("z") give?</summary>-1, which means "not found".</details>
