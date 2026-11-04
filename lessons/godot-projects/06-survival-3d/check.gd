func check(m) -> String:
	var tree: SceneTree = m.get_tree()
	if m.process_mode != Node.PROCESS_MODE_ALWAYS:
		return "In _ready() set process_mode to Node.PROCESS_MODE_ALWAYS, so the menu works while paused."
	if m.visible:
		return "The menu should start hidden."
	m.toggle_pause()
	var paused := tree.paused
	var shown: bool = m.visible
	m.toggle_pause()
	if not paused:
		return "toggle_pause() should pause the game (get_tree().paused = true)."
	if not shown:
		return "The menu should be visible while paused."
	if tree.paused:
		return "A second toggle_pause() should unpause the game."
	if m.visible:
		return "The menu should hide again when the game resumes."
	return ""
