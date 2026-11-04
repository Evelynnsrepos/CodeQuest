func check(s) -> String:
	s.bag = {}
	s.add_item("wood", 3)
	s.add_item("wood", 2)
	s.add_item("stone", 1)
	if s.bag != {"wood": 5, "stone": 1}:
		return "After adding 3 wood, 2 wood and 1 stone the bag is %s, expected {\"wood\": 5, \"stone\": 1}." % str(s.bag)
	if s.remove_item("wood", 9) != false:
		return "remove_item(\"wood\", 9) should return false: there are only 5."
	if s.bag.get("wood") != 5:
		return "A failed remove_item changed the bag. It should change nothing."
	if s.remove_item("iron", 1) != false:
		return "remove_item(\"iron\", 1) should return false: there is no iron."
	if s.remove_item("wood", 2) != true or s.bag.get("wood") != 3:
		return "remove_item(\"wood\", 2) should return true and leave 3 wood. The bag is %s." % str(s.bag)
	if s.remove_item("stone", 1) != true:
		return "remove_item(\"stone\", 1) should return true."
	if s.bag.has("stone"):
		return "Stone reached 0, so its key should be erased. The bag is %s." % str(s.bag)
	return ""
