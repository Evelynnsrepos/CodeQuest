extends Node2D

var cooldown_time := 0.5
var _cooldown := 0.0


func _process(delta):
	_cooldown = max(_cooldown - delta, 0.0)


func try_shoot() -> bool:
	if _cooldown > 0.0:
		return false
	_cooldown = cooldown_time
	return true
