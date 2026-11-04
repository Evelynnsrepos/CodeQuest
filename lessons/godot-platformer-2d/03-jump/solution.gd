extends CharacterBody2D

var gravity := 980.0
var speed := 300.0
var jump_height := 64.0
var jump_velocity := -sqrt(2.0 * gravity * jump_height)


func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta

	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = jump_velocity

	velocity.x = Input.get_axis("ui_left", "ui_right") * speed
	move_and_slide()
