const ENEMY := "extends StaticBody2D\nvar health := 5\nfunc take_damage(amount):\n\thealth -= amount\n"


func make_body(source: String, spot: Vector2, group: String) -> StaticBody2D:
	var body := StaticBody2D.new()
	if source != "":
		var s := GDScript.new()
		s.source_code = source
		s.reload()
		body.set_script(s)
	var shape := CollisionShape2D.new()
	shape.shape = CircleShape2D.new()
	shape.shape.radius = 10
	body.add_child(shape)
	body.position = spot
	if group != "":
		body.add_to_group(group)
	return body


func make_bullet(b, spot: Vector2) -> Node:
	var bullet = b.duplicate()
	bullet.position = spot
	var shape := CollisionShape2D.new()
	shape.shape = CircleShape2D.new()
	shape.shape.radius = 4
	bullet.add_child(shape)
	return bullet


func frames(tree: SceneTree, n: int) -> void:
	for i in n:
		await tree.physics_frame


func check(b) -> String:
	var tree: SceneTree = b.get_tree()
	var root := tree.root

	var player := make_body("", Vector2(0, 0), "player")
	root.add_child(player)
	var b1 = make_bullet(b, Vector2(0, 0))
	root.add_child(b1)
	await frames(tree, 4)
	if not is_instance_valid(b1):
		return "The bullet disappeared when it touched the player. Ignore bodies in the \"player\" group."
	b1.queue_free()

	var enemy := make_body(ENEMY, Vector2(300, 0), "")
	root.add_child(enemy)
	var b2 = make_bullet(b, Vector2(300, 0))
	root.add_child(b2)
	await frames(tree, 4)
	await tree.process_frame
	if enemy.health != 3:
		return "A bullet hit an enemy with 5 health; expected 3 left, but it has %d. Is body_entered connected?" % enemy.health
	if is_instance_valid(b2):
		return "After hitting the enemy the bullet should remove itself with queue_free()."

	var wall := make_body("", Vector2(600, 0), "")
	root.add_child(wall)
	var b3 = make_bullet(b, Vector2(600, 0))
	root.add_child(b3)
	await frames(tree, 4)
	await tree.process_frame
	if is_instance_valid(b3):
		return "A bullet that hits a wall (no take_damage) should still disappear."
	return ""
