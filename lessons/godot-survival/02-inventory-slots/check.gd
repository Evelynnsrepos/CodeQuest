func check(inv) -> String:
	inv.slots = [{"item": "wood", "count": 10}, {"item": "wood", "count": 3}, null, null]
	var left = inv.add_item("wood", 15)
	var want = [{"item": "wood", "count": 10}, {"item": "wood", "count": 10}, {"item": "wood", "count": 8}, null]
	if left != 0 or inv.slots != want:
		return "Adding 15 wood: expected slots %s and 0 left over, got %s and %s." % [str(want), str(inv.slots), str(left)]
	inv.slots = [null, {"item": "stone", "count": 4}, null, null]
	inv.add_item("stone", 3)
	if inv.slots[0] != null:
		return "Adding 3 stone should top up the existing stone stack before using an empty slot. Slots: %s" % str(inv.slots)
	if inv.slots[1].count != 7:
		return "The stone stack should now hold 7, but it holds %s." % str(inv.slots[1].count)
	inv.slots = [null, {"item": "stone", "count": 9}, null, null]
	left = inv.add_item("berry", 35)
	if left != 5:
		return "Adding 35 berries with 3 empty slots of 10 should leave 5 that don't fit, but add_item returned %s." % str(left)
	if inv.slots[1].item != "stone" or inv.slots[1].count != 9:
		return "Berries must not go into the stone stack."
	return ""
