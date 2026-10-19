func check(level) -> String:
	level.spawn_coins(3, 64)
	if level.get_child_count() != 3:
		return "spawn_coins(3, 64) should add 3 children, but there are %d." % level.get_child_count()
	for i in 3:
		var coin = level.get_node_or_null("Coin%d" % i)
		if coin == null:
			return "There's no child named Coin%d." % i
		if not coin is Node2D:
			return "Coin%d should be a Node2D." % i
		if not coin.position.is_equal_approx(Vector2(i * 64, 0)):
			return "Coin%d is at %s, expected %s." % [i, str(coin.position), str(Vector2(i * 64, 0))]
	return ""
