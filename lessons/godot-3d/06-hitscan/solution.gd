extends Node3D

var damage := 25
var max_range := 50.0


func shoot() -> Node:
	var from := global_position
	var to := from + -global_transform.basis.z * max_range
	var query := PhysicsRayQueryParameters3D.create(from, to)
	var hit := get_world_3d().direct_space_state.intersect_ray(query)
	if hit.is_empty():
		return null
	if hit.collider.has_method("take_damage"):
		hit.collider.take_damage(damage)
	return hit.collider
