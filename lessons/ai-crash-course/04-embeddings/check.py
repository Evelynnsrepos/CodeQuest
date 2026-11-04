co, cl = ns.get("cosine"), ns.get("closest")
assert co and cl, "Keep cosine and closest."
assert abs(co([1, 2], [2, 4]) - 1) < 1e-9 and abs(co([1, 0], [0, 3])) < 1e-9 and abs(co([1, 1], [-2, -2]) + 1) < 1e-9, "cosine: 1, 0 and −1 for same, perpendicular and opposite."
assert abs(co([3, 4], [4, 3]) - 0.96) < 1e-9, "cos([3,4],[4,3]) = 24/25."
animals = {"kitten": [0.9, 0.8, 0.1], "car": [0.1, 0.0, 0.95], "puppy": [0.8, 0.9, 0.0]}
assert cl([0.95, 0.75, 0.05], animals) == "kitten" and cl([0, 0.1, 1], animals) == "car", "closest: highest cosine."
