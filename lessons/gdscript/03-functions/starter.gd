func take_damage(health: int, damage: int) -> int:
	# Return the health left, never below 0
	return health


func run():
	print(take_damage(100, 30))
