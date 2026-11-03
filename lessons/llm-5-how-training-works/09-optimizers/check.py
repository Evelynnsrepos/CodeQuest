import math
step, sched = ns.get("adamw_step"), ns.get("lr_at")
assert step and sched, "Keep adamw_step and lr_at."
p, m, v = [1.0, -2.0], [0.0, 0.0], [0.0, 0.0]
step(p, [0.5, -4.0], m, v, 1, 0.1, 0.0)
assert abs(m[0] - 0.05) < 1e-12 and abs(v[0] - 0.00025) < 1e-12, f"After one step, m[0] should be 0.05 and v[0] 0.00025, got {m[0]}, {v[0]}. Update m and v in place."
assert abs(p[0] - 0.9) < 1e-6 and abs(p[1] - (-1.9)) < 1e-6, f"Adam's first step moves each weight by about lr against its gradient's sign: expected [0.9, −1.9], got {p!r}."
p, m, v = [2.0], [0.0], [0.0]
step(p, [0.0], m, v, 1, 0.1, 0.5)
assert abs(p[0] - 1.9) < 1e-9, f"With zero gradient, weight decay alone should shrink 2.0 by lr·wd·p = 0.1, giving 1.9; got {p[0]!r}."
p, m, v = [0.0], [0.0], [0.0]
for t in range(1, 4):
    step(p, [1.0], m, v, t, 0.01, 0.0)
assert abs(p[0] - (-0.03)) < 1e-6, f"Three steps with a constant gradient of 1 and lr 0.01 should reach about −0.03 (bias correction keeps steps ≈ lr), got {p[0]!r}."
assert abs(sched(0, 1.0, 10, 110) - 0.1) < 1e-12 and abs(sched(9, 1.0, 10, 110) - 1.0) < 1e-12, "During warmup lr = max_lr · (step + 1) / warmup."
assert abs(sched(10, 1.0, 10, 110) - 1.0) < 1e-12, "Right after warmup the cosine starts at max_lr."
assert abs(sched(60, 1.0, 10, 110) - 0.5) < 1e-12, "Halfway through the decay, the cosine schedule is at max_lr / 2."
assert sched(109, 1.0, 10, 110) < 0.001, "At the end, the learning rate should be near 0."
