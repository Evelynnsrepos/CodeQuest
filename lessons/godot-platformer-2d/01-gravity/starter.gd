extends CharacterBody2D

var gravity := 980.0
var max_fall_speed := 600.0


func _physics_process(delta):
	# 1. fall faster when not on the floor
	# 2. limit the falling speed
	move_and_slide()
