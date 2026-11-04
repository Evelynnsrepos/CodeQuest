import torch
d, mg = ns.get("derivative"), ns.get("mse_grads")
assert d and mg, "Keep derivative and mse_grads."
assert abs(d(lambda t: t ** 3, 2.0) - 12) < 1e-5, "d/dx x³ at 2 = 3·4 = 12."
assert abs(d(torch.sigmoid, 0.0) - 0.25) < 1e-6, "sigmoid′(0) = 0.25."
assert abs(d(lambda t: torch.exp(2 * t), 0.0) - 2) < 1e-5, "d/dx e^(2x) at 0 = 2 (chain rule)."
gw, gb = mg(1.0, 0.0, [1, 2, 3], [2, 4, 6])
assert abs(gw + 28 / 3) < 1e-4 and abs(gb + 4) < 1e-4, f"mse_grads(1, 0, ...) = (−9.333, −4.0), got {(gw, gb)!r}."
gw, gb = mg(2.0, 0.0, [1, 2, 3], [2, 4, 6])
assert abs(gw) < 1e-6 and abs(gb) < 1e-6, "At the perfect fit the gradients are 0."
