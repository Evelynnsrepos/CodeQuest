extends CharacterBody3D

var speed := 4.0
var turn_speed := 2.0     # radians per second


func _physics_process(delta):
	var turn := Input.get_axis("ui_right", "ui_left")
	rotation.y += turn * turn_speed * delta
	var forward := Input.get_axis("ui_up", "ui_down")
	var direction := transform.basis * Vector3(0, 0, forward)
	velocity.x = direction.x * speed
	velocity.z = direction.z * speed
	move_and_slide()
