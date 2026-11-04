func check(g) -> String:
	g.magazine = 2
	g.reserve = 30
	if not g.fire() or not g.fire():
		return "With 2 bullets in the magazine, fire() should work twice."
	if g.fire():
		return "With an empty magazine fire() should return false."
	if g.magazine != 0:
		return "magazine went below 0: %d." % g.magazine
	g.magazine = 4
	g.reserve = 50
	g.reload()
	if g.magazine != 12 or g.reserve != 42:
		return "Magazine 4, reserve 50: after reload() expected 12 and 42, got %d and %d." % [g.magazine, g.reserve]
	g.magazine = 0
	g.reserve = 5
	g.reload()
	if g.magazine != 5 or g.reserve != 0:
		return "Magazine 0, reserve 5: after reload() expected 5 and 0, got %d and %d." % [g.magazine, g.reserve]
	g.reload()
	if g.magazine != 5 or g.reserve != 0:
		return "Reloading with an empty reserve should change nothing."
	return ""
