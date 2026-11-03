import math
f = ns.get("loss_and_grad")
assert f, "Keep the function loss_and_grad."
W = [[0.0] * 27 for _ in range(27)]
loss, grad = f(W, [(0, 1), (0, 2)])
assert abs(loss - math.log(27)) < 1e-9, f"With all-zero logits the loss should be log 27 ≈ 3.296, got {loss!r}."
assert abs(grad[0][1] - (1 / 27 - 0.5)) < 1e-9, f"grad[0][1] should be (1/27 + 1/27 − 1) / 2, got {grad[0][1]!r}. Did you divide by the number of pairs?"
assert abs(grad[0][5] - 1 / 27) < 1e-9, f"grad[0][5] should be 1/27 (probability, never the true token), got {grad[0][5]!r}."
assert all(g == 0 for g in grad[3]), "Rows that never appear as the first character should have zero gradient."
assert ns.get("final_loss", 9) < 2.45, f"After training, the loss should be close to 2.3; it ended at {ns.get('final_loss')!r}."
