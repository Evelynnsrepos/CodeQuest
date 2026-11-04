extends CharacterBody3D

var sensitivity := 0.003    # radians per pixel
var head := Node3D.new()


func _ready():
	head.name = "Head"
	add_child(head)


func _unhandled_input(event):
	pass
