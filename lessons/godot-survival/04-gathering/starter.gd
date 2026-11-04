extends Node2D

signal dropped(item, amount)
signal depleted

var hits_left := 6
var tool_power := {"hand": 1, "stone_axe": 2, "iron_axe": 4}


func hit(tool: String) -> void:
	pass
