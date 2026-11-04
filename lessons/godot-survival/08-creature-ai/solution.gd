extends Node2D

enum State { WANDER, CHASE, ATTACK, FLEE }

var state := State.WANDER
var health := 50
var max_health := 50
var sight_range := 200.0
var attack_range := 30.0


func think(distance: float) -> void:
	if health < max_health * 0.3:
		state = State.FLEE
		return
	match state:
		State.WANDER:
			if distance < sight_range:
				state = State.CHASE
		State.CHASE:
			if distance <= attack_range:
				state = State.ATTACK
			elif distance > sight_range * 1.5:
				state = State.WANDER
		State.ATTACK:
			if distance > attack_range:
				state = State.CHASE
