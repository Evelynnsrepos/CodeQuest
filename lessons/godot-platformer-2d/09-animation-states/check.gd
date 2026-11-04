func check(p) -> String:
	var cases = [[Vector2(0, 0), true, "idle"], [Vector2(120, 0), true, "run"], [Vector2(-120, 0), true, "run"],
		[Vector2(0, -300), false, "jump"], [Vector2(100, -10), false, "jump"], [Vector2(0, 200), false, "fall"], [Vector2(-50, 5), false, "fall"]]
	for c in cases:
		p.velocity = c[0]
		var got = p.pick_animation(c[1])
		if got != c[2]:
			return "With velocity %s and on_floor %s, pick_animation returned \"%s\", expected \"%s\"." % [str(c[0]), str(c[1]), str(got), c[2]]
	p.velocity = Vector2(-100, 0)
	p.update_facing()
	if not p.facing_left:
		return "Moving left (velocity.x -100) should set facing_left to true."
	p.velocity = Vector2.ZERO
	p.update_facing()
	if not p.facing_left:
		return "Standing still should keep facing the same way (still left)."
	p.velocity = Vector2(80, 0)
	p.update_facing()
	if p.facing_left:
		return "Moving right should set facing_left to false."
	return ""
