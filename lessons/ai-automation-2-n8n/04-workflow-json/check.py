f = ns.get("run_order")
assert f, "Define a function called run_order."
c = lambda *names: [{"node": n, "type": "main", "index": 0} for n in names]
wf = {"connections": {"T": {"main": [c("A")]}, "A": {"main": [c("B", "C")]}, "B": {"main": [c("D")]}}}
assert f(wf, "T") == ["T", "A", "B", "C", "D"], f"Breadth-first order, got {f(wf, 'T')!r}."
iff = {"connections": {"T": {"main": [c("If")]}, "If": {"main": [c("Yes"), c("No")]}}}
assert f(iff, "T") == ["T", "If", "Yes", "No"], "Follow every output, like the IF node's true and false outputs."
merge = {"connections": {"T": {"main": [c("A", "B")]}, "A": {"main": [c("M")]}, "B": {"main": [c("M")]}}}
assert f(merge, "T") == ["T", "A", "B", "M"], "A node reached twice appears once."
assert f({"connections": {}}, "Alone") == ["Alone"], "A node without connections is just itself."
