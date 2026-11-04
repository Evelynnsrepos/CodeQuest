---
title: LM Studio's local server and the OpenAI API
xp: 35
---
# Talking to your model over HTTP

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

## Python you need

`json.dumps(d)` turns a dictionary into JSON text, `json.loads(text)` does the reverse. Nested lookups chain: `data["choices"][0]["message"]["content"]`.

## Your quest

1. `build_request(model, messages, temperature, max_tokens)`: return a dictionary with exactly those four keys.
2. `parse_reply(text)`: parse the JSON text of a response and return a tuple `(content, finish_reason, total_tokens)`.

There's no server inside CodeQuest, so the starter uses a recorded response. In Module 4 you'll send the request for real.

## Review

<details><summary>What does HSA_OVERRIDE_GFX_VERSION do?</summary>It makes ROCm treat your GPU as a supported sibling target (for example 10.3.0 for RDNA2), so ROCm's precompiled code runs on it.</details>
<details><summary>Vulkan or ROCm for training with PyTorch?</summary>ROCm. Vulkan is only an option for running GGUF models with llama.cpp.</details>
