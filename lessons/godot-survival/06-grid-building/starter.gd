extends Node2D

var cell_size := 32
var occupied := {}


func to_cell(world: Vector2) -> Vector2i:
	return Vector2i.ZERO


func cell_to_world(cell: Vector2i) -> Vector2:
	return Vector2.ZERO


func place(thing: String, world: Vector2) -> bool:
	return false
