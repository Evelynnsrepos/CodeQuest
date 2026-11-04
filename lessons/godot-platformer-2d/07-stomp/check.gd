func check(p) -> String:
	p.set_physics_process(false)
	var enemy := Node2D.new()
	p.get_parent().add_child(enemy)
	enemy.position = Vector2(0, 120)

	p.position = Vector2(0, 100)
	p.velocity = Vector2(0, 200)
	var r = p.touch_enemy(enemy)
	if r != "stomp":
		return "Falling onto the enemy from above (player y 100, enemy y 120) should return \"stomp\", got \"%s\"." % str(r)
	if not enemy.is_queued_for_deletion():
		return "A stomped enemy should be removed with queue_free()."
	if p.velocity.y != -300:
		return "After a stomp velocity.y should be bounce_velocity (-300), got %s." % str(p.velocity.y)
	if p.health != 3:
		return "A stomp shouldn't hurt the player."

	var enemy2 := Node2D.new()
	p.get_parent().add_child(enemy2)
	enemy2.position = Vector2(0, 120)
	p.position = Vector2(-20, 118)
	p.velocity = Vector2(100, 50)
	if p.touch_enemy(enemy2) != "hurt" or p.health != 2:
		return "Walking into the enemy's side (player y 118, enemy y 120) should return \"hurt\" and lower health to 2."
	if enemy2.is_queued_for_deletion():
		return "The enemy was removed even though the player hit its side."

	p.position = Vector2(0, 100)
	p.velocity = Vector2(0, -200)
	if p.touch_enemy(enemy2) != "hurt":
		return "Jumping up into an enemy (moving up, not falling) should return \"hurt\"."
	return ""
