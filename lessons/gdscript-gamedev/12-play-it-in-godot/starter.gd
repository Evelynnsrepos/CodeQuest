extends Node2D

var speed := 300.0
var play_area := Rect2(0, 0, 1152, 648)


func _process(delta):
	var direction := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	position += direction * speed * delta
	# keep the player inside play_area here
