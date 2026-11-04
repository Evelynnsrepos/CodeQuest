pl, PICK = ns.get("plan"), ns.get("PICK")
assert pl, "Keep plan."
assert pl(30, 14) == 10 and pl(20, 14) == 14 and pl(60, 1) == 1, "plan: lessons × minutes ÷ minutes per day, rounded up."
assert pl(45, 10, minutes_per_lesson=30) == 7, "Use minutes_per_lesson."
assert isinstance(PICK, str) and PICK.strip(), "Write the course you'll do next in PICK."
