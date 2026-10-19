func check(player) -> String:
	if not player.has_signal("died") or not player.has_signal("health_changed"):
		return "Keep both signals: health_changed(new_health) and died."
	var changes := []
	var deaths := [0]
	player.health_changed.connect(func(h): changes.append(h))
	player.died.connect(func(): deaths[0] += 1)

	player.take_damage(2)
	if player.health != 3:
		return "After take_damage(2) from 5, health is %s, expected 3." % str(player.health)
	if changes != [3]:
		return "health_changed should be emitted with 3. It was emitted with: %s" % str(changes)
	if deaths[0] != 0:
		return "died was emitted, but the player still has 3 health."

	player.take_damage(10)
	if player.health != 0:
		return "Health should stop at 0, but it's %s." % str(player.health)
	if deaths[0] != 1:
		return "died should be emitted once when health reaches 0. It was emitted %d times." % deaths[0]

	player.take_damage(1)
	if deaths[0] != 1:
		return "died was emitted again when the player was already at 0 health."
	return ""
