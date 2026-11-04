def shingles(text, n=3):
    return set()


def jaccard(a, b):
    return 0.0


def dedupe(docs, threshold):
    return docs


docs = [
    "The cat sat on the mat and looked at the bird outside.",
    "the cat sat on the mat and looked at the bird outside!",
    "The cat sat on the mat and looked at the dog outside.",
    "Quantization stores weights in fewer bits to save memory.",
]
print(round(jaccard(shingles(docs[0]), shingles(docs[2])), 3))
print(dedupe(docs, 0.5))
