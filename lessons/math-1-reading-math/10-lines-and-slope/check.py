sl, lt, pr = ns.get("slope"), ns.get("line_through"), ns.get("predict")
assert sl and lt and pr, "Keep slope, line_through and predict."
assert sl((1, 5), (2, 7)) == 2 and sl((2, 7), (1, 5)) == 2, f"slope((1, 5), (2, 7)) should be 2 (either order), got {sl((1, 5), (2, 7))!r}."
assert abs(sl((0, 2.5), (100, 1.5)) + 0.01) < 1e-12, "Falling line: slope −0.01."
m, b = lt((1, 5), (2, 7))
assert (m, b) == (2, 3), f"line_through((1,5), (2,7)) should be (2, 3), got {(m, b)!r}."
assert lt((0, 4), (2, 0)) == (-2, 4), "Through (0,4) and (2,0): m = −2, b = 4."
assert pr(2, 3, 10) == 23, "predict(2, 3, 10) = 2·10 + 3 = 23."
