extends Node2D


func aim_at(target: Vector2) -> void:
	rotation = (target - global_position).angle()


func _process(delta):
	aim_at(get_global_mouse_position())
