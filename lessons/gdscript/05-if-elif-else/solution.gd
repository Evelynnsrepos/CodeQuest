func damage_multiplier(element: String, enemy: String) -> float:
	if element == "fire" and enemy == "ice":
		return 2.0
	elif element == "water" and enemy == "fire":
		return 2.0
	elif element == enemy:
		return 0.5
	return 1.0


func run():
	print(damage_multiplier("fire", "ice"))
