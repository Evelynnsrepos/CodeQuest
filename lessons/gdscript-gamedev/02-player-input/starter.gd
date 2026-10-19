extends Node2D

var speed := 300.0


func _process(delta):
	var direction := Vector2.ZERO
	# Read the arrow keys with Input.get_vector(...)
	position += direction * speed * delta
