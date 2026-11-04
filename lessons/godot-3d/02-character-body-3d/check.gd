func add_floor(tree: SceneTree) -> void:
	var body := StaticBody3D.new()
	var shape := CollisionShape3D.new()
	shape.shape = BoxShape3D.new()
	shape.shape.size = Vector3(200, 1, 200)
	body.add_child(shape)
	body.position = Vector3(0, -0.5, 0)    # top surface at y = 0
	tree.root.add_child(body)


func frames(tree: SceneTree, n: int) -> void:
	for i in n:
		await tree.physics_frame


func check(p) -> String:
	if not p is CharacterBody3D:
		return "Keep \"extends CharacterBody3D\" at the top."
	var tree: SceneTree = p.get_tree()
	var shape := CollisionShape3D.new()
	shape.shape = CapsuleShape3D.new()
	p.add_child(shape)
	add_floor(tree)
	p.position = Vector3(0, 3, 0)
	await frames(tree, 70)
	if not p.is_on_floor():
		return "The player should fall onto the floor (it's at y = %.2f). Lower velocity.y by gravity * delta." % p.position.y

	var start: Vector3 = p.position
	Input.action_press("ui_up")
	await frames(tree, 30)
	Input.action_release("ui_up")
	var moved: Vector3 = p.position - start
	if moved.z > -2:
		return "Holding up for half a second should move the player forward (towards -z) about 2.5 m. It moved %s." % str(moved)
	if absf(moved.x) > 0.01:
		return "Holding up moved the player sideways too: %s." % str(moved)

	await frames(tree, 3)
	var floor_y: float = p.position.y
	Input.action_press("ui_accept")
	await tree.process_frame
	var top := floor_y
	for i in 70:
		await tree.physics_frame
		if i == 2:
			Input.action_release("ui_accept")
		top = maxf(top, p.position.y)
	var height := top - floor_y
	if height < 0.8 or height > 1.3:
		return "The jump reached %.2f m. With jump_velocity 4.5 and gravity 9.8 it should be about 1 m (4.5² ÷ (2 × 9.8))." % height
	if not p.is_on_floor():
		return "The player should land again after jumping."
	return ""
