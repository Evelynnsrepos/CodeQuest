func check(s) -> String:
	s.set_process(false)
	s._process(10.0)
	if not is_equal_approx(s.hunger, 90.0) or not is_equal_approx(s.thirst, 80.0):
		return "After 10 seconds hunger should be 90 and thirst 80, got %s and %s." % [str(s.hunger), str(s.thirst)]
	if not is_equal_approx(s.health, 100.0):
		return "Health shouldn't drop while hunger and thirst are above 0."
	s._process(45.0)
	if s.thirst != 0:
		return "Thirst should stop at 0, but it's %s." % str(s.thirst)
	s.health = 100.0
	s._process(2.0)
	if not is_equal_approx(s.health, 90.0):
		return "With thirst at 0, 2 seconds should cost 10 health (5 per second). Health is %s." % str(s.health)
	s.hunger = 0
	s.health = 100.0
	s._process(1.0)
	if not is_equal_approx(s.health, 95.0):
		return "With both hunger and thirst at 0, damage should still be 5 per second, not double. Health is %s." % str(s.health)
	s.hunger = 70
	s.eat(50)
	if s.hunger != 100:
		return "eat(50) at 70 hunger should fill up to 100, not %s." % str(s.hunger)
	return ""
