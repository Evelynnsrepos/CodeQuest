TB, L = ns.get("TokenBucket"), ns.get("Limiter")
assert TB and L, "Keep TokenBucket and Limiter."
t = [0.0]
b = TB(rate=1, capacity=3, now=lambda: t[0])
assert [b.allow() for _ in range(5)] == [True, True, True, False, False], "Starts full: 3 allowed, then empty."
assert abs(b.retry_after() - 1.0) < 1e-9, "Empty at rate 1/s: retry after 1 second."
t[0] = 0.5
assert not b.allow() and abs(b.retry_after() - 0.5) < 1e-9, "Half a token after 0.5 s: wait 0.5 more."
t[0] = 2.0
assert [b.allow(), b.allow(), b.allow()] == [True, True, False], "0.5 tokens at t = 0.5, plus 1.5 s × 1/s = 2 tokens at t = 2: two allowed."
t[0] = 100.0
assert [b.allow() for _ in range(4)] == [True, True, True, False], "Refill never goes above capacity."
t = [0.0]
lim = L(rate=2, capacity=1, now=lambda: t[0])
assert lim.check("ada") == (True, 0.0) and lim.check("ada")[0] is False and lim.check("linus")[0] is True, "One bucket per key."
ok, wait = lim.check("ada")
assert not ok and abs(wait - 0.5) < 1e-9, f"rate 2/s: wait 0.5 s for the next token, got {wait!r}."
