tk, tl, rc = ns.get("tokens"), ns.get("tokens_left"), ns.get("request_cost")
assert tk and tl and rc, "Keep tokens, tokens_left and request_cost."
assert tk("abcd" * 10) == 10 and tk("abc") == 0, "tokens = len(text) // 4."
assert tl(200000, [3000, 12000, 2000, 150000], 20000) == 13000, f"Should be 13,000 left, got {tl(200000, [3000, 12000, 2000, 150000], 20000)!r}."
assert tl(8192, [8000], 500) < 0, "Over budget gives a negative number."
assert abs(rc(160000, 2000, 3) - 0.054) < 1e-12, f"Cached request ≈ 0.054 $, got {rc(160000, 2000, 3)!r}."
assert abs(rc(0, 162000, 3) - 0.486) < 1e-12, "No cache: 0.486 $."
assert abs(rc(1000000, 0, 3, cache_factor=0.25) - 0.75) < 1e-12, "cache_factor is a parameter."
