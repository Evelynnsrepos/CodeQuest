import math


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


def patchify(image, p):
    n = len(image)
    patches = []
    for r in range(0, n, p):
        for c in range(0, n, p):
            patches.append([image[r + i][c + j] for i in range(p) for j in range(p)])
    return patches


def zero_shot(image_emb, text_embs, labels):
    scores = [cosine(image_emb, t) for t in text_embs]
    return labels[scores.index(max(scores))]


image = [[r * 4 + c for c in range(4)] for r in range(4)]
print("patches:", patchify(image, 2))

# pretend CLIP embeddings (real ones have 512+ numbers)
labels = ["a photo of a cat", "a photo of a dog", "a photo of a car"]
text_embs = [[0.9, 0.1, 0.0], [0.7, 0.6, 0.1], [0.0, 0.2, 0.9]]
photo = [0.8, 0.5, 0.15]
print("zero-shot label:", zero_shot(photo, text_embs, labels))
