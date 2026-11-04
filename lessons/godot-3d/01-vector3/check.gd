func check(s) -> String:
	var d = s.ground_distance(Vector3.ZERO, Vector3(3, 10, 4))
	if not is_equal_approx(d, 5.0):
		return "ground_distance((0, 0, 0), (3, 10, 4)) should be 5 (height ignored), got %s." % str(d)
	d = s.ground_distance(Vector3(1, 2, 1), Vector3(1, -7, -5))
	if not is_equal_approx(d, 6.0):
		return "ground_distance((1, 2, 1), (1, -7, -5)) should be 6, got %s." % str(d)
	var dir = s.ground_direction(Vector3(1, 0, 1), Vector3(4, 8, 5))
	if not dir.is_equal_approx(Vector3(0.6, 0, 0.8)):
		return "ground_direction((1, 0, 1), (4, 8, 5)) should be (0.6, 0, 0.8), got %s." % str(dir)
	return ""
