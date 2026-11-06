ra = ns.get("run_agent")
assert ra, "Keep run_agent."
m = lambda h: {"tool": "add", "args": {"a": 2, "b": 3}} if not h else {"answer": str(h[-1][1])}
assert ra(m, {"add": lambda args: args["a"] + args["b"]}) == "5", "Call the tool with action['args'], then the model answers with its result: should give '5'."
calls = []
def counter(h):
    calls.append(1)
    return {"tool": "noop", "args": {}}
assert ra(counter, {"noop": lambda args: None}, max_steps=3) == "gave up" and len(calls) == 3, "Stop after max_steps and give back 'gave up' (after the loop, at 4 spaces)."
two = lambda h: {"tool": "t", "args": {"x": len(h)}} if len(h) < 2 else {"answer": repr(h)}
assert ra(two, {"t": lambda args: args["x"] * 10}) == "[('t', 0), ('t', 10)]", "history holds (name, result) pairs: history.append((action['tool'], result))."
