extends Node3D


func ground_distance(a: Vector3, b: Vector3) -> float:
	var flat := b - a
	flat.y = 0
	return flat.length()


func ground_direction(a: Vector3, b: Vector3) -> Vector3:
	var flat := b - a
	flat.y = 0
	return flat.normalized()
