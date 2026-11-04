d = ns.get("decide")
assert d, "Keep the function decide."
def g(f, b, p): return {"needs_facts": f, "needs_behaviour": b, "prompt_works": p}
cases = [(g(True, False, False), "rag"), (g(False, True, False), "finetune"), (g(True, True, False), "both"),
         (g(True, True, True), "prompt"), (g(False, True, True), "prompt"), (g(False, False, False), "prompt")]
for goal, want in cases:
    got = d(goal)
    assert got == want, f"decide({goal}) returned {got!r}, expected {want!r}."
