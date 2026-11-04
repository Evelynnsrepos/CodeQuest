kv, tot, mc = ns.get("kv_cache_gb"), ns.get("total_vram_gb"), ns.get("max_context")
assert kv and tot and mc, "Keep the functions kv_cache_gb, total_vram_gb and max_context."
got = kv(32, 8, 128, 8192, 2)
assert abs(got - 1.073741824) < 1e-9, f"kv_cache_gb(32, 8, 128, 8192, 2) returned {got!r}, expected about 1.074."
got = kv(10, 2, 64, 1000, 1)
assert abs(got - 0.00256) < 1e-12, f"kv_cache_gb(10, 2, 64, 1000, 1) returned {got!r}, expected 0.00256 (2 × 10 × 2 × 64 × 1 × 1000 bytes)."
got = tot(5.0, 2.0)
assert abs(got - 8.0) < 1e-9, f"total_vram_gb(5.0, 2.0) returned {got!r}, expected 8.0 (including 1 GB overhead)."
got = mc(4.9, 32, 8, 128, 11.0)
assert got == 37888, f"max_context(4.9, 32, 8, 128, 11.0) returned {got!r}, expected 37888."
got = mc(9.5, 32, 8, 128, 10.0)
assert got == 0, f"max_context(9.5, 32, 8, 128, 10.0) returned {got!r}, expected 0: not even 1,024 tokens fit."
