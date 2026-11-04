extends CharacterBody2D

var gravity := 980.0
var max_speed := 300.0
var acceleration := 1200.0
var friction := 1500.0


func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta

	var direction := Input.get_axis("ui_left", "ui_right")
	if direction != 0:
		velocity.x = move_toward(velocity.x, direction * max_speed, acceleration * delta)
	else:
		velocity.x = move_toward(velocity.x, 0, friction * delta)

	move_and_slide()
