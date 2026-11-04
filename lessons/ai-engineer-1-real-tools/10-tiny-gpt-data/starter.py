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
    return {}, {}


def encode(s, stoi):
    return []


def decode(ids, itos):
    return ""


def get_batch(data, block, batch, gen):
    return None, None


stoi, itos = build_vocab(TEXT)
data = torch.tensor(encode(TEXT, stoi), dtype=torch.long)
print(len(stoi), "characters;", len(data), "tokens")
x, y = get_batch(data, 8, 2, torch.Generator().manual_seed(0))
print(x, y)
