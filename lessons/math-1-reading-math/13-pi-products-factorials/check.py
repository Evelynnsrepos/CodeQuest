import math
pr, fa, ch = ns.get("product"), ns.get("factorial"), ns.get("choose")
assert pr and fa and ch, "Keep product, factorial and choose."
assert abs(pr([0.1, 0.05, 0.2]) - 0.001) < 1e-15, f"product([0.1, 0.05, 0.2]) should be 0.001, got {pr([0.1, 0.05, 0.2])!r}."
assert pr([]) == 1, "The product of nothing is 1 (start the total at 1)."
assert fa(5) == 120 and fa(0) == 1 and fa(1) == 1, f"factorial(5) = 120 and factorial(0) = 1, got {fa(5)!r} and {fa(0)!r}."
assert ch(4, 2) == 6 and ch(10, 3) == 120 and ch(5, 0) == 1, f"choose(4, 2) should be 6, got {ch(4, 2)!r}."
assert ch(20, 10) == math.comb(20, 10), "choose(20, 10) is wrong."
