sc, kv, be = ns.get("ssm_scan"), ns.get("kv_numbers"), ns.get("break_even_tokens")
assert sc and kv and be, "Keep ssm_scan, kv_numbers and break_even_tokens."
r = sc([1, 0, 0, 1], 0.5, 1, 2)
assert len(r) == 4 and all(abs(u - v) < 1e-12 for u, v in zip(r, [2, 1, 0.5, 2.25])), f"ssm_scan should give [2, 1, 0.5, 2.25], got {r!r}."
assert sc([], 0.5, 1, 1) == [], "No input, no output."
assert all(abs(u - v) < 1e-12 for u, v in zip(sc([3, 4], 0, 1, 1), [3, 4])), "a = 0 forgets everything."
assert kv(32768, 8, 128) == 67108864, "2 · 8 · 128 · 32768."
assert be(8192, 16, 8, 128) == 64, f"Break-even at 64 tokens, got {be(8192, 16, 8, 128)!r}."
assert be(1000, 3, 2, 64) == 12, "Round up: 3000 / 256 = 11.7 → 12."
