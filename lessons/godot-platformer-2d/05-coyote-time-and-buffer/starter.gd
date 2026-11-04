extends CharacterBody2D

var gravity := 980.0
var speed := 200.0
var jump_velocity := -400.0
var coyote_time := 0.1
var buffer_time := 0.1
var coyote_timer := 0.0
var buffer_timer := 0.0


func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta

	# update the two timers, then jump when both are above 0
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = jump_velocity

	velocity.x = Input.get_axis("ui_left", "ui_right") * speed
	move_and_slide()
