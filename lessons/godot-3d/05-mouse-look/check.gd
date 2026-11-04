func motion(x: float, y: float) -> InputEventMouseMotion:
	var e := InputEventMouseMotion.new()
	e.relative = Vector2(x, y)
	return e


func check(p) -> String:
	p._unhandled_input(motion(100, 0))
	if not is_equal_approx(p.rotation.y, -0.3):
		return "Moving the mouse 100 px right should turn the body to rotation.y = -0.3 (to the right), got %.3f." % p.rotation.y
	if not is_equal_approx(p.head.rotation.x, 0.0):
		return "Moving the mouse sideways shouldn't tilt the head."
	p._unhandled_input(motion(0, 100))
	if not is_equal_approx(p.head.rotation.x, -0.3):
		return "Moving the mouse 100 px down should tilt the head to rotation.x = -0.3 (looking down), got %.3f." % p.head.rotation.x
	if not is_equal_approx(p.rotation.x, 0.0):
		return "Only the head should tilt, not the whole body."
	p._unhandled_input(motion(0, -5000))
	if not is_equal_approx(p.head.rotation.x, deg_to_rad(89)):
		return "Looking far up should stop at 89° (%.3f rad), got %.3f." % [deg_to_rad(89), p.head.rotation.x]
	p._unhandled_input(motion(0, 9000))
	if not is_equal_approx(p.head.rotation.x, deg_to_rad(-89)):
		return "Looking far down should stop at -89°, got %.3f." % p.head.rotation.x
	var key := InputEventKey.new()
	p._unhandled_input(key)
	return ""
