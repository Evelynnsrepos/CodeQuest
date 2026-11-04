func add_box(tree: SceneTree, center: Vector2, size: Vector2) -> void:
	var body := StaticBody2D.new()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = size
	body.add_child(shape)
	body.position = center
	tree.root.add_child(body)


func frames(tree: SceneTree, n: int) -> void:
	for i in n:
		await tree.physics_frame


func check(p) -> String:
	var tree: SceneTree = p.get_tree()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = Vector2(20, 30)
	p.add_child(shape)
	add_box(tree, Vector2(0, 50), Vector2(100000, 100))
	p.position = Vector2(0, -15)
	await frames(tree, 3)

	Input.action_press("ui_right")
	await frames(tree, 5)
	var early: float = p.velocity.x
	await frames(tree, 25)
	var full: float = p.velocity.x
	Input.action_release("ui_right")
	if early <= 0:
		return "Holding right didn't make the player move right."
	if early >= 299:
		return "The player was at full speed after 5 frames. Accelerate with move_toward instead of setting the speed directly."
	if absf(full - 300) > 0.5:
		return "After half a second of holding right the speed is %.0f, expected max_speed (300)." % full
	await frames(tree, 3)
	var slowing: float = p.velocity.x
	if slowing >= 299 or slowing <= 0:
		return "Just after letting go, the speed is %.0f. It should drop gradually (friction), not stay at 300 or stop at once." % slowing
	await frames(tree, 30)
	if absf(p.velocity.x) > 0.01:
		return "Half a second after letting go the player still moves at %.0f px/s. Slow down to 0 with friction." % p.velocity.x

	Input.action_press("ui_left")
	await frames(tree, 30)
	Input.action_release("ui_left")
	if absf(p.velocity.x + 300) > 0.5:
		return "Holding left should reach -300 px/s, but the speed is %.0f." % p.velocity.x
	return ""
