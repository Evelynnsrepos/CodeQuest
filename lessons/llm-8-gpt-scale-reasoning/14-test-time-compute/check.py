import math
mv, pk = ns.get("majority_vote"), ns.get("pass_at_k")
assert mv and pk, "Keep majority_vote and pass_at_k."
assert mv(["b", "a", "a"]) == "a", "['b', 'a', 'a'] has 'a' twice."
assert mv(["x", "y", "y", "x", "z"]) == "x", "On a tie, return the answer that appeared first."
assert abs(pk(10, 3, 1) - 0.3) < 1e-12, f"pass@1 should equal c/n = 0.3, got {pk(10, 3, 1)!r}."
want = 1 - math.comb(7, 5) / math.comb(10, 5)
assert abs(pk(10, 3, 5) - want) < 1e-12, f"pass_at_k(10, 3, 5) should be {want:.4f}, got {pk(10, 3, 5)!r}."
assert pk(10, 8, 5) == 1.0, "With only 2 wrong samples, every 5 contain a correct one: 1.0."
assert pk(10, 0, 5) == 0.0, "No correct samples: 0.0."
