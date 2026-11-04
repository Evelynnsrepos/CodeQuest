ra, fs = ns.get("run_agent"), ns.get("failure_summary")
assert ra and fs, "Keep run_agent and failure_summary."
def m1(task, trace):
    return {"tool": "search", "args": {"q": task}} if not trace else {"answer": "done"}
ans, tr = ra("t", m1, {"search": lambda q: [q]})
assert ans == "done" and len(tr) == 2, f"One tool span and one answer span. Got {tr!r}."
s = tr[0]
assert (s["step"], s["type"], s["name"], s["args"], s["result"], s["error"]) == (1, "tool", "search", {"q": "t"}, ["t"], None), f"Tool span fields. Got {s!r}."
assert isinstance(s["ms"], float) and s["ms"] >= 0, "ms: elapsed milliseconds as a float."
assert tr[1] == {"step": 2, "type": "answer", "name": None, "args": None, "result": "done", "error": None, "ms": 0.0}, f"Answer span. Got {tr[1]!r}."
def boom(q):
    raise ValueError("index offline")
def m2(task, trace):
    if len(trace) == 0: return {"tool": "search", "args": {"q": task}}
    if len(trace) == 1: return {"tool": "browse", "args": {}}
    return {"answer": "gave up nicely"}
ans, tr = ra("t", m2, {"search": boom})
assert tr[0]["error"] == "ValueError: index offline" and tr[0]["result"] is None, f"Record tool errors and keep going. Got {tr[0]!r}."
assert tr[1]["error"] == "KeyError: browse", f"Unknown tool → 'KeyError: browse'. Got {tr[1]['error']!r}."
assert ans == "gave up nicely", "The loop continues after errors."
loop = lambda task, trace: {"tool": "search", "args": {"q": "again"}}
ans, tr = ra("t", loop, {"search": boom}, max_steps=3)
assert ans is None and len(tr) == 3, "Stop after max_steps model calls and return None."
summary = fs([("ok", []), (None, tr), ra("t", m2, {"search": boom})])
assert summary == {"runs": 3, "no_answer": 1, "tool_errors": {"search": 4, "browse": 1}}, f"Got {summary!r}."
