import math, random
T = ns["TEXT"]
vocab = ns.get("vocab")
assert vocab == sorted(set(T)), "vocab should be the sorted list of unique characters: sorted(set(TEXT))."
V = len(vocab)
tl = ns.get("train_losses")
assert isinstance(tl, list) and len(tl) == 40, f"train_losses should have one entry per epoch (40), it has {len(tl) if isinstance(tl, list) else tl!r}."
assert abs(tl[0] - math.log(V)) < 0.01, f"With all logits at 0 the first training loss should be log V = {math.log(V):.3f}, yours is {tl[0]:.3f}."
assert tl[-1] < tl[0] * 0.8, f"Training loss went from {tl[0]:.3f} to {tl[-1]:.3f}. It should fall by at least 20%. Try a bigger learning rate."
assert all(b <= a + 1e-9 for a, b in zip(tl, tl[1:])) or tl[-1] < min(tl[:5]), "Training loss should mostly go down. If it jumps around, the learning rate may be too high."
vs, ve = ns.get("val_loss_start"), ns.get("val_loss_end")
assert isinstance(vs, float) and abs(vs - math.log(V)) < 0.01, f"val_loss_start should be the validation loss before training, about log V = {math.log(V):.3f}."
assert isinstance(ve, float) and ve < vs - 0.2, f"Validation loss went from {vs!r} to {ve!r}. It should fall clearly too."
gen = ns.get("generate")
out = gen("t", 30, random.Random(1))
assert isinstance(out, str) and len(out) == 30 and set(out) <= set(vocab), f"generate('t', 30, rng) should return 30 characters from the vocabulary, got {out!r}."
