func check(t) -> String:
	var drops := []
	var gone := [0]
	t.dropped.connect(func(item, amount): drops.append([item, amount]))
	t.depleted.connect(func(): gone[0] += 1)
	t.hit("hand")
	t.hit("stone_axe")
	t.hit("rock")
	if drops != [["wood", 1], ["wood", 2], ["wood", 1]]:
		return "Hits with hand, stone_axe and an unknown tool should drop 1, 2 and 1 wood. Drops: %s" % str(drops)
	if t.hits_left != 2:
		return "After those hits 2 should be left, got %d." % t.hits_left
	if gone[0] != 0:
		return "depleted was emitted too early."
	t.hit("iron_axe")
	if drops.back() != ["wood", 2]:
		return "An iron axe on a tree with 2 hits left should drop 2 wood, got %s." % str(drops.back())
	if gone[0] != 1 or not t.is_queued_for_deletion():
		return "When hits_left reaches 0, emit depleted once and queue_free() the tree."
	t.hit("hand")
	if drops.size() != 4 or gone[0] != 1:
		return "Hitting a used-up tree should do nothing."
	return ""
