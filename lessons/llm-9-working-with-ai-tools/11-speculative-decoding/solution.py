def expected_tokens(alpha, k):
    if alpha == 1:
        return k + 1
    return (1 - alpha ** (k + 1)) / (1 - alpha)


def speedup(alpha, k, c):
    return expected_tokens(alpha, k) / (1 + k * c)


def best_k(alpha, c, max_k=16):
    return max(range(1, max_k + 1), key=lambda k: speedup(alpha, k, c))


print(expected_tokens(0.8, 4), speedup(0.8, 4, 0.05), best_k(0.8, 0.05))
