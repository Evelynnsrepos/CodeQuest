func check(player) -> String:
	if not "health" in player:
		return "Keep the health variable at the top of the script."
	if player.health != 75:
		return "health should be 75, but it's %s." % str(player.health)
	return ""
