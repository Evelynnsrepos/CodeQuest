extends Node2D

var velocity := Vector2(100, 0)


func _process(delta):
	position += velocity * delta
