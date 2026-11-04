func check(g) -> String:
	var cases = [[1, 2.0], [2, 1.7], [3, 1.445], [10, 2.0 * pow(0.85, 9)], [30, 0.4]]
	for c in cases:
		var got = g.spawn_interval(c[0])
		if absf(got - c[1]) > 0.001:
			return "spawn_interval(%d) should be %.3f, got %s." % [c[0], c[1], str(got)]
	if not g.game_over(500) or g.high_score != 500:
		return "A first game with 500 points is a new high score: return true and store it."
	if g.game_over(300) or g.high_score != 500:
		return "300 doesn't beat 500: return false and keep the high score."
	if g.game_over(500):
		return "500 only ties the high score, it doesn't beat it."
	return ""
