import random, io, contextlib
T, M, V = ns.get("train"), ns["MLP"], ns["Value"]
assert T, "Keep the function train."
random.seed(7)
m = M(2, [3, 1])
xs, ys = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], [1.0, -1.0, 0.5]
with contextlib.redirect_stdout(io.StringIO()):
    first = T(m, xs, ys, 0.0, 1)
    final = T(m, xs, ys, 0.05, 80)
assert isinstance(final, float), "train should return loss.data, a number."
assert first > 0.1, "With a learning rate of 0 the loss should stay where it started. Compute the loss from the predictions."
assert final < first * 0.1, f"Loss went from {first:.3f} to {final:.3f}. It should drop a lot. Did you zero the grads and update p.data -= lr * p.grad?"
assert ns["final"] < 0.05, f"Your main run ended with loss {ns['final']:.4f}; it should get below 0.05."
