extends CharacterBody2D

var gravity := 980.0
var max_fall_speed := 600.0


func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta
	velocity.y = minf(velocity.y, max_fall_speed)
	move_and_slide()
