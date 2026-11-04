def shingles(text, n=3):
    words = "".join(c for c in text.lower() if c.isalnum() or c.isspace()).split()
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def jaccard(a, b):
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)


def dedupe(docs, threshold):
    kept, kept_sh = [], []
    for d in docs:
        s = shingles(d)
        if all(jaccard(s, k) < threshold for k in kept_sh):
            kept.append(d)
            kept_sh.append(s)
    return kept


docs = [
    "The cat sat on the mat and looked at the bird outside.",
    "the cat sat on the mat and looked at the bird outside!",
    "The cat sat on the mat and looked at the dog outside.",
    "Quantization stores weights in fewer bits to save memory.",
]
print(round(jaccard(shingles(docs[0]), shingles(docs[2])), 3))
print(dedupe(docs, 0.5))
