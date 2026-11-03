import math
lb, bn, lp = ns.get("log_base"), ns.get("bits_needed"), ns.get("log_prob")
assert lb and bn and lp, "Keep log_base, bits_needed and log_prob."
assert abs(lb(8, 2) - 3) < 1e-9 and abs(lb(1000, 10) - 3) < 1e-9, f"log_base(8, 2) should be 3, got {lb(8, 2)!r}."
assert abs(lb(1, 7)) < 1e-12, "log of 1 is 0 in any base."
assert bn(128000) == 17 and bn(256) == 8 and bn(257) == 9, f"bits_needed(128000) should be 17, got {bn(128000)!r}."
assert abs(lp([0.1, 0.05, 0.2]) - math.log(0.001)) < 1e-12, "log_prob should be the sum of the natural logs (equal to ln of the product)."
assert lp([1.0]) == 0, "A token with probability 1 adds nothing."
