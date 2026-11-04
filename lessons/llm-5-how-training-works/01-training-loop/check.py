L, G, T = ns.get("loss"), ns.get("gradients"), ns.get("train")
assert L and G and T, "Keep loss, gradients and train."
d = [(1.0, 2.0), (2.0, 3.0)]
assert abs(L(1.0, 0.0, d) - 1.0) < 1e-9, f"loss(1, 0, [(1, 2), (2, 3)]) returned {L(1.0, 0.0, d)!r}, expected 1.0 (errors −1 and −1)."
dw, db = G(1.0, 0.0, d)
assert abs(dw - (-3.0)) < 1e-9 and abs(db - (-2.0)) < 1e-9, f"gradients(1, 0, ...) returned {(dw, db)!r}, expected (−3.0, −2.0): average of 2·e·x and 2·e."
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    w, b = T([(0.0, 1.0), (1.0, 3.0), (2.0, 5.0)], 0.05, 2000)
assert abs(w - 2) < 0.01 and abs(b - 1) < 0.01, f"train on y = 2x + 1 ended at w={w:.3f}, b={b:.3f}. Apply w -= lr·dw and b -= lr·db every step."
