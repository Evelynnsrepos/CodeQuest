extends CharacterBody2D

var gravity := 980.0
var speed := 300.0
var jump_height := 64.0
var jump_velocity := 0.0   # work this out from jump_height and gravity


func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta

	# jump here

	velocity.x = Input.get_axis("ui_left", "ui_right") * speed
	move_and_slide()
