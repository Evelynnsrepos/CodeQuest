extends Node

var day_length := 600.0
var time_of_day := 8.0
var night_brightness := 0.2


func _process(delta):
	pass


func brightness() -> float:
	return 1.0


func is_night() -> bool:
	return false
