import random


def clean(records):
    out, seen = [], set()
    for r in records:
        prompt, answer = r["prompt"].strip(), r["answer"].strip()
        if not prompt or not answer:
            continue
        key = prompt.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append({"prompt": prompt, "answer": answer})
    return out


def split(records, seed):
    items = list(records)
    random.Random(seed).shuffle(items)
    n = len(items) // 10
    train = items[:len(items) - 2 * n]
    val = items[len(items) - 2 * n:len(items) - n]
    test = items[len(items) - n:]
    return train, val, test


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
