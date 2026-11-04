extends Node

var start_interval := 2.0
var min_interval := 0.4
var high_score := 0


func spawn_interval(wave: int) -> float:
	return start_interval


func game_over(score: int) -> bool:
	return false
