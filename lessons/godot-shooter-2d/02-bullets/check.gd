func check(b) -> String:
	b.set_physics_process(false)
	b.position = Vector2.ZERO
	b.rotation = 0
	b._physics_process(0.5)
	if not b.position.is_equal_approx(Vector2(300, 0)):
		return "A bullet with rotation 0 should move right 300 px in 0.5 s, but it's at %s." % str(b.position)
	b.position = Vector2.ZERO
	b.rotation = PI / 2
	b._physics_process(0.1)
	if not b.position.is_equal_approx(Vector2(0, 60)):
		return "A bullet with rotation PI / 2 should move straight down 60 px in 0.1 s, but it's at %s." % str(b.position)
	b.position = Vector2.ZERO
	b.rotation = PI / 4
	b._physics_process(0.1)
	if absf(b.position.length() - 60) > 0.01:
		return "A diagonal bullet moved %.1f px in 0.1 s, expected 60." % b.position.length()
	if b.is_queued_for_deletion():
		return "The bullet was removed after 0.7 s, but its lifetime is 1 s."
	b._physics_process(0.3)
	if not b.is_queued_for_deletion():
		return "After 1 s in total the bullet should remove itself with queue_free()."
	return ""
