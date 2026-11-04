func check(g) -> String:
	for i in 99:
		g.collect_coin()
	if g.coins != 99 or g.lives != 3:
		return "After 99 coins expected 99 coins and 3 lives, got %d and %d." % [g.coins, g.lives]
	g.collect_coin()
	if g.coins != 0 or g.lives != 4:
		return "The 100th coin should give an extra life and reset coins to 0. Got %d coins and %d lives." % [g.coins, g.lives]
	var a = g.next_level()
	var b = g.next_level()
	var c = g.next_level()
	if a != "res://levels/level_2.tscn" or b != "res://levels/level_3.tscn":
		return "From level 1, next_level() should return level_2, then level_3. Got %s and %s." % [a, b]
	if c != "res://win_screen.tscn":
		return "After the last level next_level() should return \"res://win_screen.tscn\", got \"%s\"." % str(c)
	return ""
