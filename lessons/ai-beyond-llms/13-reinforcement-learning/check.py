gr, qu = ns.get("greedy"), ns.get("q_update")
assert gr and qu, "Keep greedy and q_update."
assert gr({0: [0.1, 0.5, 0.2]}, 0) == 1, "greedy should pick the highest value."
assert gr({0: [0.3, 0.3]}, 0) == 0, "On a tie, the lowest index."
Q = {0: [0.0, 0.0], 1: [0.0, 2.0]}
got = qu(Q, 0, 1, 0.5, 1, 0.5, 0.9)
assert abs(got - 1.15) < 1e-12 and abs(Q[0][1] - 1.15) < 1e-12, f"target = 0.5 + 0.9·2 = 2.3, new Q = 0 + 0.5·2.3 = 1.15, got {got!r} (and Q must be updated in place)."
Q = {0: [1.0, 0.0]}
got = qu(Q, 0, 0, 3.0, None, 0.1, 0.9)
assert abs(got - 1.2) < 1e-12, f"Terminal step: target is just r = 3, new Q = 1 + 0.1·(3 − 1) = 1.2, got {got!r}."
