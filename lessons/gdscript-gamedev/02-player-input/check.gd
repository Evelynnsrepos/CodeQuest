func check(player) -> String:
	player.position = Vector2.ZERO
	Input.action_press("ui_right")
	player._process(0.5)
	Input.action_release("ui_right")
	if not player.position.is_equal_approx(Vector2(150, 0)):
		return "Holding right for 0.5 s moved the player to %s, expected (150, 0)." % str(player.position)

	player.position = Vector2.ZERO
	player._process(0.5)
	if not player.position.is_equal_approx(Vector2.ZERO):
		return "The player moved with no keys held. It ended at %s." % str(player.position)

	Input.action_press("ui_up")
	Input.action_press("ui_left")
	player._process(0.5)
	Input.action_release("ui_up")
	Input.action_release("ui_left")
	var moved: Vector2 = player.position
	if moved.x >= 0 or moved.y >= 0:
		return "Holding up and left should move up and to the left, but the player ended at %s." % str(moved)
	if absf(moved.length() - 150.0) > 0.5:
		return "Diagonal movement went %.1f pixels, expected 150. Is the direction normalized?" % moved.length()
	return ""
