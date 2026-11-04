extends CharacterBody2D

var facing_left := false


func pick_animation(on_floor: bool) -> String:
	return "idle"


func update_facing() -> void:
	pass
