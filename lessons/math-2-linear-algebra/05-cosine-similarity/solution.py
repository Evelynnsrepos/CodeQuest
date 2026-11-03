import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(v):
    return math.sqrt(dot(v, v))


def cosine(a, b):
    return dot(a, b) / (norm(a) * norm(b))


def angle_degrees(a, b):
    c = max(-1.0, min(1.0, cosine(a, b)))
    return math.degrees(math.acos(c))


def most_similar(query, items):
    return max(items, key=lambda name: cosine(query, items[name]))


print(round(cosine([1, 0], [1, 1]), 3), round(angle_degrees([1, 0], [1, 1]), 1))
words = {"kitten": [0.9, 0.8, 0.1], "tax return": [0.1, -0.2, 0.9], "dog": [0.7, 0.3, 0.2]}
print(most_similar([0.8, 0.7, 0.0], words))
