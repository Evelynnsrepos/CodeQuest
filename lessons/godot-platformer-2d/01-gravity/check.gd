func add_box(tree: SceneTree, center: Vector2, size: Vector2) -> void:
	var body := StaticBody2D.new()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = size
	body.add_child(shape)
	body.position = center
	tree.root.add_child(body)


func check(p) -> String:
	if not p is CharacterBody2D:
		return "Keep \"extends CharacterBody2D\" at the top."
	var tree: SceneTree = p.get_tree()
	var shape := CollisionShape2D.new()
	shape.shape = RectangleShape2D.new()
	shape.shape.size = Vector2(20, 30)
	p.add_child(shape)
	add_box(tree, Vector2(0, 50), Vector2(2000, 100))   # floor surface at y = 0
	p.position = Vector2(0, -400)
	p.velocity = Vector2.ZERO
	await tree.physics_frame
	for i in 10:
		await tree.physics_frame
	var v1: float = p.velocity.y
	if v1 <= 0:
		return "The player isn't falling: velocity.y is %s after 10 frames in the air." % str(v1)
	for i in 10:
		await tree.physics_frame
	var v2: float = p.velocity.y
	if v2 <= v1:
		return "The player should fall faster and faster, but velocity.y went from %.0f to %.0f." % [v1, v2]
	var fastest := 0.0
	for i in 90:
		await tree.physics_frame
		fastest = maxf(fastest, p.velocity.y)
	if fastest > 600.5:
		return "The player fell at %.0f px/s. Limit velocity.y to max_fall_speed (600)." % fastest
	if fastest < 599:
		return "The player never reached max_fall_speed. Did it fall the whole way?"
	if not p.is_on_floor():
		return "After 2 seconds the player should be standing on the floor. It's at %s." % str(p.position)
	if absf(p.position.y + 15) > 2:
		return "The player should rest on the floor at y = -15, but it's at y = %.1f." % p.position.y
	return ""
