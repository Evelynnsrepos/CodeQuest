extends Node3D

var ray := RayCast3D.new()


func _ready():
	ray.target_position = Vector3(0, 0, -2.5)
	add_child(ray)


func looking_at() -> Node:
	if ray.is_colliding() and ray.get_collider().has_method("interact"):
		return ray.get_collider()
	return null


func prompt_text() -> String:
	var thing := looking_at()
	if thing == null:
		return ""
	return "[E] " + thing.prompt


func try_interact() -> bool:
	var thing := looking_at()
	if thing == null:
		return false
	thing.interact(self)
	return true
