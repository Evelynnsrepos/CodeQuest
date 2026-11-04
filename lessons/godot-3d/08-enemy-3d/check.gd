func check(e) -> String:
	var tree: SceneTree = e.get_tree()
	e.motion_mode = CharacterBody3D.MOTION_MODE_FLOATING
	var shape := CollisionShape3D.new()
	shape.shape = CapsuleShape3D.new()
	e.add_child(shape)
	var target := Vector3(6, 5, 8)    # 10 m away on the ground, and up high
	e.target = target
	e.position = Vector3.ZERO
	e.attacks = 0
	for i in 60:
		await tree.physics_frame
	var flat: Vector3 = target - e.position
	flat.y = 0
	if absf(e.position.y) > 0.01:
		return "The enemy left the ground (y = %.2f). Ignore the height when chasing." % e.position.y
	if absf(flat.length() - 7.0) > 0.2:
		return "After 1 second at 3 m/s the enemy should be 7 m from the target, but it's %.2f m away." % flat.length()
	var fwd: Vector3 = -e.global_transform.basis.z
	if not fwd.is_equal_approx(Vector3(0.6, 0, 0.8)):
		return "The enemy should face the target along the ground, direction (0.6, 0, 0.8), but it faces %s." % str(fwd)
	if e.attacks != 0:
		return "The enemy attacked from 7 m away."
	for i in 180:
		await tree.physics_frame
	flat = target - e.position
	flat.y = 0
	if flat.length() < 1.4:
		return "The enemy walked right into the target. Stop at attack_range (1.5 m)."
	if e.attacks == 0:
		return "Within attack_range the enemy should call attack()."
	return ""
