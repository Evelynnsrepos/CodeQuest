import math
cc, hm = ns.get("call_cost"), ns.get("how_many_fit")
assert cc and hm, "Define call_cost and how_many_fit."
got = cc("x" * 2000, 100, 3, 15)
assert math.isclose(got, 0.003), f"2000 characters + 100 reply tokens at $3/$15 should cost 0.003, got {got!r}."
assert math.isclose(cc("abcde", 0, 1e6, 0), 2), "5 characters is 2 tokens (round up)."
assert cc("", 0, 3, 15) == 0, "Nothing in, nothing out: free."
assert math.isclose(cc("abcd", 10, 0, 1e6), 10), "Output tokens use the output price."
p = "x" * 4
# each call costs 1 (1 token at $1e6 per million)
assert hm([p] * 5, 0, 1e6, 0, 3) == 3, "3 calls of $1 fit into a $3 budget."
assert hm([p] * 5, 0, 1e6, 0, 2.5) == 2, "Stop before going over the budget."
assert hm([p] * 2, 0, 1e6, 0, 10) == 2, "If everything fits, return all of them."
assert hm(["x" * 400, p, p], 0, 1e6, 0, 5) == 0, "Stop at the first call that doesn't fit, don't skip ahead."
