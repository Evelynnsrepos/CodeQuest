extends CharacterBody3D

var sensitivity := 0.003    # radians per pixel
var head := Node3D.new()


func _ready():
	head.name = "Head"
	add_child(head)


func _unhandled_input(event):
	if event is InputEventMouseMotion:
		rotate_y(-event.relative.x * sensitivity)
		head.rotation.x = clampf(head.rotation.x - event.relative.y * sensitivity, deg_to_rad(-89), deg_to_rad(89))
