func check(s) -> String:
	var cases = [[500.0, 0, "idle"], [200.0, 1, "chase"], [31.0, 1, "chase"], [30.0, 2, "attack"], [0.0, 2, "attack"], [250.0, 0, "idle"]]
	for c in cases:
		s.next_state(c[0])
		if s.state != c[1]:
			return "After next_state(%s) the state is %s, expected %s." % [str(c[0]), str(s.state), ["State.IDLE", "State.CHASE", "State.ATTACK"][c[1]]]
		if s.describe() != c[2]:
			return "At distance %s describe() returned \"%s\", expected \"%s\"." % [str(c[0]), s.describe(), c[2]]
	return ""
