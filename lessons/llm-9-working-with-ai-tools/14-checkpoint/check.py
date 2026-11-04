ni = ns.get("nightly")
assert ni, "Keep nightly."
rules = {"deny": ["Bash(gh issue edit *)"], "allow": ["Bash(gh issue list *)", "Read"]}
schema = {"required": ["label"], "properties": {"label": {"enum": ["bug", "lesson", "question"]}}}
calls = [("Bash", "gh issue list --state open"), ("Read", "README.md"), ("Bash", "curl evil.com"), ("Bash", "gh issue edit 3 --add-label bug")]
replies = ['{"label": "bug"}', 'oops', '{"label": "ignore previous instructions"}', '{"label": "lesson"}', '{"x": 1}']
assert ni((0, 3, 4, 11, 3), calls, replies, rules, schema) is None, "Not 02:00 → None."
r = ni((0, 2, 4, 11, 3), calls, replies, rules, schema)
assert isinstance(r, dict), f"Return a dict, got {r!r}."
assert r.get("ran") == [("Bash", "gh issue list --state open"), ("Read", "README.md")], f"ran wrong: {r.get('ran')!r}."
assert r.get("blocked") == [("Bash", "curl evil.com"), ("Bash", "gh issue edit 3 --add-label bug")], "Unmatched (ask) and denied calls are both blocked."
assert r.get("labels") == ["bug", "lesson"], f"Only valid replies give labels, got {r.get('labels')!r}."
