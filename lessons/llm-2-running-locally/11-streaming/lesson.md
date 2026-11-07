---
title: Streaming replies token by token
minutes: 35
xp: 30
hint: Inside the loop, first: if line.startswith("data: ") == False: and under it continue
hint: Then: payload = line[len("data: "):] and if payload == "[DONE]": break
hint: Then: delta = json.loads(payload)["choices"][0]["delta"]
hint: Last line in the loop: text = text + delta.get("content", "")
---
# Server-sent events

⏱️ About 35 minutes

> **Warm-up:** in LM Studio's chat, the reply appears word by word. If the API from the last lesson returns one JSON object at the end, how does the text arrive piece by piece?

Add `"stream": true` to the request and the server sends the reply **as it is generated**, using **server-sent events (SSE)**: a long-lived HTTP response where each event is a line starting with `data: `, followed by a blank line.

```
data: {"choices": [{"index": 0, "delta": {"role": "assistant", "content": ""}}]}

data: {"choices": [{"index": 0, "delta": {"content": "Hal"}}]}

data: {"choices": [{"index": 0, "delta": {"content": "lo"}}]}

data: {"choices": [{"index": 0, "delta": {"content": "!"}, "finish_reason": "stop"}]}

data: [DONE]
```

Each chunk carries a **delta**: only the new piece of text, usually one token. The client glues the deltas together. The stream ends with the literal line `data: [DONE]`, which is *not* JSON.

Why bother? The time to the first visible word drops from "the whole reply" to "one token", which is what makes a chat feel responsive. Agents and tools also use streaming to stop early or show progress.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `raw.splitlines()` | "split into lines" | a list with one text per line |
| `line.startswith("data: ")` | | `True` if the line begins with exactly `data: ` |
| `== False` | "is false" | so `line.startswith("data: ") == False` means "does **not** start with it" |
| `continue` | | skip the rest of this round, go to the next line |
| `len("data: ")` | | 6: the number of characters in `data: ` (with the space) |
| `line[6:]` | "line from 6 on" | everything after the first 6 characters: the JSON part |
| `break` | | stop the whole loop |
| `delta.get("content", "")` | "delta get content, else empty" | the content, or `""` if this chunk has none (the first chunk often only has `role`) |
| `text = text + piece` | | glue the new piece to the end |

### 👀 Worked example: a radio message

Only lines starting with `MSG ` count, `OVER` ends the message:

```python
radio = "static\nMSG Hel\nMSG lo\nnoise\nOVER\nMSG never seen"
text = ""
for line in radio.splitlines():
    if line == "OVER":
        break
    if line.startswith("MSG ") == False:
        continue
    text = text + line[len("MSG "):]
print(text)   # Hello
```

| line | what happens |
|---|---|
| `static` | doesn't start with `MSG ` → continue |
| `MSG Hel` | add `Hel` |
| `MSG lo` | add `lo` → `Hello` |
| `noise` | continue |
| `OVER` | break: the loop ends, "never seen" is never read |

## 🎯 Your quest

Write `collect_stream(raw)`. Replace the `pass` line inside the loop with (8 spaces in front, 12 for the indented ones):

1. `if line.startswith("data: ") == False:`
2. `    continue`
3. `payload = line[len("data: "):]`
4. `if payload == "[DONE]":`
5. `    break`
6. `delta = json.loads(payload)["choices"][0]["delta"]`
7. `text = text + delta.get("content", "")`

Line 6 reads left to right: parse the JSON, take `choices`, its first item, then its `delta`.

## Review

<details><summary>What does finish_reason "length" tell you?</summary>The reply was cut off because it reached max_tokens; the model hadn't finished.</details>
<details><summary>Which endpoint do you send a chat to?</summary>POST /v1/chat/completions</details>
<details><summary>Why keep "serve on local network" off?</summary>Otherwise anyone on your network can use your model and GPU through the API.</details>
