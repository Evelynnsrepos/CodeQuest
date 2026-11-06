import math


def weights(scores):
    # biggest = max(scores)
    # exps = []     for s in scores:   inside: exps.append(math.exp(s - biggest))
    # total = sum(exps)
    # result = []   for e in exps:     inside: result.append(e / total)
    # return result
    return scores


def attend(scores, values):
    # w = weights(scores)
    # size = len(values[0])
    # result = []
    # for d in range(size):
    #     total = 0
    #     for i in range(len(values)):
    #         total = total + w[i] * values[i][d]
    #     result.append(total)
    # return result
    return values[0]


# These lines just show your results rounded to 2 decimals. You don't need to change them.
print([round(x, 2) for x in weights([0.0, 2.6, 0.0, 1.4])])
print([round(x, 2) for x in attend([0.0, 2.6, 0.0, 1.4], [[1, 0], [0, 1], [1, 1], [0.5, 0]])])
