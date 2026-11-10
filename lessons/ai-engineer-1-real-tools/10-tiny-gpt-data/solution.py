TEXT = """Ein Mensch, der viel gelesen hat,
schreibt kluge Worte aufs Papier.
Ein Modell, das viel gelesen hat,
schreibt kluge Worte auch zu dir.
Es lernt von jedem Zeichen, das es sieht,
und rät das nächste, Schritt für Schritt.
Es zählt nicht, und es denkt nicht nach,
es rät nur gut, und rät sehr oft.
""" * 8

import torch


def build_vocab(text):
    chars = sorted(set(text))
    stoi = {}
    itos = {}
    for i in range(len(chars)):
        stoi[chars[i]] = i
        itos[i] = chars[i]
    return stoi, itos


def encode(s, stoi):
    ids = []
    for c in s:
        ids.append(stoi[c])
    return ids


def decode(ids, itos):
    out = ""
    for i in ids:
        out = out + itos[int(i)]
    return out


def get_batch(data, block, batch, gen):
    ix = torch.randint(len(data) - block, (batch,), generator=gen)
    xs = []
    ys = []
    for i in ix:
        xs.append(data[i:i + block])
        ys.append(data[i + 1:i + block + 1])
    return torch.stack(xs), torch.stack(ys)


stoi, itos = build_vocab(TEXT)
data = torch.tensor(encode(TEXT, stoi), dtype=torch.long)
print(len(stoi), "characters;", len(data), "tokens")
x, y = get_batch(data, 8, 2, torch.Generator().manual_seed(0))
print(x, y)
