func check(player) -> String:
	if not player.has_method("count_big"):
		return "Write a function called count_big."
	var cases = [[[3, 7, 2, 10], 5, 2], [[], 1, 0], [[1, 1, 1], 1, 3], [[4, 9], 10, 0]]
	for c in cases:
		var got = player.count_big(c[0], c[1])
		if got != c[2]:
			return "count_big(%s, %d) returned %s, expected %d." % [str(c[0]), c[1], str(got), c[2]]
	return ""
