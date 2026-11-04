we, sg = ns.get("welch"), ns.get("significant")
assert we and sg, "Keep welch and significant."
A, B = [72, 75, 70, 74, 69], [68, 70, 66, 71, 65]
t, df = we(A, B)
assert abs(t - 2.4807) < 1e-3 and abs(df - 8) < 1e-9, f"t ≈ 2.48 with 8 degrees of freedom, got {(t, df)!r}."
assert sg(A, B) is True and sg(B, A) is True, "2.48 > 2.306, in either order (use |t|)."
assert sg([72, 74, 70, 73], [71, 72, 69, 70]) is False, "A 1.75-point gap with 4 runs each isn't significant."
a2, b2 = [0.71, 0.74, 0.69, 0.73, 0.72, 0.70], [0.68, 0.70, 0.69, 0.67, 0.71, 0.66]
t2, df2 = we(a2, b2)
assert abs(t2 - 2.7775) < 1e-3 and abs(df2 - 10) < 1e-6 and sg(a2, b2), "Second example: t ≈ 2.78, df = 10, t* = 2.228."
