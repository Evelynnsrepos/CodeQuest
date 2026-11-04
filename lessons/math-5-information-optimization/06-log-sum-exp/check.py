import math
ls, lsm, sm = ns.get("logsumexp"), ns.get("log_softmax"), ns.get("softmax")
assert ls and lsm and sm, "Keep logsumexp, log_softmax and softmax."
assert abs(ls([1, 2, 3]) - math.log(math.e + math.e ** 2 + math.e ** 3)) < 1e-12, "logsumexp([1, 2, 3]) wrong."
try:
    v = ls([1000, 1000])
except OverflowError:
    raise AssertionError("logsumexp([1000, 1000]) overflowed: subtract the max first.")
assert abs(v - (1000 + math.log(2))) < 1e-9, f"logsumexp([1000, 1000]) = 1000.693, got {v!r}."
r = lsm([1000, 0])
assert abs(r[0]) < 1e-12 and abs(r[1] + 1000) < 1e-9, f"log_softmax([1000, 0]) ≈ [0, −1000], got {r!r}."
r = sm([1000, 1000])
assert all(abs(x - 0.5) < 1e-12 for x in r), f"softmax([1000, 1000]) = [0.5, 0.5], got {r!r}."
r = sm([2, 1, 0])
assert abs(sum(r) - 1) < 1e-12 and abs(r[0] - 0.6652409558) < 1e-9, "softmax([2, 1, 0]) ≈ [0.665, 0.245, 0.090]."
