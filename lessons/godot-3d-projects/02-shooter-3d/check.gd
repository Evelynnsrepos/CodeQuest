func check(w) -> String:
	w.current = 0
	w.cycle(1)
	if w.current != 1 or w.current_damage() != 60:
		return "cycle(1) from the pistol should pick the shotgun (damage 60). current is %d." % w.current
	w.cycle(1)
	w.cycle(1)
	if w.current != 0:
		return "Cycling past the rifle should wrap to the pistol (0), got %d." % w.current
	w.cycle(-1)
	if w.current != 2 or w.current_damage() != 35:
		return "cycle(-1) from the pistol should wrap to the rifle (2), got %d." % w.current
	w.select(1)
	if w.current != 1:
		return "select(1) should pick the shotgun."
	w.select(7)
	w.select(-1)
	if w.current != 1:
		return "select(7) and select(-1) don't exist and should be ignored, but current changed to %d." % w.current
	return ""
