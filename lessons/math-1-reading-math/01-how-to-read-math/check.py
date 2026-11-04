import math
f, av, ar = ns.get("f"), ns.get("average"), ns.get("area")
assert f and av and ar, "Keep f, average and area."
assert f(4) == 14 and f(0) == 2, f"f(4) should be 3·4 + 2 = 14, got {f(4)!r}."
assert av(3, 8) == 5.5, f"average(3, 8) should be (3 + 8) / 2 = 5.5, got {av(3, 8)!r}."
assert abs(ar(2) - 4 * math.pi) < 1e-12, f"area(2) should be π·2² ≈ 12.566, got {ar(2)!r}."
