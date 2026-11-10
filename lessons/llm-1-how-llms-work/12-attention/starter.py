import math


def dot(a, b):
    total = 0
    for i in range(len(a)):
        total = total + a[i] * b[i]
    return total


def softmax(scores):
    if len(scores) == 0:
        return []
    m = max(scores)
    exps = []
    for s in scores:
        exps.append(math.exp(s - m))
    total = sum(exps)
    probs = []
    for e in exps:
        probs.append(e / total)
    return probs


def attend(q, keys, values):
    scores = []
    # for k in keys:
    #     scores.append(dot(q, k) / math.sqrt(len(q)))
    weights = softmax(scores)
    output = [0.0] * len(values[0])
    # for j in range(len(values)):
    #     w = weights[j]
    #     v = values[j]
    #     for i in range(len(v)):
    #         output[i] = output[i] + w * v[i]
    return output


# "The animal didn't cross the street because it ..." - the query for "it"
words = ["animal", "street", "because"]
keys = [[2.0, 1.0, 0.0, 1.0], [0.0, 1.0, 2.0, 0.0], [0.5, 0.0, 0.5, 0.0]]
values = [[1.0, 0.0], [0.0, 1.0], [0.5, 0.5]]
q_it = [2.0, 0.5, 0.0, 1.0]
result = attend(q_it, keys, values)
print([round(result[0], 3), round(result[1], 3)])
