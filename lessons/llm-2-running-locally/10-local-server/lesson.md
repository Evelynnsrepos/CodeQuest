---
title: LM Studio's local server and the OpenAI API
minutes: 30
xp: 35
hint: build_request: request = {}, then request["model"] = model, and the same for messages, temperature and max_tokens. Then return request
hint: parse_reply, line 1: data = json.loads(text), then choice = data["choices"][0]
hint: Then three lines: content = choice["message"]["content"], reason = choice["finish_reason"], tokens = data["usage"]["total_tokens"]
hint: Last line: return content, reason, tokens
---
# Talking to your model over HTTP

⏱️ About 30 minutes

> **Warm-up:** when an editor plugin or agent "uses your local model", how does it talk to LM Studio? Does it load the model itself?

No, it sends **HTTP requests** to LM Studio's server, which is already holding the model in VRAM. Start the server in LM Studio's *Developer* tab, or from a terminal:

```bash
lms server start          # serves on http://localhost:1234
lms ls                    # models you've downloaded
lms load qwen3-8b         # load one (use a name from lms ls)
lms ps                    # what's loaded right now
```

(`lms` is LM Studio's command line tool. If it isn't on your PATH, LM Studio can install it; the `lms` docs explain how for your version.)

The API copies OpenAI's format, so any OpenAI client library works by just changing the base URL. The two endpoints you'll use most:

```bash
curl http://localhost:1234/v1/models

curl http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen3-8b",
       "messages": [{"role": "user", "content": "Say hi in German."}],
       "temperature": 0.7, "max_tokens": 100}'
```

The answer is JSON too:

```json
{"id": "chatcmpl-123", "object": "chat.completion", "model": "qwen3-8b",
 "choices": [{"index": 0,
              "message": {"role": "assistant", "content": "Hallo!"},
              "finish_reason": "stop"}],
 "usage": {"prompt_tokens": 14, "completion_tokens": 3, "total_tokens": 17}}
```

Things to notice: you send the **whole conversation** every time (LLMs 1, lesson 13); the server applies the chat template for you; `finish_reason` is `"stop"` when the model ended on its own and `"length"` when it hit `max_tokens`; `usage` counts tokens.

The server listens only on your own computer unless you turn on "serve on local network". Leave that off unless you need it: anyone on your Wi-Fi could then use your GPU.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `request = {}` | | a new, empty dictionary |
| `request["model"] = model` | "request at model becomes model" | the key is the text `"model"` (quotes), the value comes from the box `model` (no quotes) |
| `json.loads(text)` | "JSON load string" | turns the JSON text of a reply into Python dictionaries and lists |
| `data["choices"][0]` | "data's choices, the first one" | `"choices"` is a list; `[0]` takes its first item |
| `choice["message"]["content"]` | | two lookups: the message, then its content |
| `return a, b, c` | | gives back three things at once (a **tuple**) |

### 👀 Worked example: unpacking a parcel tracking reply

```python
import json

text = '{"parcels": [{"status": {"where": "Berlin"}, "eta": "Monday"}], "count": {"total": 1}}'
data = json.loads(text)
parcel = data["parcels"][0]
where = parcel["status"]["where"]
eta = parcel["eta"]
total = data["count"]["total"]
print(where, eta, total)   # Berlin Monday 1
```

1. `json.loads` turns the text into a dictionary.
2. `data["parcels"]` is a list with one parcel; `[0]` takes it.
3. Inside it, `["status"]["where"]` goes two levels deep: `"Berlin"`.
4. `data["count"]["total"]` is at the top level of `data`, not inside the parcel.

`parse_reply` has the same shape: `choices` instead of `parcels`, `usage` instead of `count`.

## 🎯 Your quest

There's no server inside CodeQuest, so the starter uses a recorded response. In LLMs 4 you'll send the request for real.

**Part 1:** `build_request(model, messages, temperature, max_tokens)`. Replace `return {}` with:

1. `request = {}`
2. `request["model"] = model`
3. `request["messages"] = messages`
4. `request["temperature"] = temperature`
5. `request["max_tokens"] = max_tokens`
6. `return request`

**Part 2:** `parse_reply(text)`. Replace `return None, None, None` with:

1. `data = json.loads(text)`
2. `choice = data["choices"][0]`
3. `content = choice["message"]["content"]`
4. `reason = choice["finish_reason"]`
5. `tokens = data["usage"]["total_tokens"]`
6. `return content, reason, tokens`

## Review

<details><summary>What does HSA_OVERRIDE_GFX_VERSION do?</summary>It makes ROCm treat your GPU as a supported sibling target (for example 10.3.0 for RDNA2), so ROCm's precompiled code runs on it.</details>
<details><summary>Vulkan or ROCm for training with PyTorch?</summary>ROCm. Vulkan is only an option for running GGUF models with llama.cpp.</details>
