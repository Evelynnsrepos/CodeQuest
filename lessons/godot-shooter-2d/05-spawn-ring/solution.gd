extends Node2D


func ring_points(center: Vector2, radius: float, count: int) -> Array:
	var points := []
	for i in count:
		points.append(center + Vector2.from_angle(TAU / count * i) * radius)
	return points


func random_point(center: Vector2, radius: float) -> Vector2:
	return center + Vector2.from_angle(randf() * TAU) * radius
