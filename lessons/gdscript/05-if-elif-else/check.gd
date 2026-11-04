func check(s) -> String:
	var cases = [["fire", "ice", 2.0], ["water", "fire", 2.0], ["fire", "fire", 0.5],
		["ice", "ice", 0.5], ["ice", "fire", 1.0], ["fire", "water", 1.0], ["water", "ice", 1.0]]
	for c in cases:
		var got = s.damage_multiplier(c[0], c[1])
		if not is_equal_approx(float(got), c[2]):
			return "damage_multiplier(\"%s\", \"%s\") returned %s, expected %s." % [c[0], c[1], str(got), str(c[2])]
	return ""
