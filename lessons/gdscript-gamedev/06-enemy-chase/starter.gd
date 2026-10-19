extends Node2D

var speed := 80.0
var sight_range := 200.0


func can_see(target: Vector2) -> bool:
	return false


func chase(target: Vector2, delta: float) -> void:
	pass
