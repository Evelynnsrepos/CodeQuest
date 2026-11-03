acc, reg = ns.get("accuracy"), ns.get("regressed")
assert acc and reg, "Keep accuracy and regressed."
cases = [{"expect": {"name": "f", "args": {"x": 1}}}, {"expect": None}, {"expect": {"name": "g", "args": {}}}, {"expect": None}]
replies = [{"tool": {"name": "f", "args": {"x": 1}}}, {"tool": {"name": "f", "args": {"x": 1}}},
           {"tool": {"name": "g", "args": {"y": 2}}}, {"tool": None}]
got = acc(cases, replies)
assert abs(got - 0.5) < 1e-9, f"accuracy should be 0.5 (calling a tool when none is expected, or wrong args, is wrong), got {got!r}."
assert reg(0.9, 0.8) is True, "0.9 -> 0.8 is a drop of 0.1 > 0.05, so regressed should be True."
assert reg(0.9, 0.87) is False, "A drop of 0.03 is within tolerance: regressed should be False."
assert reg(0.8, 0.9) is False, "Getting better is not a regression."
assert reg(0.9, 0.85, tolerance=0.01) is True, "Respect the tolerance argument."
