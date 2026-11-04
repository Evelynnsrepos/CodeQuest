func add_box(tree: SceneTree, center: Vector2, size: Vector2) -> void:
	var body := StaticBody2D.new()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = size
	body.add_child(shape)
	body.position = center
	tree.root.add_child(body)


func tap(tree: SceneTree, action: String) -> void:
	Input.action_press(action)
	await tree.process_frame
	await tree.physics_frame
	await tree.physics_frame
	Input.action_release(action)


func check(p) -> String:
	if absf(p.jump_velocity + sqrt(2.0 * 980.0 * 64.0)) > 0.5:
		return "jump_velocity is %s. For a 64-pixel jump it should be about -354.2 (negative is up)." % str(p.jump_velocity)
	var tree: SceneTree = p.get_tree()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = Vector2(20, 30)
	p.add_child(shape)
	add_box(tree, Vector2(0, 50), Vector2(4000, 100))
	p.position = Vector2(0, -15)
	for i in 5:
		await tree.physics_frame
	var floor_y: float = p.position.y
	await tap(tree, "ui_accept")
	var top: float = p.position.y
	var went_up := false
	for i in 60:
		top = minf(top, p.position.y)
		if p.velocity.y < 0:
			went_up = true
		if went_up and i == 10:
			# mid-air: this press must not jump again
			await tap(tree, "ui_accept")
		await tree.physics_frame
	if not went_up:
		return "Pressing ui_accept on the floor didn't jump."
	var height := floor_y - top
	if height > 80:
		return "The jump reached %.0f pixels. Did the player jump again in mid-air? Check is_on_floor() too." % height
	if absf(height - 64) > 6:
		return "The jump reached %.0f pixels high, expected about 64." % height
	if not p.is_on_floor():
		return "After a second the player should have landed again."
	return ""
