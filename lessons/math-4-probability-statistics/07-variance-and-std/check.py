import math
va, sd, ds = ns.get("variance"), ns.get("std"), ns.get("data_std")
assert va and sd and ds, "Keep variance, std and data_std."
die = {k: 1 / 6 for k in range(1, 7)}
assert abs(va(die) - 35 / 12) < 1e-12, f"Die variance 35/12 ≈ 2.917, got {va(die)!r}."
assert abs(sd(die) - math.sqrt(35 / 12)) < 1e-12, "std = √variance."
assert va({5: 1.0}) == 0, "A sure thing has no spread."
assert abs(ds([69, 70, 71]) - math.sqrt(2 / 3)) < 1e-12, f"data_std([69, 70, 71]) ≈ 0.816, got {ds([69, 70, 71])!r}."
assert abs(ds([40, 70, 100]) - math.sqrt(600)) < 1e-9, "data_std([40, 70, 100]) ≈ 24.5."
assert abs(ds([2, 2, 4, 4]) - 1) < 1e-12, "Repeated values: [2, 2, 4, 4] has σ 1."
