func take_damage(health: int, damage: int) -> int:
	return max(health - damage, 0)


func run():
	print(take_damage(100, 30))
