extends Area2D

var speed := 600.0
var lifetime := 1.0


func _physics_process(delta):
	position += Vector2.from_angle(rotation) * speed * delta
	lifetime -= delta
	if lifetime <= 0:
		queue_free()
