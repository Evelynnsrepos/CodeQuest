c, p = ns.get("compose"), ns.get("pipeline")
assert c and p, "Keep compose and pipeline."
sq, p3 = (lambda x: x * x), (lambda x: x + 3)
h = c(sq, p3)
assert callable(h), "compose should return a function."
assert h(2) == 25 and c(p3, sq)(2) == 7, f"compose(square, plus3)(2) should be square(plus3(2)) = 25, got {h(2)!r}."
assert p([p3, sq], 2) == 25 and p([sq, p3], 2) == 7, "pipeline applies fs[0] first."
assert p([], 5) == 5, "An empty pipeline returns x unchanged."
