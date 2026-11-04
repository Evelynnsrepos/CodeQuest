extends Node2D

var cell_size := 32
var occupied := {}


func to_cell(world: Vector2) -> Vector2i:
	return Vector2i((world / cell_size).floor())


func cell_to_world(cell: Vector2i) -> Vector2:
	return Vector2(cell * cell_size)


func place(thing: String, world: Vector2) -> bool:
	var cell := to_cell(world)
	if occupied.has(cell):
		return false
	occupied[cell] = thing
	return true
