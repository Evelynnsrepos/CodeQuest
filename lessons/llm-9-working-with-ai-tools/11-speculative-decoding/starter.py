def expected_tokens(alpha, k):
    # if alpha == 1:
    #     return k + 1
    # return (1 - alpha ** (k + 1)) / (1 - alpha)
    return k + 1


def speedup(alpha, k, c):
    # return expected_tokens(alpha, k) / (1 + k * c)
    return 0


def best_k(alpha, c, max_k=16):
    # best = 1
    # best_s = speedup(alpha, 1, c)
    # for k in range(2, max_k + 1):
    #     s = speedup(alpha, k, c)
    #     if s > best_s:
    #         best = k
    #         best_s = s
    # return best
    return 1


print(expected_tokens(0.8, 4), speedup(0.8, 4, 0.05), best_k(0.8, 0.05))
