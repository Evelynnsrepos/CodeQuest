extends Node2D

enum State { WANDER, CHASE, ATTACK, FLEE }

var state := State.WANDER
var health := 50
var max_health := 50
var sight_range := 200.0
var attack_range := 30.0


func think(distance: float) -> void:
	pass
