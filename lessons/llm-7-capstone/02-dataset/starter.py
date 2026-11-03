import random


def clean(records):
    out = []
    return out


def split(records, seed):
    return records, [], []


raw = [
    {"prompt": " What is a flake? ", "answer": "A flake is a nix project with pinned inputs. "},
    {"prompt": "what is a flake?", "answer": "duplicate, should go"},
    {"prompt": "Explain the KV cache", "answer": ""},
    {"prompt": "", "answer": "orphan answer"},
] + [{"prompt": f"Question {i}", "answer": f"Answer {i}"} for i in range(30)]
cleaned = clean(raw)
print(len(raw), "raw →", len(cleaned), "clean")
print(cleaned[:1])
train, val, test = split(cleaned, 42)
print(len(train), "train,", len(val), "val,", len(test), "test")
