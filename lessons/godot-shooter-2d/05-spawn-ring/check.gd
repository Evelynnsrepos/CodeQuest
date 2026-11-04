func check(s) -> String:
	var pts = s.ring_points(Vector2(10, 10), 100, 4)
	var want = [Vector2(110, 10), Vector2(10, 110), Vector2(-90, 10), Vector2(10, -90)]
	if pts.size() != 4:
		return "ring_points(..., 4) should return 4 points, got %d." % pts.size()
	for i in 4:
		if not pts[i].is_equal_approx(want[i]):
			return "ring_points(Vector2(10, 10), 100, 4): point %d is %s, expected %s." % [i, str(pts[i]), str(want[i])]
	if s.ring_points(Vector2.ZERO, 50, 3).size() != 3:
		return "ring_points with count 3 should return 3 points."
	var seen := {}
	for i in 20:
		var p: Vector2 = s.random_point(Vector2(5, 5), 300)
		if absf(p.distance_to(Vector2(5, 5)) - 300) > 0.01:
			return "random_point(Vector2(5, 5), 300) returned %s, which isn't 300 away from the center." % str(p)
		seen[p.snapped(Vector2(1, 1))] = true
	if seen.size() < 10:
		return "random_point keeps returning the same few points. Use randf() * TAU for the angle."
	return ""
