extends AnimatableBody3D

var axis := Vector3(1, 0, 0)
var distance := 3.0
var period := 4.0
var start := Vector3.ZERO
var time := 0.0


func _physics_process(delta):
	time += delta
	position = start + axis * sin(time / period * TAU) * distance
