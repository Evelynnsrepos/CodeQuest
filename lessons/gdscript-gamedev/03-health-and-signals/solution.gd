extends Node2D

signal health_changed(new_health)
signal died

var health := 5


func take_damage(amount: int) -> void:
	if health == 0:
		return
	health = max(health - amount, 0)
	health_changed.emit(health)
	if health == 0:
		died.emit()
