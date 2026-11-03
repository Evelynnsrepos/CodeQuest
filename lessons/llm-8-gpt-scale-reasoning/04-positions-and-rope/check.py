import math
sn, rp, dot = ns.get("sinusoidal"), ns.get("rope"), ns["dot"]
assert sn and rp, "Keep sinusoidal and rope."
pe = sn(3, 4)
want = [math.sin(3), math.cos(3), math.sin(3 / 100), math.cos(3 / 100)]
assert len(pe) == 4 and all(abs(a - b) < 1e-9 for a, b in zip(pe, want)), f"sinusoidal(3, 4) should be {want!r}, got {pe!r}."
assert all(abs(a - b) < 1e-12 for a, b in zip(sn(0, 6), [0, 1, 0, 1, 0, 1])), "Position 0 should be [0, 1, 0, 1, ...]."
x = [1.0, 2.0, 3.0, 4.0]
assert all(abs(a - b) < 1e-12 for a, b in zip(rp(x, 0), x)), "rope at position 0 should not change the vector."
r = rp(x, 2)
a0, a1 = 2.0, 2.0 / 100
want = [1 * math.cos(a0) - 2 * math.sin(a0), 1 * math.sin(a0) + 2 * math.cos(a0), 3 * math.cos(a1) - 4 * math.sin(a1), 3 * math.sin(a1) + 4 * math.cos(a1)]
assert all(abs(a - b) < 1e-9 for a, b in zip(r, want)), f"rope(x, 2) should be {want!r}, got {r!r}."
assert abs(sum(v * v for v in r) - 30) < 1e-9, "A rotation must keep the vector's length."
q, k = [0.3, -1.0, 2.0, 0.5, 1.0, 1.0], [1.0, 0.2, -0.5, 1.5, 0.0, 2.0]
s1, s2 = dot(rp(q, 7), rp(k, 4)), dot(rp(q, 40), rp(k, 37))
assert abs(s1 - s2) < 1e-9, "q·k after RoPE should depend only on the distance between positions."
