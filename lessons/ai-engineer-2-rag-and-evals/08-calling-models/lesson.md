---
title: Calling real models robustly
minutes: 50
xp: 60
hint: Start: wait = 1.0, url = base + "/chat/completions", payload = {...}, then for attempt in range(retries + 1):
hint: Inside: try: r = client.post(url, timeout=60, json=payload) and except httpx.TimeoutException: r = None
hint: Success: if r is not None and r.status_code != 429 and r.status_code < 500: raise_for_status, read the JSON, return content and usage
hint: Otherwise: break on the last attempt. Else pick delay (Retry-After header or wait), sleep(delay), wait = wait * 2. After the loop: raise RuntimeError("model unavailable")
---
# Timeouts, retries and backoff

⏱️ About 50 minutes

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

## 🧮 Worked example

A call fails with 503 three times, then works. The waits double each time:

| attempt | result | wait before the next try |
|---|---|---|
| 1 | 503 | 1 s |
| 2 | 503 | 2 s |
| 3 | 429 with `Retry-After: 10` | 10 s (the server's number wins) |
| 4 | 200 OK | done |

A 401 on attempt 1 would stop right away: a wrong API key stays wrong however often you retry.

```python
for attempt in range(4):
    print(f"attempt {attempt + 1}: wait {2 ** attempt} s if it fails")   # 1, 2, 4, 8
```

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `for attempt in range(retries + 1):` | | the first try plus `retries` retries: 4 tries for retries = 3 |
| `try:` / `except httpx.TimeoutException:` | | if the request takes too long, don't crash: remember "no response" (`r = None`) |
| `r.status_code` | | the HTTP number: 200 OK, 429 "too many requests", 500+ "server broke" |
| `r is not None and r.status_code != 429 and r.status_code < 500` | | "we got an answer that a retry won't change" |
| `data["choices"][0]["message"]["content"]` | | digs into the JSON: the first choice's message text |
| `data.get("usage", {})` | | the token counts, or `{}` if missing |
| `"Retry-After" in r.headers` | | did the server say how long to wait? |
| `sleep(delay)` | | waits that many seconds (in the check, a fake that doesn't really wait) |
| `wait = wait * 2` | | 1, 2, 4, 8, ...: **exponential back-off** |
| `raise RuntimeError("...")` | | gives up with an error |

### 👀 Worked example: two 503s, then success

1. Attempt 0: status 503 (≥ 500) → not the last attempt → no Retry-After → sleep(1), wait becomes 2.
2. Attempt 1: 503 again → sleep(2), wait becomes 4.
3. Attempt 2: 200 → `raise_for_status()` does nothing for 200 → return the text and usage.

A 401 ("bad API key") goes straight into the success branch's `raise_for_status()`, which raises right away: no retry, because waiting won't fix a wrong key.

## 🎯 Your quest

`chat(messages, model, base, client, retries=3, sleep=time.sleep)`:

1. POST to `{base}/chat/completions` with `json={"model": model, "messages": messages, "temperature": 0}` and `timeout=60` using `client.post`.
2. On status 429 or ≥ 500, or an `httpx.TimeoutException`: if attempts remain, call `sleep(wait)` and retry. `wait` starts at 1 and doubles; if the response has a `Retry-After` header, use `float()` of it instead. After `retries` retries, raise `RuntimeError("model unavailable")`.
3. Any other error status: `raise_for_status()` (no retry).
4. Return `(content, usage)` from the JSON.

(`sleep` is a parameter so the check can run without really waiting.)

Replace `return "", {}` with:

1. `wait = 1.0`
2. `url = base + "/chat/completions"`
3. `payload = {"model": model, "messages": messages, "temperature": 0}`
4. `for attempt in range(retries + 1):`
5. `    try:`
6. `        r = client.post(url, timeout=60, json=payload)`
7. `    except httpx.TimeoutException:`
8. `        r = None`
9. `    if r is not None and r.status_code != 429 and r.status_code < 500:`
10. `        r.raise_for_status()`
11. `        data = r.json()`
12. `        content = data["choices"][0]["message"]["content"]`
13. `        return content, data.get("usage", {})`
14. `    if attempt == retries:`
15. `        break`
16. `    if r is not None and "Retry-After" in r.headers:`
17. `        delay = float(r.headers["Retry-After"])`
18. `    else:`
19. `        delay = wait`
20. `    sleep(delay)`
21. `    wait = wait * 2`
22. `raise RuntimeError("model unavailable")`

**Remember:** timeout always; retry only what a retry can fix; back off exponentially.

## Review

<details><summary>Why let the model say "I don't know"?</summary>Otherwise it invents an answer when retrieval didn't find the right chunk.</details>
