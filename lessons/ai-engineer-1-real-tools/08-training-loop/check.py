import torch
fl = ns.get("fit_line")
assert fl, "Keep fit_line."
g = torch.Generator().manual_seed(1)
xs = torch.linspace(-2, 2, 50)
ys = 2 * xs + 1 + 0.1 * torch.randn(50, generator=g)
w, b, loss = fl(xs.tolist(), ys.tolist())
assert abs(w - 2) < 0.05 and abs(b - 1) < 0.05, f"Expected w ≈ 2 and b ≈ 1, got w={w:.3f}, b={b:.3f}."
assert loss < 0.02, f"The final loss should be about the noise level (0.01), got {loss:.4f}."
w2, b2, _ = fl(xs.tolist(), (-3 * xs + 0.5).tolist(), steps=800)
assert abs(w2 + 3) < 0.01 and abs(b2 - 0.5) < 0.01, "It should fit any line, e.g. y = −3x + 0.5."
