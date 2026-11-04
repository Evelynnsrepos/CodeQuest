extends Node2D

@export var bullet_scene: PackedScene
var muzzle_distance := 20.0
var cooldown_time := 0.25
var _cooldown := 0.0


func _process(delta):
	_cooldown = maxf(_cooldown - delta, 0.0)


func shoot() -> Node2D:
	return null
