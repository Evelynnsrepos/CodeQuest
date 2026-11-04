extends CharacterBody3D


func move_direction(input: Vector2, camera_yaw: float) -> Vector3:
	return Basis(Vector3.UP, camera_yaw) * Vector3(input.x, 0, input.y)


func face(direction: Vector3) -> void:
	if direction.length() > 0:
		look_at(global_position + direction)
