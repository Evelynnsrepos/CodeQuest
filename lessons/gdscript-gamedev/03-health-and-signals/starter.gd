extends Node2D

signal health_changed(new_health)
signal died

var health := 5


func take_damage(amount: int) -> void:
	# 1. lower health (never below 0)
	# 2. emit health_changed
	# 3. emit died when health reaches 0
	pass
