bc, dg = ns.get("best_checkpoint"), ns.get("diagnose")
assert bc and dg, "Keep best_checkpoint and diagnose."
h = [{"step": 5, "loss": 2.0}, {"step": 5, "eval_loss": 2.1}, {"step": 10, "loss": 1.5}, {"step": 10, "eval_loss": 1.7},
     {"step": 15, "loss": 1.2}, {"step": 15, "eval_loss": 1.8}]
assert bc(h) == 10, f"best_checkpoint should be step 10 (eval_loss 1.7), got {bc(h)!r}."
assert dg(h) == ["overfitting"], f"diagnose should report ['overfitting'], got {dg(h)!r}."
good = [{"step": 5, "loss": 2.0}, {"step": 5, "eval_loss": 2.1}, {"step": 10, "loss": 1.5}, {"step": 10, "eval_loss": 1.7}]
assert dg(good) == [], f"A healthy run should have no problems, got {dg(good)!r}."
bad = [{"step": 5, "loss": float("nan")}, {"step": 5, "eval_loss": 1.0}, {"step": 10, "loss": 0.01}, {"step": 10, "eval_loss": 1.3}]
assert dg(bad) == ["nan loss", "overfitting", "memorizing"], f"Expected all three problems in order, got {dg(bad)!r}."
