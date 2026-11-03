import math
nm, nz, ds, cl = ns.get("norm"), ns.get("normalize"), ns.get("distance"), ns.get("clip")
assert nm and nz and ds and cl, "Keep norm, normalize, distance and clip."
assert nm([3, 4]) == 5 and abs(nm([1, 1, 1, 1]) - 2) < 1e-12, f"norm([3, 4]) should be 5, got {nm([3, 4])!r}."
u = nz([3, 4])
assert all(abs(a - b) < 1e-12 for a, b in zip(u, [0.6, 0.8])), f"normalize([3, 4]) should be [0.6, 0.8], got {u!r}."
try:
    nz([0, 0])
except ValueError:
    pass
else:
    raise AssertionError("normalize([0, 0]) should raise ValueError.")
assert ds([1, 1], [4, 5]) == 5, f"distance([1,1], [4,5]) should be 5, got {ds([1, 1], [4, 5])!r}."
c = cl([30, 40], 1.0)
assert all(abs(a - b) < 1e-12 for a, b in zip(c, [0.6, 0.8])), f"clip([30, 40], 1.0) should be [0.6, 0.8], got {c!r}."
assert cl([0.1, 0.2], 1.0) == [0.1, 0.2], "A gradient shorter than max_norm stays unchanged."
