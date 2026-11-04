func check(d) -> String:
	d.set_process(false)
	d.time_of_day = 8.0
	d._process(150.0)
	if not is_equal_approx(d.time_of_day, 14.0):
		return "150 real seconds with a 600-second day is 6 in-game hours: 8 → 14. Got %s." % str(d.time_of_day)
	d._process(300.0)
	if not is_equal_approx(d.time_of_day, 2.0):
		return "From 14:00, 12 more hours should wrap to 2:00, but time_of_day is %s." % str(d.time_of_day)
	var cases = [[0.0, 0.2], [12.0, 1.0], [6.0, 0.6], [18.0, 0.6], [3.0, 0.2 + 0.8 * (1 - cos(PI / 4)) / 2]]
	for c in cases:
		d.time_of_day = c[0]
		if absf(d.brightness() - c[1]) > 0.001:
			return "At %s:00 brightness should be %.3f, got %.3f." % [str(c[0]), c[1], d.brightness()]
	for h in [20.0, 23.0, 0.0, 5.9]:
		d.time_of_day = h
		if not d.is_night():
			return "%s:00 should be night." % str(h)
	for h in [6.0, 12.0, 19.9]:
		d.time_of_day = h
		if d.is_night():
			return "%s:00 should be day." % str(h)
	return ""
