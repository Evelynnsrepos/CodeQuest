import math


def dot(a, b):
    total = 0
    for i in range(len(a)):
        total = total + a[i] * b[i]
    return total


def sinusoidal(pos, d):
    pe = []
    for i in range(d // 2):
        a = pos / 10000 ** (2 * i / d)
        pe.append(math.sin(a))
        pe.append(math.cos(a))
    return pe


def rope(x, pos, base=10000):
    d = len(x)
    out = []
    for i in range(d // 2):
        a = pos * base ** (-2 * i / d)
        x0 = x[2 * i]
        x1 = x[2 * i + 1]
        out.append(x0 * math.cos(a) - x1 * math.sin(a))
        out.append(x0 * math.sin(a) + x1 * math.cos(a))
    return out


q, k = [1.0, 0.0, 0.5, 0.5], [0.0, 1.0, 1.0, 0.0]
print("sinusoidal pos 1:", [round(v, 4) for v in sinusoidal(1, 4)])
print("rope q at 3:", [round(v, 4) for v in rope(q, 3)])
for m, n in [(3, 1), (10, 8), (52, 50)]:
    print(f"q at {m}, k at {n}: score", round(dot(rope(q, m), rope(k, n)), 6))
