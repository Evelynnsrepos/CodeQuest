extends Node2D

var health := 5
var invincible_duration := 1.0
var invincible_time := 0.0


func take_damage(amount: int) -> void:
	health -= amount


func _process(delta):
	pass
