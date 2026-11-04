extends CharacterBody2D

var health := 3
var bounce_velocity := -300.0


func touch_enemy(enemy: Node2D) -> String:
	if velocity.y > 0 and position.y < enemy.position.y - 8:
		enemy.queue_free()
		velocity.y = bounce_velocity
		return "stomp"
	health -= 1
	return "hurt"
