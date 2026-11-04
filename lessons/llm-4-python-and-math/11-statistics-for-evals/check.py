import math
m, s, c, cb = ns.get("mean"), ns.get("std"), ns.get("ci95"), ns.get("clearly_better")
assert m and s and c and cb, "Keep mean, std, ci95 and clearly_better."
assert m([2, 4, 9]) == 5, f"mean([2, 4, 9]) returned {m([2, 4, 9])!r}, expected 5."
assert abs(s([2, 4, 4, 4, 5, 5, 7, 9]) - 2.138089935299395) < 1e-9, f"std([2, 4, 4, 4, 5, 5, 7, 9]) returned {s([2, 4, 4, 4, 5, 5, 7, 9])!r}, expected about 2.138 (divide by n − 1)."
lo, hi = c([1, 0, 1, 1])
se = s([1, 0, 1, 1]) / 2
assert abs(lo - (0.75 - 1.96 * se)) < 1e-9 and abs(hi - (0.75 + 1.96 * se)) < 1e-9, f"ci95([1, 0, 1, 1]) returned {(lo, hi)!r}, expected 0.75 ± 1.96 × SE."
assert cb([1] * 13 + [0] * 7) is False, "13 of 20 is not clearly better: the interval includes 0.5."
assert cb([1] * 130 + [0] * 70) is True, "130 of 200: the whole interval is above 0.5."
