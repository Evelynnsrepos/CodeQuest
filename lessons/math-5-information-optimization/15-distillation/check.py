st, dl = ns.get("soft_targets"), ns.get("distill_loss")
assert st and dl, "Keep soft_targets and distill_loss."
r = st([4, 1, 0], 1)
assert all(abs(a - b) < 1e-9 for a, b in zip(r, [0.9362395519, 0.0466126226, 0.0171478255])), f"T = 1: (0.936, 0.047, 0.017), got {r!r}."
r = st([4, 1, 0], 4)
assert all(abs(a - b) < 1e-9 for a, b in zip(r, [0.5434056117, 0.2566866355, 0.1999077528])), f"T = 4: (0.543, 0.257, 0.200), got {r!r}."
assert abs(sum(st([1000, 999], 1)) - 1) < 1e-12, "Shift by the max: no overflow."
assert abs(dl([4, 1, 0], [4, 1, 0], 3)) < 1e-12, "Student = teacher: loss 0."
zt, zs, T = [4, 1, 0], [2, 1, 1], 4
pt, ps = st(zt, T), st(zs, T)
for i in range(3):
    up, dn = list(zs), list(zs)
    up[i] += 1e-6
    dn[i] -= 1e-6
    num = (dl(zt, up, T) - dl(zt, dn, T)) / 2e-6
    assert abs(num - T * (ps[i] - pt[i])) < 1e-5, f"Gradient for student logit {i} should be T·(p_S − p_T): did you multiply by T²? got {num}."
