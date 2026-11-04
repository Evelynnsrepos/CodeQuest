extends Node2D


func aim_at(target: Vector2) -> void:
	# 1. arrow from me to the target
	# 2. its angle goes into rotation
	pass


func _process(delta):
	aim_at(get_global_mouse_position())
