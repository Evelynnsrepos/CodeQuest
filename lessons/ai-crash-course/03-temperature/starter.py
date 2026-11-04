import math


def softmax_t(scores, t):
    return scores


print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 1)])
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 0.2)])
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 5)])
