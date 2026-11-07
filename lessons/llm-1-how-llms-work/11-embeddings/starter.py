import math


def dot(a, b):
    # total = 0
    # for i in range(len(a)):
    #     total = total + a[i] * b[i]
    # return total
    return 0


def cosine(a, b):
    # return dot(a, b) / (math.sqrt(dot(a, a)) * math.sqrt(dot(b, b)))
    return 0


EMBEDDINGS = {
    "king": [0.9, 0.8, 0.1],
    "queen": [0.85, 0.75, 0.9],
    "prince": [0.8, 0.6, 0.15],
    "banana": [-0.2, 0.1, 0.3],
    "keyboard": [0.1, -0.9, 0.05],
}

for word in EMBEDDINGS:
    if word != "king":
        print(word, round(cosine(EMBEDDINGS["king"], EMBEDDINGS[word]), 2))
