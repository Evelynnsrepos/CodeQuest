func check(p) -> String:
	p.set_process(false)
	p.take_damage(1)
	p.take_damage(1)
	p.take_damage(1)
	if p.health != 4:
		return "Three hits in the same moment should only count once (health 4), but health is %d." % p.health
	var states := {}
	for i in 8:
		p._process(0.05)
		states[p.visible] = true
	if states.size() < 2:
		return "While invincible the player should blink (visible switching between true and false)."
	p._process(0.3)
	p.take_damage(1)
	if p.health != 4:
		return "After 0.7 s the player is still invincible, but took damage."
	p._process(0.35)
	if not p.visible:
		return "When invincibility ends the player must be visible again."
	p.take_damage(2)
	if p.health != 2:
		return "After more than 1 s the player can be hit again: health should be 2, got %d." % p.health
	return ""
