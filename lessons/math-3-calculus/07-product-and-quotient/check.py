import math
dp, dq = ns.get("d_product"), ns.get("d_quotient")
assert dp and dq, "Keep d_product and d_quotient."
assert dp(4, 4, 3, 1) == 16, f"x²(x + 1) at 2: 4·3 + 4·1 = 16, got {dp(4, 4, 3, 1)!r}."
assert abs(dq(4, 4, 3, 1) - 8 / 9) < 1e-12, f"x²/(x + 1) at 2: 8/9, got {dq(4, 4, 3, 1)!r}."
x = 0.7
num = (math.sin(x + 1e-5) * math.exp(x + 1e-5) - math.sin(x - 1e-5) * math.exp(x - 1e-5)) / 2e-5
assert abs(dp(math.sin(x), math.cos(x), math.exp(x), math.exp(x)) - num) < 1e-6, "sin·exp check failed."
num = (math.sin(x + 1e-5) / (x + 1e-5) - math.sin(x - 1e-5) / (x - 1e-5)) / 2e-5
assert abs(dq(math.sin(x), math.cos(x), x, 1) - num) < 1e-6, "sin(x)/x check failed."
