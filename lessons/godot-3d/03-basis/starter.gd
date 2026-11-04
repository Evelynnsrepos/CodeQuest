extends CharacterBody3D

var speed := 4.0
var turn_speed := 2.0     # radians per second


func _physics_process(delta):
	# 1. turn
	# 2. read forward / back
	# 3. world direction from the basis
	move_and_slide()
