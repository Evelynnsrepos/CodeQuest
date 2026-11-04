extends Node2D

signal dropped(item, amount)
signal depleted

var hits_left := 6
var tool_power := {"hand": 1, "stone_axe": 2, "iron_axe": 4}


func hit(tool: String) -> void:
	if hits_left == 0:
		return
	var amount := mini(tool_power.get(tool, 1), hits_left)
	hits_left -= amount
	dropped.emit("wood", amount)
	if hits_left == 0:
		depleted.emit()
		queue_free()
