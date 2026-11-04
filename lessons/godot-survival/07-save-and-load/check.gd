func check(s) -> String:
	s.health = 64
	s.day = 12
	s.items = {"wood": 5, "berry": 2}
	s.position = Vector2(120.5, -40)
	var text: String = s.save_text()
	var parsed = JSON.parse_string(text)
	if not parsed is Dictionary:
		return "save_text() should return JSON text, got: %s" % text
	for key in ["health", "day", "items", "position"]:
		if not parsed.has(key):
			return "The saved JSON is missing \"%s\": %s" % [key, text]
	s.health = 1
	s.day = 1
	s.items = {}
	s.position = Vector2.ZERO
	s.load_text(text)
	if typeof(s.health) != TYPE_INT or s.health != 64 or s.day != 12:
		return "After loading, health should be 64 and day 12 (as ints). Got %s and %s." % [str(s.health), str(s.day)]
	if s.items.get("wood") != 5.0 or s.items.get("berry") != 2.0:
		return "After loading, items should be wood 5 and berry 2, got %s." % str(s.items)
	if not s.position.is_equal_approx(Vector2(120.5, -40)):
		return "After loading, position should be (120.5, -40), got %s." % str(s.position)
	return ""
