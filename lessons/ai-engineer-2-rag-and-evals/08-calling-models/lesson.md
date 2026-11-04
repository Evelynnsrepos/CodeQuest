---
title: Calling real models robustly
xp: 60
---
# Timeouts, retries and backoff

> **Warm-up:** your app calls a model API 10,000 times a day. What can go wrong with a single call?

It can be slow, the server can be overloaded (**HTTP 429** "too many requests", **503** "unavailable"), the network can drop, or the model can return something that isn't what you asked for. Production code handles all of these.

**The OpenAI-compatible API.** Ollama (`http://localhost:11434/v1`), LM Studio (`http://localhost:1234/v1`), vLLM and most hosted providers accept the same request:

```
POST {base}/chat/completions
{"model": "llama3.2", "messages": [{"role": "user", "content": "Hi"}], "temperature": 0}
→ {"choices": [{"message": {"content": "Hello!"}}], "usage": {"prompt_tokens": 9, "completion_tokens": 3}}
```

So one small client works with all of them (Anthropic's own API has a different shape; their SDK handles it).

**Retries with exponential backoff:** on 429, 5xx or a timeout, wait and try again, doubling the wait each time (1 s, 2 s, 4 s …), up to a limit. **Don't** retry 400 or 401: the request itself is wrong, and retrying won't fix it. If the server sends a `Retry-After` header, wait that long instead.

**Always set a timeout.** Without one, a stuck request hangs your app forever.

## Your quest

`chat(messages, model, base, client, retries=3, sleep=time.sleep)`:

1. POST to `{base}/chat/completions` with `json={"model": model, "messages": messages, "temperature": 0}` and `timeout=60` using `client.post`.
2. On status 429 or ≥ 500, or an `httpx.TimeoutException`: if attempts remain, call `sleep(wait)` and retry. `wait` starts at 1 and doubles; if the response has a `Retry-After` header, use `float()` of it instead. After `retries` retries, raise `RuntimeError("model unavailable")`.
3. Any other error status: `raise_for_status()` (no retry).
4. Return `(content, usage)` from the JSON.

(`sleep` is a parameter so the check can run without really waiting.)

**Remember:** timeout always; retry only what a retry can fix; back off exponentially.

## Review

<details><summary>Why let the model say "I don't know"?</summary>Otherwise it invents an answer when retrieval didn't find the right chunk.</details>
