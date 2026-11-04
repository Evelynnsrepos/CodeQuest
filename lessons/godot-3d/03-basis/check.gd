func frames(tree: SceneTree, n: int) -> void:
	for i in n:
		await tree.physics_frame


func check(p) -> String:
	var tree: SceneTree = p.get_tree()
	p.motion_mode = CharacterBody3D.MOTION_MODE_FLOATING
	Input.action_press("ui_left")
	await frames(tree, 30)
	Input.action_release("ui_left")
	if absf(p.rotation.y - 1.0) > 0.1:
		return "Holding left for half a second at 2 rad/s should turn the player to rotation.y ≈ 1.0, got %.2f." % p.rotation.y

	p.rotation.y = PI / 2
	p.position = Vector3.ZERO
	Input.action_press("ui_up")
	await frames(tree, 30)
	Input.action_release("ui_up")
	var moved: Vector3 = p.position
	if moved.x > -1.5 or absf(moved.z) > 0.2:
		return "Turned left 90° and holding up, the player should walk towards -x (its forward). It moved %s. Use transform.basis * Vector3(0, 0, forward)." % str(moved)

	p.rotation.y = 0
	p.position = Vector3.ZERO
	Input.action_press("ui_down")
	await frames(tree, 30)
	Input.action_release("ui_down")
	if p.position.z < 1.5:
		return "Facing forward and holding down should walk backwards (towards +z). It moved %s." % str(p.position)
	return ""
