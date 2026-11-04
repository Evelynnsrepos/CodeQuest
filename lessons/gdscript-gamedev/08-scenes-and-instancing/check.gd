func check(level) -> String:
	var coin := Node2D.new()
	coin.name = "Coin"
	var sprite := Node2D.new()
	sprite.name = "Sprite"
	coin.add_child(sprite)
	sprite.owner = coin
	var scene := PackedScene.new()
	scene.pack(coin)
	level.coin_scene = scene
	var a = level.spawn_at(Vector2(10, 20))
	var b = level.spawn_at(Vector2(50, 20))
	if a == null or b == null:
		return "spawn_at() should return the new coin."
	if a == b:
		return "Both calls returned the same node. Call instantiate() each time for a fresh copy."
	if not a.has_node("Sprite"):
		return "The spawned node isn't a copy of coin_scene. Use coin_scene.instantiate()."
	if a.get_parent() != level or b.get_parent() != level:
		return "Add each coin as a child of this node with add_child()."
	if not a.position.is_equal_approx(Vector2(10, 20)) or not b.position.is_equal_approx(Vector2(50, 20)):
		return "The coins are at %s and %s, expected (10, 20) and (50, 20)." % [str(a.position), str(b.position)]
	return ""
