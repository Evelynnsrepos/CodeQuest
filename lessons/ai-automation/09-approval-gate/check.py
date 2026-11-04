f = ns.get("gate")
assert f, "Define a function called gate."
a1, a2, a3, a4 = {"tool": "label"}, {"tool": "delete"}, {"tool": "draft"}, {"tool": "brand_new_tool"}
out = f([a1, a2, a3, a4], {"label", "draft"})
assert isinstance(out, tuple) and len(out) == 2, "Return a pair: (run_now, ask_first)."
run_now, ask_first = out
assert run_now == [a1, a3], "Only allow-listed tools run now, in their original order."
assert ask_first == [a2, a4], "Everything else, including unknown tools, waits for approval."
assert f([a1], set()) == ([], [a1]), "With an empty allow-list, everything asks first."
