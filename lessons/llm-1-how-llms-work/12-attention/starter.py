import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def softmax(scores):
    if not scores:
        return []
    m = max(scores)
    exps = [math.exp(s - m) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def attend(q, keys, values):
    scores = []
    weights = softmax(scores)
    output = [0.0] * len(values[0])
    return output


# "The animal didn't cross the street because it ..." — the query for "it"
words = ["animal", "street", "because"]
keys = [[2.0, 1.0, 0.0, 1.0], [0.0, 1.0, 2.0, 0.0], [0.5, 0.0, 0.5, 0.0]]
values = [[1.0, 0.0], [0.0, 1.0], [0.5, 0.5]]
q_it = [2.0, 0.5, 0.0, 1.0]
print([round(x, 3) for x in attend(q_it, keys, values)])
