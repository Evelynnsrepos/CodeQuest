func add_box(tree: SceneTree, center: Vector2, size: Vector2) -> void:
	var body := StaticBody2D.new()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = size
	body.add_child(shape)
	body.position = center
	tree.root.add_child(body)


func jump_height(p, tree: SceneTree, hold_frames: int) -> float:
	var start: float = p.position.y
	var top := start
	Input.action_press("ui_accept")
	await tree.process_frame
	for i in 70:
		await tree.physics_frame
		if i == hold_frames:
			Input.action_release("ui_accept")
			await tree.process_frame
		top = minf(top, p.position.y)
	return start - top


func check(p) -> String:
	var tree: SceneTree = p.get_tree()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = Vector2(20, 30)
	p.add_child(shape)
	add_box(tree, Vector2(0, 50), Vector2(4000, 100))
	p.position = Vector2(0, -15)
	for i in 5:
		await tree.physics_frame
	var full: float = await jump_height(p, tree, 60)
	var hop: float = await jump_height(p, tree, 4)
	if full < 90:
		return "Holding jump only reached %.0f pixels, expected about 103." % full
	if hop > full * 0.6:
		return "A quick tap reached %.0f pixels and a held jump %.0f. The tap should be much lower: cut velocity.y when ui_accept is released." % [hop, full]
	return ""
