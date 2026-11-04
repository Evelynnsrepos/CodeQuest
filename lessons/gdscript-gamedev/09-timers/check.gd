func check(s) -> String:
	var timer = s.get_node_or_null("SpawnTimer")
	if timer == null or not timer is Timer:
		return "Add a Timer child named \"SpawnTimer\" in _ready()."
	if not is_equal_approx(timer.wait_time, 0.2):
		return "The timer's wait_time is %s, expected spawn_every (0.2)." % str(timer.wait_time)
	if timer.one_shot:
		return "The timer should repeat, so leave one_shot false."
	if timer.is_stopped():
		return "The timer isn't running. Call start() (or set autostart before adding it)."
	s.spawned = 0
	await s.get_tree().create_timer(0.5).timeout
	if s.spawned < 2 or s.spawned > 3:
		return "In 0.5 seconds %d enemies spawned, expected about 2. Is timeout connected to _on_spawn_timer_timeout?" % s.spawned
	return ""
