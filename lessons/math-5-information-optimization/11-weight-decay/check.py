import math
lp, lg, dc = ns.get("l2_penalty"), ns.get("l2_grad"), ns.get("decay")
assert lp and lg and dc, "Keep l2_penalty, l2_grad and decay."
assert abs(lp([3, -4], 0.1) - 1.25) < 1e-12, f"l2_penalty([3, -4], 0.1) = 1.25, got {lp([3, -4], 0.1)!r}."
g = lg([3, -4], 0.1)
assert all(abs(a - b) < 1e-12 for a, b in zip(g, [0.3, -0.4])), f"l2_grad = λw, got {g!r}."
h = 1e-6
num = (lp([3 + h, -4], 0.1) - lp([3 - h, -4], 0.1)) / (2 * h)
assert abs(num - 0.3) < 1e-6, "The gradient of your penalty should be λw (use λ/2)."
ws = [1.0, -2.0]
for _ in range(10000):
    ws = dc(ws, 0.001, 0.1)
assert abs(ws[0] - 0.9999 ** 10000) < 1e-9 and abs(ws[1] + 2 * 0.9999 ** 10000) < 1e-9, f"10,000 decay steps → ×0.368, got {ws!r}."
