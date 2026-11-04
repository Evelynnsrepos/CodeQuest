extends Node

var weapons := [
	{"name": "pistol", "damage": 20},
	{"name": "shotgun", "damage": 60},
	{"name": "rifle", "damage": 35},
]
var current := 0


func cycle(step: int) -> void:
	current = posmod(current + step, weapons.size())


func select(index: int) -> void:
	if index >= 0 and index < weapons.size():
		current = index


func current_damage() -> int:
	return weapons[current].damage
