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
	wave += 1
	var count := 3 + 2 * wave
	for i in count:
		var enemy := spawn_enemy()
		enemy.connect("died", _on_enemy_died)
	alive = count


func _on_enemy_died() -> void:
	alive -= 1
	if alive == 0:
		wave_cleared.emit(wave)
