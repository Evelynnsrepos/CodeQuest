import hashlib, json
ck, TC, cc = ns.get("cache_key"), ns.get("TTLCache"), ns.get("cached_call")
assert ck and TC and cc, "Keep cache_key, TTLCache and cached_call."
m = [{"role": "user", "content": "hi"}]
want = hashlib.sha256(json.dumps({"model": "a", "messages": m, "temperature": 0}, sort_keys=True).encode()).hexdigest()
assert ck("a", m, 0) == want, "cache_key: sha256 hex of the sorted JSON."
assert ck("a", m, 0) != ck("b", m, 0) and ck("a", m, 0) != ck("a", m, 0.5), "Model and temperature are part of the key."
t = [0.0]
c = TC(ttl=10, max_items=2, now=lambda: t[0])
assert c.get("x") is None
c.put("x", 1); t[0] = 5
assert c.get("x") == 1, "Fresh entries are returned."
t[0] = 10.5
assert c.get("x") is None and "x" not in getattr(c, "data", {}), "Expired entries count as missing."
assert abs(c.hit_rate() - 1 / 3) < 1e-9, f"1 hit of 3 lookups, got {c.hit_rate()!r}."
c.put("a", 1); t[0] = 11; c.put("b", 2); t[0] = 12; c.put("c", 3)
assert c.get("a") is None and c.get("b") == 2 and c.get("c") == 3, "When full, drop the oldest entry."
calls = []
llm = lambda msgs: calls.append(1) or len(calls)
cache = TC(ttl=100, max_items=10)
assert [cc(cache, llm, "s", m, 0) for _ in range(3)] == [1, 1, 1] and len(calls) == 1, "temperature 0: one model call, then cached."
assert [cc(cache, llm, "s", m, 0.7) for _ in range(2)] == [2, 3], "temperature > 0: never cached."
