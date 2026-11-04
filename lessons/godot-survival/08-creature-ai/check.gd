func check(w) -> String:
	var names = ["WANDER", "CHASE", "ATTACK", "FLEE"]
	var steps = [[500.0, 0, "far away"], [199.0, 1, "just inside sight_range"], [250.0, 1, "between 200 and 300 (hysteresis: keep chasing)"],
		[25.0, 2, "within attack_range"], [28.0, 2, "still within attack_range"], [60.0, 1, "out of attack_range"],
		[301.0, 0, "beyond sight_range × 1.5"], [250.0, 0, "at 250 while wandering (not yet seen)"]]
	for s in steps:
		w.think(s[0])
		if w.state != s[1]:
			return "At distance %s (%s) the state should be %s, but it's %s." % [str(s[0]), s[2], names[s[1]], names[w.state]]
	w.think(100.0)
	w.think(20.0)
	w.health = 14
	w.think(20.0)
	if w.state != 3:
		return "With health 14 of 50 (below 30%%) the wolf should FLEE, even while attacking. It's %s." % names[w.state]
	w.think(500.0)
	if w.state != 3:
		return "A fleeing wolf should keep fleeing while its health is low."
	w.health = 15
	w.state = 0
	w.think(100.0)
	if w.state != 1:
		return "Health 15 of 50 is exactly 30%, not below, so the wolf shouldn't flee."
	return ""
