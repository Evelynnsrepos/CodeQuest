m, d, e = ns.get("matches"), ns.get("decide"), ns.get("effective")
assert m and d and e, "Keep matches, decide and effective."
assert m("Bash(ls *)", "Bash", "ls -la") and m("Bash(ls *)", "Bash", "ls"), "Bash(ls *) matches 'ls -la' and 'ls'."
assert not m("Bash(ls *)", "Bash", "lsof"), "Bash(ls *) must NOT match 'lsof' (the space matters)."
assert m("Bash(ls*)", "Bash", "lsof"), "Bash(ls*) matches 'lsof'."
assert m("Bash(git diff:*)", "Bash", "git diff HEAD") and not m("Bash(git diff:*)", "Bash", "git diffx"), ":* works like ' *'."
assert m("Read(./.env)", "Read", "./.env") and not m("Read(./.env)", "Read", "./.env.local"), "No * → exact."
assert m("WebSearch", "WebSearch", "anything") and not m("Bash(ls *)", "Read", "ls"), "Bare tool name; tool must match."
rules = {"deny": ["Bash(git push *)"], "allow": ["Bash(git *)"]}
assert d("Bash", "git status", rules) == "allow" and d("Bash", "git push origin main", rules) == "deny", "deny is checked before allow."
assert d("Bash", "npm install", rules) == "ask", "No match → ask."
assert d("Bash", "aws s3 ls", {"deny": ["Bash(aws *)"], "allow": ["Bash(aws s3 ls)"]}) == "deny", "An allow can't carve an exception out of a deny."
assert d("Bash", "npm test", {"ask": ["Bash(npm *)"], "allow": ["Bash(npm test)"]}) == "ask", "ask beats allow."
layers = {"user": {"model": "a", "theme": "dark"}, "project": {"model": "b"}, "local": {"model": "c"}}
assert e("model", layers) == "c" and e("theme", layers) == "dark" and e("nope", layers) is None, "Highest layer that sets the key wins."
assert e("model", dict(layers, managed={"model": "m"}, cli={"model": "x"})) == "m", "Managed beats everything."
