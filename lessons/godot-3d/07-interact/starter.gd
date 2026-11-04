extends Node3D

var ray := RayCast3D.new()


func _ready():
	ray.target_position = Vector3(0, 0, -2.5)
	add_child(ray)


func looking_at() -> Node:
	return null


func prompt_text() -> String:
	return ""


func try_interact() -> bool:
	return false
