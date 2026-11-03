import math
add, scale, dot, norm, rms = (ns.get(n) for n in ("add", "scale", "dot", "norm", "rms_norm"))
assert all((add, scale, dot, norm, rms)), "Keep add, scale, dot, norm and rms_norm."
assert add([1, 2, 3], [10, 20, 30]) == [11, 22, 33], f"add returned {add([1, 2, 3], [10, 20, 30])!r}."
assert scale(-2, [1, 0.5]) == [-2, -1.0], f"scale(-2, [1, 0.5]) returned {scale(-2, [1, 0.5])!r}."
assert dot([1, 2], [3, -1]) == 1, f"dot([1, 2], [3, -1]) returned {dot([1, 2], [3, -1])!r}, expected 1."
assert abs(norm([6, 8]) - 10) < 1e-9, f"norm([6, 8]) returned {norm([6, 8])!r}, expected 10."
r = rms([1, 1, 1, 5])
want = [x / 2.6457513110645907 for x in [1, 1, 1, 5]]
assert all(abs(x - y) < 1e-9 for x, y in zip(r, want)) and len(r) == 4, f"rms_norm([1, 1, 1, 5]) returned {r!r}, expected each entry divided by √7 ≈ 2.646."
assert abs(math.sqrt(sum(x * x for x in r) / 4) - 1) < 1e-9, "After rms_norm, the root mean square should be 1."
