extends Node2D


func knockback(enemy_position: Vector2, strength: float) -> void:
	var away := (position - enemy_position).normalized()
	position += away * strength
