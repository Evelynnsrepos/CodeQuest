const TREE := "extends StaticBody3D\nvar prompt := \"Chop tree\"\nvar chopped_by = null\nfunc interact(who):\n\tchopped_by = who\n"


func add_box(tree: SceneTree, spot: Vector3, scripted: bool) -> StaticBody3D:
	var body := StaticBody3D.new()
	if scripted:
		var s := GDScript.new()
		s.source_code = TREE
		s.reload()
		body.set_script(s)
	var shape := CollisionShape3D.new()
	shape.shape = BoxShape3D.new()
	body.add_child(shape)
	body.position = spot
	tree.root.add_child(body)
	return body


func frames(tree: SceneTree, n: int) -> void:
	for i in n:
		await tree.physics_frame


func check(p) -> String:
	var tree: SceneTree = p.get_tree()
	await frames(tree, 2)
	if p.looking_at() != null or p.prompt_text() != "" or p.try_interact():
		return "Looking at nothing: looking_at() should be null, prompt_text() \"\" and try_interact() false."
	var rock := add_box(tree, Vector3(0, 0, -2), false)
	await frames(tree, 3)
	if p.looking_at() != null:
		return "A rock without an interact method isn't usable, so looking_at() should be null."
	rock.free()
	var t := add_box(tree, Vector3(0, 0, -2), true)
	await frames(tree, 3)
	if p.looking_at() != t:
		return "Looking at a tree 1.5 m ahead (it has interact), looking_at() should return it."
	if p.prompt_text() != "[E] Chop tree":
		return "prompt_text() should be \"[E] Chop tree\", got \"%s\"." % p.prompt_text()
	if not p.try_interact() or t.chopped_by != p:
		return "try_interact() should call interact(self) on the tree and return true."
	t.position = Vector3(0, 0, -6)
	await frames(tree, 3)
	if p.looking_at() != null:
		return "A tree 5.5 m away is out of reach, so looking_at() should be null."
	return ""
