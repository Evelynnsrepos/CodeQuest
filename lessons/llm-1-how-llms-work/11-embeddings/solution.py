import math


def dot(a, b):
    total = 0
    for x, y in zip(a, b):
        total += x * y
    return total


def cosine(a, b):
    return dot(a, b) / (math.sqrt(dot(a, a)) * math.sqrt(dot(b, b)))


EMBEDDINGS = {
    "king": [0.9, 0.8, 0.1],
    "queen": [0.85, 0.75, 0.9],
    "prince": [0.8, 0.6, 0.15],
    "banana": [-0.2, 0.1, 0.3],
    "keyboard": [0.1, -0.9, 0.05],
}

for word, vec in EMBEDDINGS.items():
    if word != "king":
        print(f"{word:9} {cosine(EMBEDDINGS['king'], vec):.2f}")
