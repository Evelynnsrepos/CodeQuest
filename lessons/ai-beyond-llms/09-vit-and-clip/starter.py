import math


def cosine(a, b):
    dot = 0
    size_a = 0
    size_b = 0
    for i in range(len(a)):
        dot = dot + a[i] * b[i]
        size_a = size_a + a[i] * a[i]
        size_b = size_b + b[i] * b[i]
    return dot / (math.sqrt(size_a) * math.sqrt(size_b))


def patchify(image, p):
    # n = len(image)
    # patches = []
    # for r in range(0, n, p):
    #     for c in range(0, n, p):
    #         patch = []
    #         for i in range(p):
    #             for j in range(p):
    #                 patch.append(image[r + i][c + j])
    #         patches.append(patch)
    # return patches
    return []


def zero_shot(image_emb, text_embs, labels):
    # best = 0
    # best_s = cosine(image_emb, text_embs[0])
    # for i in range(1, len(text_embs)):
    #     s = cosine(image_emb, text_embs[i])
    #     if s > best_s:
    #         best = i
    #         best_s = s
    # return labels[best]
    return labels[0]


image = [[r * 4 + c for c in range(4)] for r in range(4)]
print("patches:", patchify(image, 2))

# pretend CLIP embeddings (real ones have 512+ numbers)
labels = ["a photo of a cat", "a photo of a dog", "a photo of a car"]
text_embs = [[0.9, 0.1, 0.0], [0.7, 0.6, 0.1], [0.0, 0.2, 0.9]]
photo = [0.8, 0.5, 0.15]
print("zero-shot label:", zero_shot(photo, text_embs, labels))
