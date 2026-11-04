fw, bw = ns.get("forward"), ns.get("backward")
assert fw and bw, "Keep forward and backward."
z, a, L = fw(0.5, 0, 2, 1)
assert abs(z - 1) < 1e-12 and abs(a - 0.7310585786) < 1e-9 and abs(L - 0.0723294881) < 1e-9, f"forward(0.5, 0, 2, 1) should be (1, 0.7311, 0.0723), got {(z, a, L)!r}."
dw, db = bw(0.5, 0, 2, 1)
assert abs(dw + 0.2115083711) < 1e-9 and abs(db + 0.1057541856) < 1e-9, f"backward(0.5, 0, 2, 1) should be (-0.2115, -0.1058), got {(dw, db)!r}."
for w, b, x, y in [(-1.2, 0.4, 0.7, 0), (2, -3, 1.5, 1)]:
    h = 1e-6
    nw = (fw(w + h, b, x, y)[2] - fw(w - h, b, x, y)[2]) / (2 * h)
    nb = (fw(w, b + h, x, y)[2] - fw(w, b - h, x, y)[2]) / (2 * h)
    gw, gb = bw(w, b, x, y)
    assert abs(gw - nw) < 1e-6 and abs(gb - nb) < 1e-6, f"Gradient check failed at {(w, b, x, y)}: yours {(gw, gb)}, numeric {(nw, nb)}."
