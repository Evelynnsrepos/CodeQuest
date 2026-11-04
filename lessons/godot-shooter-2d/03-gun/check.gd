func check(p) -> String:
	p.set_process(false)
	var proto := Node2D.new()
	proto.name = "Bullet"
	var scene := PackedScene.new()
	scene.pack(proto)
	p.bullet_scene = scene
	p.position = Vector2(100, 100)
	p.rotation = PI / 2
	var b = p.shoot()
	if b == null:
		return "The first shot should return the new bullet."
	if b.get_parent() != p.get_parent():
		return "Add the bullet to get_parent() (the level), not to the player."
	if not b.global_position.is_equal_approx(Vector2(100, 120)):
		return "Facing down from (100, 100), the bullet should start at the muzzle (100, 120), but it's at %s." % str(b.global_position)
	if not is_equal_approx(b.rotation, PI / 2):
		return "The bullet's rotation should match the player's (PI / 2), but it's %s." % str(b.rotation)
	if p.shoot() != null:
		return "Shooting again straight away should return null because of the cooldown."
	p._process(0.3)
	p.rotation = 0
	var b2 = p.shoot()
	if b2 == null:
		return "After the cooldown the gun should shoot again."
	if b2 == b:
		return "Each shot needs a new bullet from bullet_scene.instantiate()."
	if not b2.global_position.is_equal_approx(Vector2(120, 100)):
		return "Facing right from (100, 100), the bullet should start at (120, 100), but it's at %s." % str(b2.global_position)
	return ""
