from difflib import SequenceMatcher


def key(s):
    return " ".join(str(s).split()).casefold()


def dedupe(rows, cols):
    return rows


def similarity(a, b):
    return 0.0


def near_duplicates(texts, threshold=0.9):
    return []


rows = [{"email": "ada@x.de", "n": 1}, {"email": " ADA@x.de", "n": 2}, {"email": "lin@x.de", "n": 3}]
print(dedupe(rows, ["email"]))
qs = ["What is a flake?", "what is a flake", "How do I install Nix?", "What's a flake?"]
print(round(similarity(qs[0], qs[1]), 3), near_duplicates(qs))
