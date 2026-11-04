func check(p) -> String:
	p.set_process(false)
	p.position = Vector2(100, 100)
	var cases = [[Vector2(200, 100), 0.0, "right"], [Vector2(100, 300), PI / 2, "straight down"],
		[Vector2(100, 0), -PI / 2, "straight up"], [Vector2(200, 200), PI / 4, "down-right"]]
	for c in cases:
		p.rotation = 1.0
		p.aim_at(c[0])
		if absf(angle_difference(p.rotation, c[1])) > 0.001:
			return "Standing at (100, 100) and aiming at %s (%s), rotation should be %.3f but it's %.3f." % [str(c[0]), c[2], c[1], p.rotation]
	p.position = Vector2(-50, 20)
	p.aim_at(Vector2(-50, 120))
	if absf(angle_difference(p.rotation, PI / 2)) > 0.001:
		return "Aiming from (-50, 20) at (-50, 120) should point down (PI / 2). Subtract your own position from the target."
	return ""
