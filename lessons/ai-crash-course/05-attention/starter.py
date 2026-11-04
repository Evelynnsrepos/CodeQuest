import math


def weights(scores):
    return scores


def attend(scores, values):
    return values[0]


print([round(w, 2) for w in weights([0.0, 2.6, 0.0, 1.4])])
print([round(x, 2) for x in attend([0.0, 2.6, 0.0, 1.4], [[1, 0], [0, 1], [1, 1], [0.5, 0]])])
