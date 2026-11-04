po, kr = ns.get("ppo_objective"), ns.get("kl_penalized_reward")
assert po and kr, "Keep ppo_objective and kl_penalized_reward."
assert abs(po(1.5, 1.0) - 1.2) < 1e-12, f"ratio 1.5 with A = +1 should be capped at 1.2, got {po(1.5, 1.0)!r}."
assert abs(po(0.5, 1.0) - 0.5) < 1e-12, "ratio 0.5 with A = +1: min(0.5, 0.8) = 0.5."
assert abs(po(0.5, -1.0) - (-0.8)) < 1e-12, f"ratio 0.5 with A = -1: min(-0.5, -0.8) = -0.8, got {po(0.5, -1.0)!r}."
assert abs(po(1.5, -1.0) - (-1.5)) < 1e-12, "ratio 1.5 with A = -1: min(-1.5, -1.2) = -1.5 (no clipping benefit for making a bad token likelier)."
assert abs(po(1.1, 2.0, eps=0.05) - 2.1) < 1e-12, "Respect eps."
got = kr(2.0, [-1.0, -0.5], [-1.5, -1.0], 0.5)
assert abs(got - 1.5) < 1e-12, f"2.0 - 0.5 * (0.5 + 0.5) = 1.5, got {got!r}."
