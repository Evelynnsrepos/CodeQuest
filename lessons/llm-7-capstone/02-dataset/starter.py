import random


def clean(records):
    out = []
    # seen = set()
    # for r in records:
    #     prompt = r["prompt"].strip()
    #     answer = r["answer"].strip()
    #     if prompt == "" or answer == "":
    #         continue
    #     key = prompt.lower()
    #     if key in seen:
    #         continue
    #     seen.add(key)
    #     out.append({"prompt": prompt, "answer": answer})
    return out


def split(records, seed):
    # items = list(records)
    # random.Random(seed).shuffle(items)
    # n = len(items) // 10
    # end_train = len(items) - 2 * n
    # end_val = len(items) - n
    # train = items[:end_train]
    # val = items[end_train:end_val]
    # test = items[end_val:]
    # return train, val, test
    return records, [], []


raw = [
    {"prompt": " What is a flake? ", "answer": "A flake is a nix project with pinned inputs. "},
    {"prompt": "what is a flake?", "answer": "duplicate, should go"},
    {"prompt": "Explain the KV cache", "answer": ""},
    {"prompt": "", "answer": "orphan answer"},
]
for i in range(30):
    raw.append({"prompt": "Question " + str(i), "answer": "Answer " + str(i)})
cleaned = clean(raw)
print(len(raw), "raw →", len(cleaned), "clean")
print(cleaned[:1])
train, val, test = split(cleaned, 42)
print(len(train), "train,", len(val), "val,", len(test), "test")
