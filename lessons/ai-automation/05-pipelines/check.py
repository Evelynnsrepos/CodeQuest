f = ns.get("run_pipeline")
assert f, "Define a function called run_pipeline."
def add_one(x): return x + 1
def double(x): return x * 2
def nothing(x): return None
assert f(3, [add_one, double]) == 8, "Run the steps in order: (3 + 1) * 2 = 8."
assert f(3, [double, add_one]) == 7, "Order matters: 3 * 2 + 1 = 7."
assert f("same", []) == "same", "No steps: return the value unchanged."
ran = []
def later(x):
    ran.append(x)
    return x
try:
    f(1, [add_one, nothing, later])
except RuntimeError as e:
    assert str(e) == "step nothing gave nothing", f"Say which step: got {str(e)!r}."
else:
    raise AssertionError("A step returning None should raise RuntimeError.")
assert ran == [], "Stop at the step that gave nothing; don't run the next ones."
assert f(0, [lambda x: 0]) == 0, "0 is a real value, only None means 'nothing'. Use 'is None'."
