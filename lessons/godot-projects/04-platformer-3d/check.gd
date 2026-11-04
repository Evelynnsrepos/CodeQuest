func check(p) -> String:
	p.set_physics_process(false)
	p.sync_to_physics = false    # read position straight back instead of waiting for the physics step
	p.time = 0.0
	p.start = Vector3(0, 2, 0)
	var cases = [[1.0, Vector3(3, 2, 0)], [1.0, Vector3(0, 2, 0)], [1.0, Vector3(-3, 2, 0)], [0.5, Vector3(-3 * sin(PI / 4), 2, 0)]]
	var t := 0.0
	for c in cases:
		p._physics_process(c[0])
		t += c[0]
		if not p.position.is_equal_approx(c[1]):
			return "At time %.1f s the platform should be at %s, but it's at %s." % [t, str(c[1]), str(p.position)]
	p.axis = Vector3(0, 1, 0)
	p.time = 0.0
	p._physics_process(1.0)
	if not p.position.is_equal_approx(Vector3(0, 5, 0)):
		return "With axis (0, 1, 0) the platform should move up and down: expected (0, 5, 0) after 1 s, got %s." % str(p.position)
	return ""
