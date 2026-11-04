import math
import torch
G, A = ns.get("TinyGPT"), ns.get("CausalSelfAttention")
assert G and A, "Keep TinyGPT and CausalSelfAttention."
torch.manual_seed(0)
att = A(16, 4, 8)
x = torch.randn(2, 5, 16)
y = att(x)
assert tuple(y.shape) == (2, 5, 16), f"Attention output must keep the shape (B, T, C) = (2, 5, 16), got {tuple(y.shape)}."
x2 = x.clone(); x2[:, 3:] = torch.randn(2, 2, 16)
assert torch.allclose(att(x2)[:, :3], y[:, :3], atol=1e-6), "Not causal: changing tokens 3 and 4 changed the outputs of tokens 0 to 2. Apply the mask before softmax."
assert not torch.allclose(att(x2)[:, 3:], y[:, 3:]), "Attention should actually depend on the input."
model = G(vocab=40)
idx = torch.randint(40, (3, 12))
logits, loss = model(idx, idx)
assert logits is not None and tuple(logits.shape) == (3, 12, 40), "logits must be (B, T, vocab)."
assert loss is not None and abs(loss.item() - math.log(40)) < 0.6, f"A fresh model's loss should be near ln(40) ≈ 3.69, got {loss.item() if loss is not None else None}."
assert model(idx)[1] is None, "Without targets, loss is None."
idx2 = idx.clone(); idx2[:, 6:] = (idx2[:, 6:] + 1) % 40
assert torch.allclose(model(idx2)[0][:, :6], logits[:, :6], atol=1e-5), "The whole model must be causal too."
