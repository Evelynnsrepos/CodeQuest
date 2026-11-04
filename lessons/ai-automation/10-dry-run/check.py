f = ns.get("execute")
assert f, "Define a function called execute."
calls = []
tools = {"rename": lambda old, new: calls.append(("rename", old, new)), "tag": lambda n: calls.append(("tag", n))}
acts = [{"tool": "rename", "args": {"old": "a.jpg", "new": "b.jpg"}}, {"tool": "tag", "args": {"n": 5}}]
log = f(acts, tools)
assert log == ["DRY rename(old='a.jpg', new='b.jpg')", "DRY tag(n=5)"], f"Dry-run log lines are wrong: {log!r}."
assert calls == [], "A dry run (the default) must not call any tool."
log = f(acts, tools, dry_run=False)
assert log == ["RAN rename(old='a.jpg', new='b.jpg')", "RAN tag(n=5)"], f"Real-run log lines are wrong: {log!r}."
assert calls == [("rename", "a.jpg", "b.jpg"), ("tag", 5)], "With dry_run=False, call each tool with its args."
assert f([{"tool": "tag", "args": {}}], tools) == ["DRY tag()"], "No args: empty brackets."
