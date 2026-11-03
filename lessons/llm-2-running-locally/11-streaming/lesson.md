---
title: Streaming replies token by token
xp: 30
---
# Server-sent events

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

## Python you need

`text.splitlines()` splits text into lines. `line.startswith("data: ")` and `line[len("data: "):]` strip the prefix. `continue` skips to the next loop round, `break` leaves the loop. `delta.get("content", "")` returns `""` if the key is missing.

## Your quest

Write `collect_stream(raw)`: go through the lines of a raw SSE stream, ignore lines that don't start with `data: `, stop at `[DONE]`, parse the JSON of every other event and add its `choices[0]["delta"]` content to the result. Return the full text.

## Review

<details><summary>What does finish_reason "length" tell you?</summary>The reply was cut off because it reached max_tokens; the model hadn't finished.</details>
<details><summary>Which endpoint do you send a chat to?</summary>POST /v1/chat/completions</details>
<details><summary>Why keep "serve on local network" off?</summary>Otherwise anyone on your network can use your model and GPU through the API.</details>
