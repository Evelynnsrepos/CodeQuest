def expected_tokens(alpha, k):
    return k + 1


def speedup(alpha, k, c):
    return 0


def best_k(alpha, c, max_k=16):
    return 1


print(expected_tokens(0.8, 4), speedup(0.8, 4, 0.05), best_k(0.8, 0.05))
