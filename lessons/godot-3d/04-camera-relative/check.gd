func check(p) -> String:
	var cases = [[Vector2(0, -1), 0.0, Vector3(0, 0, -1)], [Vector2(0, -1), PI / 2, Vector3(-1, 0, 0)],
		[Vector2(1, 0), PI / 2, Vector3(0, 0, -1)], [Vector2(0, 1), PI, Vector3(0, 0, -1)]]
	for c in cases:
		var got = p.move_direction(c[0], c[1])
		if not got.is_equal_approx(c[2]):
			return "move_direction(%s, %.2f) returned %s, expected %s." % [str(c[0]), c[1], str(got), str(c[2])]
	p.position = Vector3(2, 0, 3)
	p.face(Vector3(1, 0, 0))
	var fwd: Vector3 = -p.global_transform.basis.z
	if not fwd.is_equal_approx(Vector3(1, 0, 0)):
		return "After face(Vector3(1, 0, 0)) the player's forward should point along +x, but it points %s." % str(fwd)
	p.face(Vector3.ZERO)
	fwd = -p.global_transform.basis.z
	if not fwd.is_equal_approx(Vector3(1, 0, 0)):
		return "face(Vector3.ZERO) should leave the player facing the same way."
	return ""
