import math
import random
sm, se, nn = ns.get("simulate_mean"), ns.get("standard_error"), ns.get("n_needed")
assert sm and se and nn, "Keep simulate_mean, standard_error and n_needed."
rng = random.Random(7)
want = sum(rng.randint(1, 6) for _ in range(50)) / 50
assert sm(7, 50) == want, f"Use random.Random(seed).randint(1, 6): simulate_mean(7, 50) should be {want}, got {sm(7, 50)!r}."
assert abs(sm(3, 20000) - 3.5) < 0.05, "With 20000 rolls the average should be close to 3.5."
assert abs(se(1.71, 100) - 0.171) < 1e-12, f"standard_error(1.71, 100) = 0.171, got {se(1.71, 100)!r}."
assert abs(se(2, 400) - 0.1) < 1e-12, "σ / √n: 2 / 20."
assert nn(1.71, 0.05) == 1170, f"(1.71 / 0.05)² = 1169.64 → round up to 1170, got {nn(1.71, 0.05)!r}."
assert nn(2, 0.1) == 400, "Exactly 400 is enough for SE 0.1 with σ = 2."
assert se(2, nn(3, 0.07)) <= se(2, nn(3, 0.07)) and 3 / math.sqrt(nn(3, 0.07)) <= 0.07 + 1e-12, "n_needed must make SE ≤ target."
