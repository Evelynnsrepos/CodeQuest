const TARGET := "extends StaticBody3D\nvar health := 100\nfunc take_damage(amount):\n\thealth -= amount\n"


func add_box(tree: SceneTree, spot: Vector3, scripted: bool) -> StaticBody3D:
	var body := StaticBody3D.new()
	if scripted:
		var s := GDScript.new()
		s.source_code = TARGET
		s.reload()
		body.set_script(s)
	var shape := CollisionShape3D.new()
	shape.shape = BoxShape3D.new()
	body.add_child(shape)
	body.position = spot
	tree.root.add_child(body)
	return body


func check(gun) -> String:
	var tree: SceneTree = gun.get_tree()
	var near := add_box(tree, Vector3(0, 0, -10), true)
	var behind := add_box(tree, Vector3(0, 0, -20), true)
	var side := add_box(tree, Vector3(10, 0, 0), false)
	var far := add_box(tree, Vector3(0, 0, 80), true)
	await tree.physics_frame
	await tree.physics_frame

	var got = gun.shoot()
	if got != near:
		return "Shooting forward (-z) should hit the target 10 m ahead first, but shoot() returned %s." % str(got)
	if near.health != 75 or behind.health != 100:
		return "The first target should drop to 75 health and the one behind it stay at 100. They have %d and %d." % [near.health, behind.health]

	gun.rotation.y = -PI / 2    # turn right, towards +x
	got = gun.shoot()
	if got != side:
		return "Turned to face +x, the shot should hit the wall there. Did you use -global_transform.basis.z?"

	gun.rotation.y = PI         # facing +z, the target is 80 m away
	got = gun.shoot()
	if got != null:
		return "A target 80 m away is beyond max_range (50), so shoot() should return null."
	if far.health != 100:
		return "A target out of range was damaged."
	return ""
