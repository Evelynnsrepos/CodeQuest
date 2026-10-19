func check(gun) -> String:
	if not gun.try_shoot():
		return "The first shot should work."
	if gun.try_shoot():
		return "A second shot straight away should be blocked by the cooldown."
	gun._process(0.3)
	if gun.try_shoot():
		return "After 0.3 s the 0.5 s cooldown is still running, so try_shoot() should return false."
	gun._process(0.3)
	if not gun.try_shoot():
		return "After 0.6 s in total the cooldown is over, so try_shoot() should return true."
	if gun.try_shoot():
		return "Shooting should start the cooldown again."
	return ""
