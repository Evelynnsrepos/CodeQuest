import math
b, rm = ns.get("batches"), ns.get("run_minutes")
assert b and rm, "Define batches and run_minutes."
assert b([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]], "Groups of 3, the last one shorter."
assert b([1, 2], 5) == [[1, 2]], "Fewer items than the size: one batch."
assert b([], 3) == [], "No items, no batches."
assert math.isclose(rm(600, 4, 2), 20), f"600 items, 4 s, 2 at once = 20 minutes, got {rm(600, 4, 2)!r}."
assert math.isclose(rm(601, 4, 2), 301 * 4 / 60), "601 items need 301 rounds (round up)."
assert math.isclose(rm(90, 2, 1), 3), "One at a time: 90 x 2 s = 3 minutes."
assert math.isclose(rm(10, 6, 4), 0.3), "ceil(10 / 4) = 3 rounds, x 6 s = 18 s = 0.3 minutes. Don't round the minutes."
