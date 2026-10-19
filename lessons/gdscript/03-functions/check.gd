func check(player) -> String:
	if not player.has_method("take_damage"):
		return "Write a function called take_damage."
	var cases = [[100, 30, 70], [10, 50, 0], [50, 50, 0], [5, 0, 5]]
	for c in cases:
		var got = player.take_damage(c[0], c[1])
		if got != c[2]:
			return "take_damage(%d, %d) returned %s, expected %d." % [c[0], c[1], str(got), c[2]]
	return ""
