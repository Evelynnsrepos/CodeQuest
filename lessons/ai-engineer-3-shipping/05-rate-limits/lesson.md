---
title: Rate limits: the token bucket
minutes: 50
xp: 55
hint: TokenBucket.__init__: store rate, capacity and now, then self.tokens = float(capacity) (starts full) and self.last = now()
hint: _refill: t = self.now(), self.tokens = min(self.capacity, self.tokens + (t - self.last) * self.rate), self.last = t
hint: allow: self._refill(), then if self.tokens >= 1: take one and return True, else return False
hint: retry_after: self._refill(), 0.0 if there's a token, else (1 - self.tokens) / self.rate
hint: Limiter.check: make a bucket for a new key, then if b.allow(): return True, 0.0, else return False, b.retry_after()
---
# Protect your wallet and your GPU

⏱️ About 50 minutes

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

**retry_after, in small steps**: 0.5 tokens left, rate 1 per second. You need 1 − 0.5 = **0.5** more tokens. At 1 token per second that takes 0.5 / 1 = **0.5 seconds**.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `now=time.monotonic` | | the clock function itself (no brackets), so a test can pass a fake clock |
| `self.now()` | | calls whichever clock was given and gets the time in seconds |
| `float(capacity)` | | 3 → 3.0: tokens can be fractions after a refill |
| `min(a, b)` | | the smaller of the two: here it caps the tokens at the capacity |
| `def _refill(self):` | | a helper method. The `_` at the start means "only used inside this class". |
| `self.buckets = {}` | | one bucket per key (per user, per IP address) |
| `TokenBucket(self.rate, self.capacity, self.now)` | | a new bucket with the limiter's settings |

## 🎯 Your quest

1. `TokenBucket(rate, capacity, now=time.monotonic)`: starts full. `allow()` first refills by `(now() − last) × rate` (capped at capacity), then takes a token and returns `True`, or returns `False` if fewer than 1 is left. `retry_after()` returns the seconds until 1 token is available (0 if one is).
2. `Limiter(rate, capacity, now)`: one bucket per key, created on first use. `check(key)` returns `(allowed, retry_after)`.

**Part 1:** `TokenBucket.__init__`. Replace `pass` with (8 spaces):

1. `self.rate = rate`
2. `self.capacity = capacity`
3. `self.now = now`
4. `self.tokens = float(capacity)`
5. `self.last = now()`

**Part 2:** the helper `_refill` (it's commented out under `__init__` in the starter; remove the `# `):

1. `def _refill(self):`
2. `    t = self.now()`
3. `    self.tokens = min(self.capacity, self.tokens + (t - self.last) * self.rate)`
4. `    self.last = t`

**Part 3:** `allow`. Replace `return True` with:

1. `self._refill()`
2. `if self.tokens >= 1:`
3. `    self.tokens = self.tokens - 1`
4. `    return True`
5. `return False`

`retry_after`: replace `return 0.0` with:

1. `self._refill()`
2. `if self.tokens >= 1:`
3. `    return 0.0`
4. `return (1 - self.tokens) / self.rate`

**Part 4:** `Limiter`. In `__init__`, replace `pass` with:

1. `self.rate = rate`
2. `self.capacity = capacity`
3. `self.now = now`
4. `self.buckets = {}`

In `check`, replace `return True, 0.0` with:

1. `if key not in self.buckets:`
2. `    self.buckets[key] = TokenBucket(self.rate, self.capacity, self.now)`
3. `b = self.buckets[key]`
4. `if b.allow():`
5. `    return True, 0.0`
6. `return False, b.retry_after()`

**Remember:** bursts up to capacity, average at rate, 429 with Retry-After.

## Review

<details><summary>Name the fields of a good request log line.</summary>request id, method, path, status and duration; for model calls also model, tokens and cost.</details>
