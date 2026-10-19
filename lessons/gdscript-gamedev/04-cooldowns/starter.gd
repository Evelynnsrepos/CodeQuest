extends Node2D

var cooldown_time := 0.5
var _cooldown := 0.0


func _process(delta):
	# Count _cooldown down towards 0
	pass


func try_shoot() -> bool:
	# Return false while cooling down, otherwise start the cooldown and return true
	return true
