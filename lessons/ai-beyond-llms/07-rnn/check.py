import math
st, rr = ns.get("rnn_step"), ns.get("run_rnn")
assert st and rr, "Keep rnn_step and run_rnn."
got = st([1.0], [0.5, -0.5], [[2.0], [0.0]], [[1.0, 0.0], [0.0, 1.0]], [0.0, 0.25])
want = [math.tanh(2.5), math.tanh(-0.25)]
assert all(abs(a - b) < 1e-12 for a, b in zip(got, want)), f"rnn_step should be tanh(Wx·x + Wh·h + b) = {want!r}, got {got!r}."
states = rr([[1.0], [1.0]], [[1.0]], [[0.5]], [0.0])
h1 = math.tanh(1.0); h2 = math.tanh(1.0 + 0.5 * h1)
assert len(states) == 2 and abs(states[0][0] - h1) < 1e-12 and abs(states[1][0] - h2) < 1e-12, f"run_rnn should return [{h1:.4f}], [{h2:.4f}], got {states!r}. Start h at zeros and carry it forward."
