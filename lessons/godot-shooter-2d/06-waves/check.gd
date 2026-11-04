func check(m) -> String:
	var cleared := []
	m.wave_cleared.connect(func(n): cleared.append(n))
	m.start_wave()
	if m.wave != 1:
		return "After the first start_wave() wave should be 1, got %d." % m.wave
	if m.get_child_count() != 5 or m.alive != 5:
		return "Wave 1 should spawn 5 enemies and set alive to 5. There are %d children and alive is %d." % [m.get_child_count(), m.alive]
	var enemies = m.get_children()
	for i in 4:
		enemies[i].emit_signal("died")
	if m.alive != 1:
		return "After 4 of 5 enemies died, alive should be 1, got %d. Did you connect each enemy's died signal?" % m.alive
	if cleared.size() != 0:
		return "wave_cleared was emitted while an enemy was still alive."
	enemies[4].emit_signal("died")
	if cleared != [1]:
		return "When the last enemy dies, wave_cleared should be emitted once with 1. Got: %s" % str(cleared)
	for e in enemies:
		e.free()
	m.start_wave()
	if m.alive != 7 or m.get_child_count() != 7:
		return "Wave 2 should spawn 7 enemies (3 + 2 × 2). alive is %d." % m.alive
	return ""
