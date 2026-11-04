f = ns.get("changed_files")
assert f, "Define a function called changed_files."
assert f({"a": 1}, {"a": 1, "b": 5}) == ["b"], "New files count."
assert f({"a": 1}, {"a": 2}) == ["a"], "Files with a different mtime count."
assert f({"a": 1, "b": 2}, {"a": 1, "b": 2}) == [], "Nothing changed: empty list."
assert f({"a": 1, "gone": 3}, {"a": 1}) == [], "Deleted files are ignored."
assert f({}, {"z": 1, "m": 1, "a": 1}) == ["a", "m", "z"], "Return the names sorted."
