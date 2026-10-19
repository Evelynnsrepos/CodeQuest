func check(enemy) -> String:
	enemy.position = Vector2.ZERO
	if not enemy.can_see(Vector2(120, 160)):
		return "A target exactly 200 pixels away should be visible."
	if enemy.can_see(Vector2(300, 0)):
		return "A target 300 pixels away is out of sight range."

	enemy.chase(Vector2(100, 0), 0.5)
	if not enemy.position.is_equal_approx(Vector2(40, 0)):
		return "chase(Vector2(100, 0), 0.5) should move 40 pixels to (40, 0), but the enemy is at %s." % str(enemy.position)

	enemy.chase(Vector2(100, 0), 1.0)
	if not enemy.position.is_equal_approx(Vector2(100, 0)):
		return "The enemy should stop on the target at (100, 0) instead of overshooting. It's at %s." % str(enemy.position)

	enemy.position = Vector2.ZERO
	enemy.chase(Vector2(0, 500), 1.0)
	if not enemy.position.is_equal_approx(Vector2.ZERO):
		return "The enemy moved towards a target it can't see. It's at %s." % str(enemy.position)
	return ""
