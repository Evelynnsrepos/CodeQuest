func check(w) -> String:
	var area := Rect2(100, 50, 800, 600)
	var pts = w.scatter(40, area, 60)
	if pts.size() != 40:
		return "scatter(40, an 800×600 area, 60) should find 40 points, got %d." % pts.size()
	for p in pts:
		if not area.has_point(p):
			return "%s is outside the area %s." % [str(p), str(area)]
	for i in pts.size():
		for j in range(i + 1, pts.size()):
			if pts[i].distance_to(pts[j]) < 60:
				return "%s and %s are only %.1f apart, closer than min_gap (60)." % [str(pts[i]), str(pts[j]), pts[i].distance_to(pts[j])]
	var crowded = w.scatter(50, Rect2(0, 0, 100, 100), 80)
	if crowded.size() > 4:
		return "In a 100×100 area with gap 80 only a few points fit, but scatter returned %d." % crowded.size()
	if crowded.size() == 0:
		return "scatter should still return the points that fit."
	return ""
