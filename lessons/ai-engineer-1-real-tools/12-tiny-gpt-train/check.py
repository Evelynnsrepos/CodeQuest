import math
import torch
G, tr, ge, bv, TEXT = (ns.get(n) for n in ("TinyGPT", "train", "generate", "build_vocab", "TEXT"))
assert G and tr and ge and bv and TEXT, "Keep TinyGPT, train, generate, build_vocab and TEXT."
stoi, itos = bv(TEXT)
data = torch.tensor([stoi[c] for c in TEXT], dtype=torch.long)
torch.manual_seed(1)
model = G(len(stoi))
losses = tr(model, data, 400)
assert len(losses) == 400, f"train should return one loss per step (400), got {len(losses)}."
assert abs(losses[0] - math.log(len(stoi))) < 0.7, f"The first loss should be near ln({len(stoi)}) ≈ {math.log(len(stoi)):.2f}, got {losses[0]:.2f}."
tail = sum(losses[-20:]) / 20
assert tail < 1.0, f"After 400 steps the last 20 losses should average below 1.0, got {tail:.2f}. Check zero_grad/backward/step and the learning rate."
out = ge(model, torch.tensor([[stoi["E"]]]), 120)
assert tuple(out.shape) == (1, 121), f"generate should return shape (1, start + n) = (1, 121), got {tuple(out.shape)}."
text = "".join(itos[int(i)] for i in out[0])
words = [w for w in text.split() if len(w) > 3]
known = set(TEXT.split())
assert words and sum(w in known for w in words) / len(words) > 0.5, f"The sample doesn't look like the poem yet: {text[:80]!r}"
assert torch.equal(ge(model, torch.tensor([[stoi["E"]]]), 20, seed=5), ge(model, torch.tensor([[stoi["E"]]]), 20, seed=5)), "Same seed, same sample: use the generator."
