L, S = ns.get("Linear"), ns.get("Sequential")
assert L and S, "Keep the classes Linear and Sequential."
l = L([[2, 0, 1], [0, 1, 0]], [1, -1])
assert l([1, 2, 3]) == [6, 1], f"Linear([[2, 0, 1], [0, 1, 0]], [1, -1])([1, 2, 3]) returned {l([1, 2, 3])!r}, expected [6, 1]."
assert l.num_params() == 8, f"num_params() returned {l.num_params()!r}, expected 6 weights + 2 biases = 8."
m = S([L([[1, 1]], [0]), L([[3]], [1])])
assert m([2, 5]) == [22], f"Sequential of two layers returned {m([2, 5])!r} for [2, 5], expected [3 × 7 + 1] = [22]."
assert S([])([4]) == [4], "A Sequential with no layers should return its input unchanged."
