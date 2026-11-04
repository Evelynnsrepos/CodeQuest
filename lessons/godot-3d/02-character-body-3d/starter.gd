extends CharacterBody3D

var speed := 5.0          # metres per second: 3D units are usually metres
var jump_velocity := 4.5
var gravity := 9.8


func _physics_process(delta):
	move_and_slide()
