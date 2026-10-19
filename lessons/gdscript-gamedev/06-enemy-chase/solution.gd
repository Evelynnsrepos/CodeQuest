extends Node2D

var speed := 80.0
var sight_range := 200.0


func can_see(target: Vector2) -> bool:
	return position.distance_to(target) <= sight_range


func chase(target: Vector2, delta: float) -> void:
	if can_see(target):
		position = position.move_toward(target, speed * delta)
