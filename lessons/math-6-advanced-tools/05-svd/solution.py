import math


def transpose(A):
    return [list(col) for col in zip(*A)]


def matmul(A, B):
    Bt = transpose(B)
    return [[sum(a * b for a, b in zip(row, col)) for col in Bt] for row in A]


def normalize(v):
    n = math.sqrt(sum(x * x for x in v))
    return [x / n for x in v]


def top_singular(A, steps=200):
    AtA = matmul(transpose(A), A)
    v = normalize([1.0] * len(AtA))
    for _ in range(steps):
        v = normalize([sum(m * x for m, x in zip(row, v)) for row in AtA])
    Av = [sum(a * x for a, x in zip(row, v)) for row in A]
    sigma = math.sqrt(sum(x * x for x in Av))
    return sigma, [x / sigma for x in Av], v


def rank1(A):
    s, u, v = top_singular(A)
    return [[s * a * b for b in v] for a in u]


def frobenius(A):
    return math.sqrt(sum(x * x for row in A for x in row))


def lora_params(d, k, r):
    return r * (d + k)


def full_params(d, k):
    return d * k


A = [[3, 0], [4, 5]]
print(top_singular(A), rank1(A), lora_params(4096, 4096, 16), full_params(4096, 4096))
