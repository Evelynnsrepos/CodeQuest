extends CharacterBody2D

var gravity := 980.0
var max_speed := 300.0
var acceleration := 1200.0
var friction := 1500.0


func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta

	# horizontal movement goes here

	move_and_slide()
