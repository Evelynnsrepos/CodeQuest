bp = ns.get("build_prompt")
assert bp, "Keep build_prompt."
p = bp("Summarize.", "For a beginner.", ["doc one", "doc two"], [("in1", "out1")], "Only bullets.")
want = '<documents>\n<document index="1">doc one</document>\n<document index="2">doc two</document>\n</documents>\n<examples>\n<example><input>in1</input><output>out1</output></example>\n</examples>\n<instructions>Summarize. For a beginner.</instructions>\nOnly bullets.'
assert p == want, f"Prompt layout differs. Got:\n{p}"
p = bp("T.", "W.", ["d"], [], "F.")
assert "<examples>" not in p and p.index("<documents>") < p.index("<instructions>") and p.endswith("F."), "No examples block when empty; documents first; format last."
