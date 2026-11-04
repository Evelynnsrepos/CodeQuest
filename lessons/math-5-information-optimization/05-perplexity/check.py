import math
pp, pf, lf = ns.get("perplexity"), ns.get("ppl_from_loss"), ns.get("loss_from_ppl")
assert pp and pf and lf, "Keep perplexity, ppl_from_loss and loss_from_ppl."
assert abs(pp([0.5, 0.25]) - math.sqrt(8)) < 1e-12, f"perplexity([0.5, 0.25]) ≈ 2.83, got {pp([0.5, 0.25])!r}."
assert abs(pp([0.001] * 7) - 1000) < 1e-6, "Uniform over 1000: perplexity 1000."
assert abs(pp([1.0, 1.0, 1.0]) - 1) < 1e-12, "Always sure and right: 1."
assert abs(pp([0.5] * 2) - pp([0.5] * 50)) < 1e-12, "Average, don't sum: length must not matter."
assert abs(pf(2.1) - 8.1661699126) < 1e-9, "e^2.1 ≈ 8.17."
assert abs(lf(1000) - math.log(1000)) < 1e-12 and abs(lf(pf(1.3)) - 1.3) < 1e-12, "loss_from_ppl undoes ppl_from_loss."
