import math
ir, dl, ra = ns.get("implicit_reward"), ns.get("dpo_loss"), ns.get("reward_accuracy")
assert ir and dl and ra, "Keep implicit_reward, dpo_loss and reward_accuracy."
assert abs(ir(-10.0, -12.0, 0.5) - 1.0) < 1e-12, f"implicit_reward(-10, -12, 0.5) returned {ir(-10.0, -12.0, 0.5)!r}, expected 0.5 × 2 = 1."
assert abs(dl(-5.0, -5.0, -5.0, -5.0, 0.1) - math.log(2)) < 1e-12, "When policy equals reference, the margin is 0 and the loss is log 2."
got = dl(-30.0, -50.0, -40.0, -40.0, 0.1)
want = math.log(1 + math.exp(-(0.1 * 10 - 0.1 * -10)))
assert abs(got - want) < 1e-12, f"dpo_loss(-30, -50, -40, -40, 0.1) returned {got!r}, expected {want:.6f} (margin 2)."
assert dl(-50.0, -30.0, -40.0, -40.0, 0.1) > math.log(2), "Preferring the rejected answer should give a loss above log 2."
assert ra([(-1.0, -9.0, -5.0, -5.0), (-9.0, -1.0, -5.0, -5.0), (-5.0, -5.0, -5.0, -5.0), (-2.0, -9.0, -5.0, -5.0)], 0.1) == 0.5, "reward_accuracy counts only strict wins: 2 of these 4."
