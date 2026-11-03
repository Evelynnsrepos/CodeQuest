import math
lv, pr, rm = ns.get("levels"), ns.get("power_rules_hold"), ns.get("rms")
assert lv and pr and rm, "Keep levels, power_rules_hold and rms."
assert lv(4) == 16 and lv(8) == 256 and lv(1) == 2, f"levels(4) should be 2⁴ = 16, got {lv(4)!r}."
assert pr(2, 3, 2) is True and pr(1.5, 2, 3) is True, "The power rules are always true, so power_rules_hold should return True."
assert abs(rm([3, 4]) - math.sqrt(12.5)) < 1e-12, f"rms([3, 4]) = √((9 + 16) / 2) ≈ 3.536, got {rm([3, 4])!r}."
assert abs(rm([-2, 2]) - 2) < 1e-12, "rms([-2, 2]) is 2: squaring removes the sign."
