import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def sinusoidal(pos, d):
    return [0.0] * d


def rope(x, pos, base=10000):
    return list(x)


q, k = [1.0, 0.0, 0.5, 0.5], [0.0, 1.0, 1.0, 0.0]
print("sinusoidal pos 1:", [round(v, 4) for v in sinusoidal(1, 4)])
print("rope q at 3:", [round(v, 4) for v in rope(q, 3)])
for m, n in [(3, 1), (10, 8), (52, 50)]:
    print(f"q at {m}, k at {n}: score", round(dot(rope(q, m), rope(k, n)), 6))
