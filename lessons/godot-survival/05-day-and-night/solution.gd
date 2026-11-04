extends Node

var day_length := 600.0
var time_of_day := 8.0
var night_brightness := 0.2


func _process(delta):
	time_of_day = fposmod(time_of_day + 24.0 / day_length * delta, 24.0)


func brightness() -> float:
	var angle := time_of_day / 24.0 * TAU
	var day_amount := (1.0 - cos(angle)) / 2.0
	return lerpf(night_brightness, 1.0, day_amount)


func is_night() -> bool:
	return time_of_day >= 20 or time_of_day < 6
