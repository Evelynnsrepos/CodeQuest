func hold(player, action: String, seconds: float) -> void:
	Input.action_press(action)
	player._process(seconds)
	Input.action_release(action)


func check(player) -> String:
	player.position = Vector2(500, 300)
	hold(player, "ui_right", 0.5)
	if not player.position.is_equal_approx(Vector2(650, 300)):
		return "Holding right for 0.5 s from (500, 300) should reach (650, 300), but the player is at %s." % str(player.position)

	player.position = Vector2(50, 300)
	hold(player, "ui_left", 1.0)
	if not player.position.is_equal_approx(Vector2(0, 300)):
		return "Walking left from x = 50 should stop at the left edge (0, 300), but the player is at %s." % str(player.position)

	player.position = Vector2(1100, 600)
	hold(player, "ui_right", 1.0)
	hold(player, "ui_down", 1.0)
	if not player.position.is_equal_approx(Vector2(1152, 648)):
		return "Walking right and down should stop at the bottom-right corner (1152, 648), but the player is at %s." % str(player.position)

	player.position = Vector2(300, 20)
	hold(player, "ui_up", 1.0)
	if not player.position.is_equal_approx(Vector2(300, 0)):
		return "Walking up from y = 20 should stop at the top edge (300, 0), but the player is at %s." % str(player.position)
	return ""
