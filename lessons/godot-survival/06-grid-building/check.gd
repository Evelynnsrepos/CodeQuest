func check(g) -> String:
	var cases = [[Vector2(70, 10), Vector2i(2, 0)], [Vector2(90, 31.9), Vector2i(2, 0)], [Vector2(-5, 64), Vector2i(-1, 2)], [Vector2(0, 0), Vector2i(0, 0)]]
	for c in cases:
		var got = g.to_cell(c[0])
		if got != c[1]:
			return "to_cell(%s) returned %s, expected %s. Round down with floor." % [str(c[0]), str(got), str(c[1])]
	if g.cell_to_world(Vector2i(2, -1)) != Vector2(64, -32):
		return "cell_to_world(Vector2i(2, -1)) should be (64, -32), got %s." % str(g.cell_to_world(Vector2i(2, -1)))
	g.occupied = {}
	if not g.place("wall", Vector2(70, 10)):
		return "Placing a wall on an empty cell should return true."
	if g.place("door", Vector2(80, 20)):
		return "(80, 20) is in the same cell (2, 0) as the wall, so place should return false."
	if g.occupied.get(Vector2i(2, 0)) != "wall":
		return "occupied should hold \"wall\" at Vector2i(2, 0). It is %s." % str(g.occupied)
	if not g.place("door", Vector2(100, 20)):
		return "(100, 20) is a different cell (3, 0), so the door fits."
	return ""
