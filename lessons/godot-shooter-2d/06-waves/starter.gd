extends Node2D

signal wave_cleared(wave_number)

var wave := 0
var alive := 0


func spawn_enemy() -> Node:
	var enemy := Node2D.new()
	enemy.add_user_signal("died")
	add_child(enemy)
	return enemy


func start_wave() -> void:
	pass


func _on_enemy_died() -> void:
	pass
