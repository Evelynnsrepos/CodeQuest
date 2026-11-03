d, n, r = ns.get("dot"), ns.get("neuron"), ns.get("relation")
assert d and n and r, "Keep dot, neuron and relation."
assert d([2, 5, 1], [3, 1, 4]) == 15, f"dot([2,5,1], [3,1,4]) should be 15, got {d([2, 5, 1], [3, 1, 4])!r}."
try:
    d([1, 2], [1, 2, 3])
except ValueError:
    pass
else:
    raise AssertionError("dot should raise ValueError when the lengths differ (zip would silently cut it short).")
assert abs(n([0.5, -1], [4, 1], 0.2) - 1.2) < 1e-12, f"neuron([0.5, -1], [4, 1], 0.2) = 2 − 1 + 0.2 = 1.2, got {n([0.5, -1], [4, 1], 0.2)!r}."
assert r([1, 2], [3, 4]) == "same direction" and r([1, 2], [2, -1]) == "perpendicular" and r([1, 0], [-2, 1]) == "opposite", "relation follows the sign of the dot product."
