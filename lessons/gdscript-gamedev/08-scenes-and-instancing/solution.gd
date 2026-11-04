extends Node2D

@export var coin_scene: PackedScene


func spawn_at(spot: Vector2) -> Node:
	var coin := coin_scene.instantiate()
	coin.position = spot
	add_child(coin)
	return coin
