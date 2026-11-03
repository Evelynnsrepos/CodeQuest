import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(v):
    return math.sqrt(dot(v, v))


def cosine(a, b):
    return 0.0


def angle_degrees(a, b):
    return 0.0


def most_similar(query, items):
    return ""


print(round(cosine([1, 0], [1, 1]), 3), round(angle_degrees([1, 0], [1, 1]), 1))
words = {"kitten": [0.9, 0.8, 0.1], "tax return": [0.1, -0.2, 0.9], "dog": [0.7, 0.3, 0.2]}
print(most_similar([0.8, 0.7, 0.0], words))
