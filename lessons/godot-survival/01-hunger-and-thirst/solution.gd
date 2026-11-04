extends Node

var health := 100.0
var hunger := 100.0
var thirst := 100.0
var hunger_rate := 1.0
var thirst_rate := 2.0
var starve_damage := 5.0


func _process(delta):
	hunger = clampf(hunger - hunger_rate * delta, 0.0, 100.0)
	thirst = clampf(thirst - thirst_rate * delta, 0.0, 100.0)
	if hunger == 0 or thirst == 0:
		health -= starve_damage * delta


func eat(amount: float) -> void:
	hunger = clampf(hunger + amount, 0.0, 100.0)
