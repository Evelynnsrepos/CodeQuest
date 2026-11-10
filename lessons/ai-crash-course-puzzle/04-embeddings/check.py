d, ln, co, cl = ns.get("dot"), ns.get("length"), ns.get("cosine"), ns.get("closest")
assert d and ln and co and cl, "Keep dot, length, cosine and closest."
assert d([3, 4], [4, 3]) == 24 and d([1, 2, 3], [4, 5, 6]) == 32, f"dot([3, 4], [4, 3]) = 3×4 + 4×3 = 24, yours gave {d([3, 4], [4, 3])!r}."
assert abs(ln([3, 4]) - 5) < 1e-9 and abs(ln([2, 3, 6]) - 7) < 1e-9, f"length([3, 4]) = √(9 + 16) = 5, yours gave {ln([3, 4])!r}."
assert abs(co([3, 4], [4, 3]) - 0.96) < 1e-9 and abs(co([1, 2], [2, 4]) - 1) < 1e-9, "cosine: dot ÷ (length × length). cos([3,4],[4,3]) = 24/25 = 0.96."
assert abs(co([1, 0], [0, 3])) < 1e-9 and abs(co([1, 1], [-2, -2]) + 1) < 1e-9, "cosine: 0 for a right angle, −1 for opposite."
animals = {"kitten": [0.9, 0.8, 0.1], "car": [0.1, 0.0, 0.95], "puppy": [0.8, 0.9, 0.0]}
assert cl([0.95, 0.75, 0.05], animals) == "kitten" and cl([0, 0.1, 1], animals) == "car", "closest: the name with the highest cosine."
assert cl([-1, 0], {"right": [1, 0], "up_right": [1, 1]}) == "up_right", "closest must also work when every cosine is low or negative (start best_score at -2)."
