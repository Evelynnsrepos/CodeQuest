extends CharacterBody3D


func move_direction(input: Vector2, camera_yaw: float) -> Vector3:
	return Vector3(input.x, 0, input.y)


func face(direction: Vector3) -> void:
	pass
