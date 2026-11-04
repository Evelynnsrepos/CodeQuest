TEXT = """Ein Mensch, der viel gelesen hat,
schreibt kluge Worte aufs Papier.
Ein Modell, das viel gelesen hat,
schreibt kluge Worte auch zu dir.
Es lernt von jedem Zeichen, das es sieht,
und rät das nächste, Schritt für Schritt.
Es zählt nicht, und es denkt nicht nach,
es rät nur gut, und rät sehr oft.
""" * 8

import math
import torch
import torch.nn as nn
import torch.nn.functional as F


class CausalSelfAttention(nn.Module):
    def __init__(self, n_embd, n_head, block):
        super().__init__()
        self.n_head = n_head
        self.qkv = nn.Linear(n_embd, 3 * n_embd)
        self.proj = nn.Linear(n_embd, n_embd)
        self.register_buffer("mask", torch.tril(torch.ones(block, block, dtype=torch.bool)))

    def forward(self, x):
        B, T, C = x.shape
        q, k, v = self.qkv(x).split(C, dim=2)
        q, k, v = (t.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) for t in (q, k, v))
        att = q @ k.transpose(-2, -1) / math.sqrt(C // self.n_head)
        att = att.masked_fill(~self.mask[:T, :T], float("-inf"))
        y = att.softmax(dim=-1) @ v
        y = y.transpose(1, 2).contiguous().view(B, T, C)
        return self.proj(y)


class Block(nn.Module):
    def __init__(self, n_embd, n_head, block):
        super().__init__()
        self.ln1 = nn.LayerNorm(n_embd)
        self.attn = CausalSelfAttention(n_embd, n_head, block)
        self.ln2 = nn.LayerNorm(n_embd)
        self.mlp = nn.Sequential(nn.Linear(n_embd, 4 * n_embd), nn.GELU(), nn.Linear(4 * n_embd, n_embd))

    def forward(self, x):
        x = x + self.attn(self.ln1(x))
        return x + self.mlp(self.ln2(x))


class TinyGPT(nn.Module):
    def __init__(self, vocab, n_embd=64, n_head=4, n_layer=2, block=32):
        super().__init__()
        self.block = block
        self.tok = nn.Embedding(vocab, n_embd)
        self.pos = nn.Embedding(block, n_embd)
        self.blocks = nn.Sequential(*[Block(n_embd, n_head, block) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.head = nn.Linear(n_embd, vocab)

    def forward(self, idx, targets=None):
        B, T = idx.shape
        x = self.tok(idx) + self.pos(torch.arange(T, device=idx.device))
        logits = self.head(self.ln_f(self.blocks(x)))
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(B * T, -1), targets.view(B * T))
        return logits, loss


def build_vocab(text):
    chars = sorted(set(text))
    return {c: i for i, c in enumerate(chars)}, {i: c for i, c in enumerate(chars)}


def get_batch(data, block, batch, gen):
    ix = torch.randint(len(data) - block, (batch,), generator=gen)
    return torch.stack([data[i:i + block] for i in ix]), torch.stack([data[i + 1:i + block + 1] for i in ix])


def train(model, data, steps, block=32, batch=16, lr=3e-3, seed=0):
    torch.manual_seed(seed)
    gen = torch.Generator().manual_seed(seed)
    opt = torch.optim.AdamW(model.parameters(), lr=lr)
    model.train()
    losses = []
    for _ in range(steps):
        x, y = get_batch(data, block, batch, gen)
        _, loss = model(x, y)
        opt.zero_grad()
        loss.backward()
        opt.step()
        losses.append(loss.item())
    return losses


def generate(model, idx, n, seed=0, temperature=1.0):
    gen = torch.Generator().manual_seed(seed)
    model.eval()
    with torch.no_grad():
        for _ in range(n):
            logits, _ = model(idx[:, -model.block:])
            probs = F.softmax(logits[:, -1, :] / temperature, dim=-1)
            idx = torch.cat([idx, torch.multinomial(probs, 1, generator=gen)], dim=1)
    return idx


stoi, itos = build_vocab(TEXT)
data = torch.tensor([stoi[c] for c in TEXT], dtype=torch.long)
torch.manual_seed(0)
model = TinyGPT(len(stoi))
losses = train(model, data, 400)
print("first and last loss:", losses[:1], losses[-1:])
out = generate(model, torch.tensor([[stoi["E"]]]), 200)
print("".join(itos[int(i)] for i in out[0]))
