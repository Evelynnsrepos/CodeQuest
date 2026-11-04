func add_box(tree: SceneTree, center: Vector2, size: Vector2) -> void:
	var body := StaticBody2D.new()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = size
	body.add_child(shape)
	body.position = center
	tree.root.add_child(body)


func check(e) -> String:
	var tree: SceneTree = e.get_tree()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = Vector2(20, 30)
	e.add_child(shape)
	# platform from x = -150 to x = 150 with a wall on the right; drop on the left
	add_box(tree, Vector2(0, 50), Vector2(300, 100))
	add_box(tree, Vector2(160, -50), Vector2(20, 100))
	e.position = Vector2(0, -15)
	var min_x := 0.0
	var max_x := 0.0
	var turns := 0
	var last_dir: int = e.direction
	for i in 240:
		await tree.physics_frame
		min_x = minf(min_x, e.position.x)
		max_x = maxf(max_x, e.position.x)
		if e.direction != last_dir:
			turns += 1
			last_dir = e.direction
		if e.position.y > 100:
			return "The enemy walked off the edge of the platform. Turn around when the ray stops colliding."
	if max_x < 120:
		return "The enemy never got near the wall (it reached x = %.0f). Does it walk with velocity.x = direction * speed?" % max_x
	if max_x > 141:
		return "The enemy is inside the wall."
	if min_x > -110:
		return "The enemy never walked back to the left edge. Does it turn around at the wall (is_on_wall())?"
	if turns < 2:
		return "In 4 seconds the enemy turned around %d times, expected at least 2 (wall, then ledge)." % turns
	if turns > 8:
		return "The enemy turned %d times in 4 seconds. It's flipping back and forth. Move the ray to the new front after turning." % turns
	return ""
