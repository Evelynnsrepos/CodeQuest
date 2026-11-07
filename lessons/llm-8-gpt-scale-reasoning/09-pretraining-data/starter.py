def shingles(text, n=3):
    # clean = ""
    # for c in text.lower():
    #     if c.isalnum() or c.isspace():
    #         clean = clean + c
    # words = clean.split()
    # result = set()
    # for i in range(len(words) - n + 1):
    #     result.add(tuple(words[i:i + n]))
    # return result
    return set()


def jaccard(a, b):
    # if len(a) == 0 and len(b) == 0:
    #     return 0.0
    # return len(a & b) / len(a | b)
    return 0.0


def dedupe(docs, threshold):
    # kept = []
    # kept_sh = []
    # for d in docs:
    #     s = shingles(d)
    #     unique = True
    #     for k in kept_sh:
    #         if jaccard(s, k) >= threshold:
    #             unique = False
    #     if unique:
    #         kept.append(d)
    #         kept_sh.append(s)
    # return kept
    return docs


docs = [
    "The cat sat on the mat and looked at the bird outside.",
    "the cat sat on the mat and looked at the bird outside!",
    "The cat sat on the mat and looked at the dog outside.",
    "Quantization stores weights in fewer bits to save memory.",
]
print(round(jaccard(shingles(docs[0]), shingles(docs[2])), 3))
print(dedupe(docs, 0.5))
