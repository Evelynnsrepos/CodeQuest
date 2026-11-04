import math
en, mx = ns.get("entropy"), ns.get("max_entropy")
assert en and mx, "Keep entropy and max_entropy."
assert abs(en([0.5, 0.5]) - 1) < 1e-12, f"Fair coin: 1 bit, got {en([0.5, 0.5])!r}."
assert abs(en([0.9, 0.1]) - 0.4689955936) < 1e-9, f"90/10 coin: 0.469 bits, got {en([0.9, 0.1])!r}."
assert abs(en([1, 0])) < 1e-12, "Certain outcome: 0 (skip p = 0)."
assert abs(en([1 / 6] * 6) - math.log2(6)) < 1e-12, "Fair die: 2.58 bits."
assert abs(en([0.5, 0.5], base=math.e) - math.log(2)) < 1e-12, "In nats: 0.693."
assert abs(mx(6) - math.log2(6)) < 1e-12 and abs(mx(1000, math.e) - math.log(1000)) < 1e-12, "max_entropy(n) = log n."
assert en([0.7, 0.2, 0.1]) < mx(3), "Uneven is less than the maximum."
