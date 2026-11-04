extends Control


func _ready():
	process_mode = Node.PROCESS_MODE_ALWAYS
	visible = false


func toggle_pause() -> void:
	get_tree().paused = not get_tree().paused
	visible = get_tree().paused
