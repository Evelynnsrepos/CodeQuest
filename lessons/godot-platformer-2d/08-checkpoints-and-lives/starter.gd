extends CharacterBody2D

signal game_over

var lives := 3
var checkpoint := Vector2.ZERO
var death_y := 1000.0


func _physics_process(delta):
	pass


func set_checkpoint(spot: Vector2) -> void:
	pass


func die() -> void:
	pass
