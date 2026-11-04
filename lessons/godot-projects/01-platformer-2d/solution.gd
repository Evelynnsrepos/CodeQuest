extends Node

var levels := ["res://levels/level_1.tscn", "res://levels/level_2.tscn", "res://levels/level_3.tscn"]
var current := 0
var coins := 0
var lives := 3


func collect_coin() -> void:
	coins += 1
	if coins == 100:
		lives += 1
		coins = 0


func next_level() -> String:
	current += 1
	if current >= levels.size():
		return "res://win_screen.tscn"
	return levels[current]
