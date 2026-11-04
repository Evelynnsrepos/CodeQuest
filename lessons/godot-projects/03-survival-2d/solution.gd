extends Node2D


func scatter(count: int, area: Rect2, min_gap: float) -> Array:
	var points := []
	var tries := 0
	while points.size() < count and tries < count * 30:
		tries += 1
		var spot := Vector2(randf_range(area.position.x, area.end.x), randf_range(area.position.y, area.end.y))
		var ok := true
		for p in points:
			if p.distance_to(spot) < min_gap:
				ok = false
				break
		if ok:
			points.append(spot)
	return points
