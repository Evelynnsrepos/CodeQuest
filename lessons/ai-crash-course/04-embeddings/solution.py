import math


def dot(a, b):
    total = 0
    for i in range(len(a)):
        total = total + a[i] * b[i]
    return total


def length(v):
    total = 0
    for x in v:
        total = total + x * x
    return math.sqrt(total)


def cosine(a, b):
    return dot(a, b) / (length(a) * length(b))


def closest(query, items):
    best = None
    best_score = -2
    for name in items:
        score = cosine(query, items[name])
        if score > best_score:
            best = name
            best_score = score
    return best


animals = {"kitten": [0.9, 0.8, 0.1], "car": [0.1, 0.0, 0.95], "puppy": [0.8, 0.9, 0.0]}
print(dot([3, 4], [4, 3]), length([3, 4]), cosine([3, 4], [4, 3]), closest([0.95, 0.75, 0.05], animals))
