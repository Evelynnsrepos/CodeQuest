import math
il, lr = ns.get("initial_loss"), ns.get("lr_at")
assert il and lr, "Keep initial_loss and lr_at."
assert abs(il(50257) - 10.8249) < 1e-3, f"initial_loss(50257) should be ln(50257) = 10.82, got {il(50257)!r}."
assert abs(il(65) - math.log(65)) < 1e-9, "For 65 characters it's ln(65)."
args = (1e-3, 1e-4, 10, 110)
assert abs(lr(0, *args) - 1e-4) < 1e-12, f"Step 0 of a 10-step warmup should be max_lr * 1/10, got {lr(0, *args)!r}."
assert abs(lr(9, *args) - 1e-3) < 1e-12, "The last warmup step should reach max_lr."
assert abs(lr(10, *args) - 1e-3) < 1e-12, "Right after warmup the cosine starts at max_lr."
assert abs(lr(60, *args) - 5.5e-4) < 1e-12, f"Halfway through the decay lr should be halfway between max and min (5.5e-4), got {lr(60, *args)!r}."
assert abs(lr(110, *args) - 1e-4) < 1e-12 and abs(lr(500, *args) - 1e-4) < 1e-12, "From step total on, lr stays at min_lr."
