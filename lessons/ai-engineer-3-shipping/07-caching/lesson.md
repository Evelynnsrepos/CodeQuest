---
title: Caching answers
minutes: 50
xp: 50
hint: cache_key: raw = json.dumps({...}, sort_keys=True), then return hashlib.sha256(raw.encode()).hexdigest()
hint: get: item = self.data.get(key). If item is not None and self.now() - item[0] < self.ttl: count a hit and return item[1]
hint: get, otherwise: self.data.pop(key, None), count a miss, return None
hint: put: when full and the key is new, find the key with the smallest stored time (best-so-far) and del it. Then self.data[key] = (self.now(), value)
hint: cached_call: if temperature != 0: return llm(messages). Else get from the cache, and on a miss call llm and put the answer
---
# Don't pay twice for the same answer

⏱️ About 50 minutes

> **Warm-up:** 30% of your users ask "how do I reset my password?". How many times should the model answer it?

A **response cache** stores answers by a **key** made from everything that affects the answer: model, messages, temperature. Same key → return the stored answer instantly, for free.

- The key is a **hash** (`sha256`) of a canonical JSON dump (`sort_keys=True`, so key order in dicts doesn't matter).
- Entries **expire** after a time-to-live (**TTL**), because documents and models change.
- Only cache **deterministic** calls (temperature 0). Caching a creative answer at temperature 1 freezes the randomness.
- A cache has a **size limit**; when full, drop the oldest entry.

This is different from the provider's **prompt cache** (LLMs 9 lesson 02), which only makes repeated *prompt prefixes* cheaper; a response cache skips the call entirely.

Measure the **hit rate** (hits ÷ lookups) to see if it's worth it.

## 🧮 Worked example

Two requests with the same settings in a different order must give the same key:

```python
import hashlib, json
a = {"model": "llama3.2", "temperature": 0}
b = {"temperature": 0, "model": "llama3.2"}

def key(r):
    return hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest()

print(key(a) == key(b))   # True: sort_keys puts both in the same order first
```

**Hit rate:** 100 lookups, 30 found in the cache → 30 ÷ 100 = **30%** of model calls saved.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `json.dumps(d, sort_keys=True)` | | the dictionary as text, keys in alphabetical order, so the same request always gives the same text |
| `raw.encode()` | | text → bytes, which `sha256` needs |
| `hashlib.sha256(...).hexdigest()` | | a 64-character fingerprint of the text. Same text, same fingerprint; any change gives a totally different one. |
| `self.data[key] = (self.now(), value)` | | stores a pair: when it was saved, and the value |
| `item[0]`, `item[1]` | | the saved time, the value |
| `self.now() - item[0] < self.ttl` | | younger than the time-to-live? Then it's still fresh. |
| `self.data.pop(key, None)` | | removes the entry if it's there (no error if not) |
| `del self.data[oldest]` | | removes that entry |

### 👀 Worked example: a cache with room for 2

`ttl` = 10 seconds. At t = 0 put "a", at t = 1 put "b", at t = 2 put "c":

1. "c" is new and the cache is full (2 items) → find the oldest: "a" (time 0) → delete it.
2. Store "c" at time 2. The cache holds "b" and "c".
3. At t = 15, `get("b")`: 15 − 1 = 14, not < 10 → expired → removed, counted as a miss, `None`.

## 🎯 Your quest

1. `cache_key(model, messages, temperature)`: the hex `sha256` of `json.dumps({"model": ..., "messages": ..., "temperature": ...}, sort_keys=True)`.
2. `TTLCache(ttl, max_items, now=time.monotonic)`: `get(key)` returns the value or `None` (expired entries count as missing and are removed); `put(key, value)` stores it with the current time, dropping the **oldest** entry when full; `hit_rate()` = hits ÷ (hits + misses), 0 if no lookups.
3. `cached_call(cache, llm, model, messages, temperature)`: only when `temperature == 0`, use the cache; otherwise always call `llm(messages)`.

**Part 1:** `cache_key`. Replace `return ""` with:

1. `raw = json.dumps({"model": model, "messages": messages, "temperature": temperature}, sort_keys=True)`
2. `return hashlib.sha256(raw.encode()).hexdigest()`

**Part 2:** `TTLCache` (8 spaces, inside the class). `__init__`: replace `pass` with:

1. `self.ttl = ttl`
2. `self.max_items = max_items`
3. `self.now = now`
4. `self.data = {}`
5. `self.hits = 0`
6. `self.misses = 0`

`get`: replace `return None` with:

1. `item = self.data.get(key)`
2. `if item is not None and self.now() - item[0] < self.ttl:`
3. `    self.hits = self.hits + 1`
4. `    return item[1]`
5. `self.data.pop(key, None)`
6. `self.misses = self.misses + 1`
7. `return None`

`put`: replace `pass` with:

1. `if key not in self.data and len(self.data) >= self.max_items:`
2. `    oldest = None`
3. `    for k in self.data:`
4. `        if oldest is None or self.data[k][0] < self.data[oldest][0]:`
5. `            oldest = k`
6. `    del self.data[oldest]`
7. `self.data[key] = (self.now(), value)`

`hit_rate`: replace `return 0.0` with:

1. `total = self.hits + self.misses`
2. `if total == 0:`
3. `    return 0.0`
4. `return self.hits / total`

**Part 3:** `cached_call`. Replace `return llm(messages)` with:

1. `if temperature != 0:`
2. `    return llm(messages)`
3. `key = cache_key(model, messages, temperature)`
4. `value = cache.get(key)`
5. `if value is None:`
6. `    value = llm(messages)`
7. `    cache.put(key, value)`
8. `return value`

**Remember:** key on everything that matters, expire, measure the hit rate.

## Review

<details><summary>Why watch p95 latency instead of the average?</summary>The average hides the slow tail that makes some users leave.</details>
