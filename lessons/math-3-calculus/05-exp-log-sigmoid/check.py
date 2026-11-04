import math
s, ds, dl, de = ns.get("sigmoid"), ns.get("d_sigmoid"), ns.get("d_ln"), ns.get("d_exp")
assert s and ds and dl and de, "Keep sigmoid, d_sigmoid, d_ln and d_exp."
num = lambda f, x: (f(x + 1e-5) - f(x - 1e-5)) / 2e-5
assert abs(s(0) - 0.5) < 1e-12, "sigmoid(0) = 0.5."
for x in (-3, 0, 0.7, 4):
    assert abs(ds(x) - num(s, x)) < 1e-6, f"d_sigmoid({x}) should match the slope of sigmoid, got {ds(x)!r}."
assert abs(ds(0) - 0.25) < 1e-12, "Slope of sigmoid at 0 is 0.25."
assert abs(dl(4) - 0.25) < 1e-12 and abs(dl(0.5) - 2) < 1e-12, "d_ln(x) = 1/x."
assert abs(de(1) - math.e) < 1e-12 and abs(de(0) - 1) < 1e-12, "d_exp(x) = e^x."
