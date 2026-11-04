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
    return {c: i for i, c in enumerate(chars)}, {i: c for i, c in enumerate(chars)}


def encode(s, stoi):
    return [stoi[c] for c in s]


def decode(ids, itos):
    return "".join(itos[int(i)] for i in ids)


def get_batch(data, block, batch, gen):
    ix = torch.randint(len(data) - block, (batch,), generator=gen)
    x = torch.stack([data[i:i + block] for i in ix])
    y = torch.stack([data[i + 1:i + block + 1] for i in ix])
    return x, y


stoi, itos = build_vocab(TEXT)
data = torch.tensor(encode(TEXT, stoi), dtype=torch.long)
print(len(stoi), "characters;", len(data), "tokens")
x, y = get_batch(data, 8, 2, torch.Generator().manual_seed(0))
print(x, y)
