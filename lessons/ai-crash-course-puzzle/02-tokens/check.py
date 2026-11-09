et, co = ns.get("estimate_tokens"), ns.get("cost")
assert et and co, "Keep estimate_tokens and cost."
assert et("unbelievable") == 3 and et("hello") == 2 and et("") == 0, f"estimate_tokens: characters ÷ 4, rounded up. 'hello' (5 characters) should give 2, yours gave {et('hello')!r}."
assert abs(co(20_000, 1_000, 3, 15) - 0.075) < 1e-12, f"20,000 × 3 ÷ 1,000,000 + 1,000 × 15 ÷ 1,000,000 = 0.075 dollars, yours gave {co(20_000, 1_000, 3, 15)!r}."
assert abs(co(1_000_000, 0, 0.5, 2) - 0.5) < 1e-12 and abs(co(0, 2_000_000, 1, 4) - 8) < 1e-12, "Use in_price for input tokens and out_price for output tokens, both per million."
