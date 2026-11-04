extends Node2D

var health := 5
var invincible_duration := 1.0
var invincible_time := 0.0


func take_damage(amount: int) -> void:
	if invincible_time > 0:
		return
	health -= amount
	invincible_time = invincible_duration


func _process(delta):
	invincible_time = maxf(invincible_time - delta, 0.0)
	if invincible_time > 0:
		visible = int(invincible_time * 10) % 2 == 0
	else:
		visible = true
