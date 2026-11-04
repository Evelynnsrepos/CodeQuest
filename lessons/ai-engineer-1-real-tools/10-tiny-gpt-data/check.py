import torch
bv, en, de, gb, TEXT = (ns.get(n) for n in ("build_vocab", "encode", "decode", "get_batch", "TEXT"))
assert bv and en and de and gb and TEXT, "Keep build_vocab, encode, decode, get_batch and TEXT."
stoi, itos = bv("hallo")
assert stoi == {"a": 0, "h": 1, "l": 2, "o": 3} and itos == {0: "a", 1: "h", 2: "l", 3: "o"}, f"build_vocab('hallo') sorts the characters. Got {stoi!r}."
assert en("hallo", stoi) == [1, 0, 2, 2, 3] and de([1, 0, 2, 2, 3], itos) == "hallo", "encode and decode should round-trip."
stoi, itos = bv(TEXT)
data = torch.tensor(en(TEXT, stoi), dtype=torch.long)
x, y = gb(data, 16, 4, torch.Generator().manual_seed(0))
assert tuple(x.shape) == (4, 16) and tuple(y.shape) == (4, 16), f"x and y should be (batch, block) = (4, 16), got {tuple(x.shape)}."
assert x.dtype == torch.long, "Token ids are long integers."
assert torch.equal(x[:, 1:], y[:, :-1]), "y must be x shifted left by one."
ix = torch.randint(len(data) - 16, (4,), generator=torch.Generator().manual_seed(0))
assert torch.equal(x[0], data[ix[0]:ix[0] + 16]), "Use torch.randint(len(data) - block, (batch,), generator=gen) for the starts."
