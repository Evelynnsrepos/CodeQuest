l, f, p = ns.get("left"), ns.get("fits"), ns.get("per_program")
assert l and f and p, "Keep left, fits and per_program."
assert l(12, 5) == 7 and l(12, 12) == 0, f"left(12, 5) should be 7, got {l(12, 5)!r}."
assert f(5, 12) is True and f(12, 12) is True and f(16, 12) is False, "fits: model ≤ total (equal counts as fitting)."
assert p(12, 3) == 4 and p(7, 2) == 3.5, f"per_program(7, 2) should be 3.5, got {p(7, 2)!r}."
