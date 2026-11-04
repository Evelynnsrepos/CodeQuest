from difflib import SequenceMatcher


def key(s):
    return " ".join(str(s).split()).casefold()


def dedupe(rows, cols):
    seen, out = set(), []
    for r in rows:
        k = tuple(key(r[c]) for c in cols)
        if k not in seen:
            seen.add(k)
            out.append(r)
    return out


def similarity(a, b):
    return SequenceMatcher(None, key(a), key(b)).ratio()


def near_duplicates(texts, threshold=0.9):
    return [(i, j) for i in range(len(texts)) for j in range(i + 1, len(texts))
            if similarity(texts[i], texts[j]) >= threshold]


rows = [{"email": "ada@x.de", "n": 1}, {"email": " ADA@x.de", "n": 2}, {"email": "lin@x.de", "n": 3}]
print(dedupe(rows, ["email"]))
qs = ["What is a flake?", "what is a flake", "How do I install Nix?", "What's a flake?"]
print(round(similarity(qs[0], qs[1]), 3), near_duplicates(qs))
