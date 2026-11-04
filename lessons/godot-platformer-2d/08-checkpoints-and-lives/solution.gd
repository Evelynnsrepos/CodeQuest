extends CharacterBody2D

signal game_over

var lives := 3
var checkpoint := Vector2.ZERO
var death_y := 1000.0


func _physics_process(delta):
	if position.y > death_y:
		die()


func set_checkpoint(spot: Vector2) -> void:
	checkpoint = spot


func die() -> void:
	lives -= 1
	if lives > 0:
		position = checkpoint
		velocity = Vector2.ZERO
	else:
		game_over.emit()
