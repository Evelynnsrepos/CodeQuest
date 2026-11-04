eb, ts, wf = ns.get("effective_batch"), ns.get("total_steps"), ns.get("warnings_for")
assert eb and ts and wf, "Keep effective_batch, total_steps and warnings_for."
assert eb(2, 8) == 16 and eb(4, 4, 2) == 32, "effective_batch is per_device × accumulation × gpus."
assert ts(500, 2, 8, 3) == 96, f"total_steps(500, 2, 8, 3) returned {ts(500, 2, 8, 3)!r}, expected ⌈500/16⌉ × 3 = 96."
assert ts(32, 4, 4, 1) == 2, "Exact multiples shouldn't round up: 32 examples / 16 = 2 steps."
ok = {"lr": 2e-4, "epochs": 2, "examples": 1000, "per_device": 2, "accumulation": 8}
assert wf(ok) == [], f"A sensible config should have no warnings, got {wf(ok)!r}."
bad = {"lr": 1e-3, "epochs": 10, "examples": 40, "per_device": 1, "accumulation": 2}
assert wf(bad) == ["learning rate too high", "too many epochs", "effective batch too small"], f"Got {wf(bad)!r}. Check each condition, in the listed order (this run has 200 steps, so no step warning)."
low = {"lr": 5e-6, "epochs": 1, "examples": 100, "per_device": 2, "accumulation": 8}
assert wf(low) == ["learning rate too low", "very few steps"], f"Got {wf(low)!r} for lr 5e-6 and 7 steps."
