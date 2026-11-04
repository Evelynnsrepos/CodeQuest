func check(p) -> String:
	var ended := [0]
	p.game_over.connect(func(): ended[0] += 1)
	p.set_checkpoint(Vector2(300, -50))
	if p.checkpoint != Vector2(300, -50):
		return "set_checkpoint(Vector2(300, -50)) should store the spot in checkpoint."
	p.position = Vector2(900, 1200)
	p.velocity = Vector2(50, 700)
	await p.get_tree().physics_frame
	await p.get_tree().physics_frame
	if p.lives != 2:
		return "The player fell below death_y but lives is %d, expected 2. Call die() in _physics_process." % p.lives
	if p.position != Vector2(300, -50):
		return "After dying the player should be back at the checkpoint (300, -50), but it's at %s." % str(p.position)
	if p.velocity != Vector2.ZERO:
		return "After respawning velocity should be Vector2.ZERO, but it's %s." % str(p.velocity)
	if ended[0] != 0:
		return "game_over was emitted with lives left."
	p.die()
	p.die()
	if ended[0] != 1:
		return "Losing the last life should emit game_over once. It was emitted %d times." % ended[0]
	return ""
