s, c, m = ns.get("solve"), ns.get("check"), ns.get("max_tokens")
assert s and c and m, "Keep solve, check and max_tokens."
assert s(2, 1, 9) == 4, f"2x + 1 = 9 gives x = 4, got {s(2, 1, 9)!r}."
assert s(5, -3, 7) == 2, "5x − 3 = 7 gives x = 2."
assert abs(s(4, 0, 1) - 0.25) < 1e-12, "4x = 1 gives x = 0.25."
assert c(2, 1, 9, 4) is True and c(2, 1, 9, 5) is False, "check: is a·x + b equal to c?"
assert abs(m(12, 5, 0.0002) - 35000) < 1e-6, f"(12 − 5) / 0.0002 = 35,000 tokens, got {m(12, 5, 0.0002)!r}."
