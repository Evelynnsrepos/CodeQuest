func make_body(group: String, spot: Vector2) -> CharacterBody2D:
	var body := CharacterBody2D.new()
	var shape := CollisionShape2D.new()
	shape.shape = CircleShape2D.new()
	shape.shape.radius = 8
	body.add_child(shape)
	if group != "":
		body.add_to_group(group)
	body.position = spot
	return body


func check(coin) -> String:
	if not coin is Area2D:
		return "Keep \"extends Area2D\" at the top."
	var tree: SceneTree = coin.get_tree()
	var shape := CollisionShape2D.new()
	shape.shape = CircleShape2D.new()
	shape.shape.radius = 16
	coin.add_child(shape)
	coin.position = Vector2(500, 500)
	var hits := [0]
	coin.collected.connect(func(): hits[0] += 1)

	var enemy := make_body("enemies", Vector2(500, 500))
	tree.root.add_child(enemy)
	for i in 4:
		await tree.physics_frame
	if hits[0] != 0 or not is_instance_valid(coin):
		return "An enemy (not in the \"player\" group) collected the coin."
	enemy.queue_free()

	var player := make_body("player", Vector2(500, 500))
	tree.root.add_child(player)
	for i in 4:
		await tree.physics_frame
	await tree.process_frame
	if hits[0] != 1:
		return "The player touched the coin but collected was emitted %d times, expected once. Is body_entered connected?" % hits[0]
	if is_instance_valid(coin):
		return "The coin should remove itself with queue_free() when collected."
	return ""
