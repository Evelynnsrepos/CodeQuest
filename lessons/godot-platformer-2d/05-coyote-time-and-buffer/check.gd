func add_box(tree: SceneTree, center: Vector2, size: Vector2) -> void:
	var body := StaticBody2D.new()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = size
	body.add_child(shape)
	body.position = center
	tree.root.add_child(body)


func tap(tree: SceneTree) -> void:
	Input.action_press("ui_accept")
	await tree.process_frame
	await tree.physics_frame
	Input.action_release("ui_accept")


func jumped_within(p, tree: SceneTree, n: int) -> bool:
	for i in n:
		if p.velocity.y < -100:
			return true
		await tree.physics_frame
	return p.velocity.y < -100


func check(p) -> String:
	var tree: SceneTree = p.get_tree()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = Vector2(20, 30)
	p.add_child(shape)
	# a ledge: floor from x = -2000 to x = 0, and a low floor far below
	add_box(tree, Vector2(-1000, 50), Vector2(2000, 100))
	add_box(tree, Vector2(0, 650), Vector2(100000, 100))
	p.position = Vector2(-200, -15)
	for i in 5:
		await tree.physics_frame

	# 1. coyote time: walk off the ledge, jump 3 frames later
	Input.action_press("ui_right")
	var guard := 0
	while p.is_on_floor() and guard < 200:
		await tree.physics_frame
		guard += 1
	Input.action_release("ui_right")
	for i in 2:
		await tree.physics_frame
	await tap(tree)
	if not await jumped_within(p, tree, 3):
		return "Jumping 3 frames after walking off the ledge didn't work. Add coyote time."

	# 2. buffering: press jump just before landing on the low floor
	var guard2 := 0
	while guard2 < 400:
		guard2 += 1
		await tree.physics_frame
		if p.velocity.y > 0:
			var gap: float = 600.0 - (p.position.y + 15)
			var per_frame: float = p.velocity.y / 60.0
			if gap < per_frame * 3.5:
				break
	await tap(tree)
	if p.velocity.y < -100:
		return "The player jumped in mid-air before landing. Only jump when on the floor (or in coyote time)."
	if not await jumped_within(p, tree, 8):
		return "Pressing jump just before landing should jump as soon as the player lands. Add a jump buffer."

	# 3. no jump long after leaving the ground
	for i in 30:
		await tree.physics_frame
	if p.velocity.y < -100:
		return "The player jumped twice from one press. Set both timers to 0 after jumping."
	await tap(tree)
	if await jumped_within(p, tree, 3):
		return "The player jumped half a second after leaving the ground. Coyote time should only last coyote_time (0.1 s)."
	return ""
