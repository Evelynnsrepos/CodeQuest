import math


def dot(a, b):
    # total = 0
    # for i in range(len(a)):   inside: total = total + a[i] * b[i]
    # return total
    return 0


def length(v):
    # total = 0
    # for x in v:   inside: total = total + x * x
    # return math.sqrt(total)
    return 0


def cosine(a, b):
    # return dot(a, b) / (length(a) * length(b))
    return 0.0


def closest(query, items):
    # best = None   and   best_score = -2
    # for name in items:
    #     score = cosine(query, items[name])
    #     if score > best_score: remember name and score
    # return best
    return None


animals = {"kitten": [0.9, 0.8, 0.1], "car": [0.1, 0.0, 0.95], "puppy": [0.8, 0.9, 0.0]}
print(dot([3, 4], [4, 3]), length([3, 4]), cosine([3, 4], [4, 3]), closest([0.95, 0.75, 0.05], animals))
