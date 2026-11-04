---
title: Rate limits: the token bucket
xp: 55
---
# Protect your wallet and your GPU

> **Warm-up:** someone's script calls your `/ask` endpoint 50 times per second. Each call costs you money. What should happen?

A **rate limit** caps how often each user (API key, IP) can call you. The standard algorithm is the **token bucket**:

- Each user has a bucket that holds up to `capacity` tokens (not LLM tokens; think of coins).
- The bucket refills at `rate` tokens per second, never above `capacity`.
- Each request takes 1 token. Empty bucket → reject with **429 Too Many Requests** and a `Retry-After` header.

It allows short **bursts** (up to `capacity` at once) but limits the average to `rate`. Model providers use the same idea on you, which is why AI engineer 2's client retries 429s with backoff.

Time is passed in as a function (`now`), so tests can use a fake clock instead of waiting.

## 🧮 Worked example

A bucket with `capacity = 3` and `rate = 1` token per second:

| time | tokens before | request? | tokens after |
|---|---|---|---|
| 0.0 s | 3 | yes, allowed | 2 |
| 0.0 s | 2 | yes, allowed | 1 |
| 0.0 s | 1 | yes, allowed | 0 |
| 0.0 s | 0 | **429**, rejected | 0 |
| 1.0 s | 0 + 1 s × 1 = 1 | yes, allowed | 0 |
| 5.0 s | 0 + 4 s × 1 = 4 → capped at **3** | yes, allowed | 2 |

A burst of 3 goes through at once; after that, about 1 request per second.

## Your quest

1. `TokenBucket(rate, capacity, now=time.monotonic)`: starts full. `allow()` first refills by `(now() − last) × rate` (capped at capacity), then takes a token and returns `True`, or returns `False` if fewer than 1 is left. `retry_after()` returns the seconds until 1 token is available (0 if one is).
2. `Limiter(rate, capacity, now)`: one bucket per key, created on first use. `check(key)` returns `(allowed, retry_after)`.

**Remember:** bursts up to capacity, average at rate, 429 with Retry-After.

## Review

<details><summary>Name the fields of a good request log line.</summary>request id, method, path, status and duration; for model calls also model, tokens and cost.</details>
