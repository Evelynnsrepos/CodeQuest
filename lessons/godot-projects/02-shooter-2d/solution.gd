extends Node

var start_interval := 2.0
var min_interval := 0.4
var high_score := 0


func spawn_interval(wave: int) -> float:
	return maxf(start_interval * pow(0.85, wave - 1), min_interval)


func game_over(score: int) -> bool:
	if score > high_score:
		high_score = score
		return true
	return false
