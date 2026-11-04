---
title: Caching answers
xp: 50
---
# Don't pay twice for the same answer

> **Warm-up:** 30% of your users ask "how do I reset my password?". How many times should the model answer it?

A **response cache** stores answers by a **key** made from everything that affects the answer: model, messages, temperature. Same key → return the stored answer instantly, for free.

- The key is a **hash** (`sha256`) of a canonical JSON dump (`sort_keys=True`, so key order in dicts doesn't matter).
- Entries **expire** after a time-to-live (**TTL**), because documents and models change.
- Only cache **deterministic** calls (temperature 0). Caching a creative answer at temperature 1 freezes the randomness.
- A cache has a **size limit**; when full, drop the oldest entry.

This is different from the provider's **prompt cache** (LLMs 9 lesson 02), which only makes repeated *prompt prefixes* cheaper; a response cache skips the call entirely.

Measure the **hit rate** (hits ÷ lookups) to see if it's worth it.

## Your quest

1. `cache_key(model, messages, temperature)`: the hex `sha256` of `json.dumps({"model": ..., "messages": ..., "temperature": ...}, sort_keys=True)`.
2. `TTLCache(ttl, max_items, now=time.monotonic)`: `get(key)` returns the value or `None` (expired entries count as missing and are removed); `put(key, value)` stores it with the current time, dropping the **oldest** entry when full; `hit_rate()` = hits ÷ (hits + misses), 0 if no lookups.
3. `cached_call(cache, llm, model, messages, temperature)`: only when `temperature == 0`, use the cache; otherwise always call `llm(messages)`.

**Remember:** key on everything that matters, expire, measure the hit rate.

## Review

<details><summary>Why watch p95 latency instead of the average?</summary>The average hides the slow tail that makes some users leave.</details>
