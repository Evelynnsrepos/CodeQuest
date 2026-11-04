f = ns.get("next_course")
assert f, "Keep the function next_course."
R = ns["ROADMAP"]
assert f(set()) == R[0], f"With nothing done, next_course should return {R[0]!r}, got {f(set())!r}."
assert f({R[0], R[1]}) == R[2], f"After the first two courses, next_course should return {R[2]!r}."
assert f({R[0], R[2]}) == R[1], "Return the first unfinished course, even if a later one is done."
assert f(set(R)) == "all done", "When every course is done, return 'all done'."
assert isinstance(ns.get("my_done"), set), "Keep my_done as a set (it may be empty)."
