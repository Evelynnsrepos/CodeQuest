extends CharacterBody2D

var facing_left := false


func pick_animation(on_floor: bool) -> String:
	if not on_floor:
		return "jump" if velocity.y < 0 else "fall"
	if velocity.x != 0:
		return "run"
	return "idle"


func update_facing() -> void:
	if velocity.x != 0:
		facing_left = velocity.x < 0
