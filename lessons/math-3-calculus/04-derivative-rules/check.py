ev, dv = ns.get("evaluate"), ns.get("derive")
assert ev and dv, "Keep evaluate and derive."
assert ev([7, 5, 3], 2) == 29, f"7 + 5·2 + 3·4 = 29, got {ev([7, 5, 3], 2)!r}."
assert ev([], 4) == 0, "An empty polynomial is 0."
assert dv([7, 5, 3]) == [5, 6], f"derive([7, 5, 3]) should be [5, 6], got {dv([7, 5, 3])!r}."
assert dv([0, 0, 0, 1]) == [0, 0, 3], "x³ → 3x²."
assert ev(dv([7]), 5) == 0, "A constant has slope 0."
p = [1, -2, 0, 4]
h = 1e-5
num = (ev(p, 1.5 + h) - ev(p, 1.5 - h)) / (2 * h)
assert abs(ev(dv(p), 1.5) - num) < 1e-5, "Your derivative should match the central difference."
