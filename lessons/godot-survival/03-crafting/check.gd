func check(c) -> String:
	c.items = {"wood": 4, "stone": 1}
	if c.can_craft("axe"):
		return "With 4 wood and 1 stone you can't craft an axe (needs 2 stone)."
	if c.craft("axe"):
		return "craft(\"axe\") should return false without enough stone."
	if c.items != {"wood": 4, "stone": 1}:
		return "A failed craft changed the items to %s. Check everything before taking anything." % str(c.items)
	if c.can_craft("sword"):
		return "can_craft(\"sword\") should be false: there's no sword recipe."
	if c.can_craft("bandage"):
		return "can_craft(\"bandage\") should be false: there's no cloth at all."
	c.items["stone"] = 2
	if not c.can_craft("axe"):
		return "With 4 wood and 2 stone you can craft an axe."
	if not c.craft("axe"):
		return "craft(\"axe\") should return true with 4 wood and 2 stone."
	if c.items.get("wood") != 1 or c.items.get("stone") != 0 or c.items.get("axe") != 1:
		return "After crafting an axe expected 1 wood, 0 stone and 1 axe. Items: %s" % str(c.items)
	return ""
