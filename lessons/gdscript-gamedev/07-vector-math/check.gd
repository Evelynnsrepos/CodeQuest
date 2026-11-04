func check(p) -> String:
	p.position = Vector2(100, 0)
	p.knockback(Vector2.ZERO, 50)
	if not p.position.is_equal_approx(Vector2(150, 0)):
		return "Player at (100, 0), enemy at (0, 0), strength 50: expected (150, 0), got %s." % str(p.position)
	p.position = Vector2(0, 0)
	p.knockback(Vector2(30, 40), 10)
	if not p.position.is_equal_approx(Vector2(-6, -8)):
		if p.position.is_equal_approx(Vector2(6, 8)):
			return "The player was pulled towards the enemy. Subtract the other way round: player minus enemy."
		return "Player at (0, 0), enemy at (30, 40), strength 10: expected (-6, -8), got %s. Did you normalize?" % str(p.position)
	return ""
