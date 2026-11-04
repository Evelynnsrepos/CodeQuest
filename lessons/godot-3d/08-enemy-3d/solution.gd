extends CharacterBody3D

var speed := 3.0
var attack_range := 1.5
var attacks := 0
var target := Vector3.ZERO


func _physics_process(delta):
	hunt(target)


func attack() -> void:
	attacks += 1


func hunt(target: Vector3) -> void:
	var flat := target - global_position
	flat.y = 0
	if flat.length() > attack_range:
		var direction := flat.normalized()
		velocity.x = direction.x * speed
		velocity.z = direction.z * speed
		look_at(Vector3(target.x, global_position.y, target.z))
	else:
		velocity.x = 0
		velocity.z = 0
		attack()
	move_and_slide()
