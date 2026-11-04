func check(hud) -> String:
	hud.on_score_changed(42)
	if hud.score_label.text != "Score: 42":
		return "After on_score_changed(42) the label says \"%s\", expected \"Score: 42\"." % hud.score_label.text
	hud.on_health_changed(30, 120)
	if hud.health_bar.max_value != 120 or hud.health_bar.value != 30:
		return "After on_health_changed(30, 120) the bar is %s out of %s, expected 30 out of 120." % [str(hud.health_bar.value), str(hud.health_bar.max_value)]
	return ""
