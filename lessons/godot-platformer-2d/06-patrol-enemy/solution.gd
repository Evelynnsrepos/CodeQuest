extends CharacterBody2D

var gravity := 980.0
var speed := 160.0
var direction := 1
var ledge_ray := RayCast2D.new()


func _ready():
	ledge_ray.position = Vector2(16, 0)
	ledge_ray.target_position = Vector2(0, 40)
	add_child(ledge_ray)


func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta

	if is_on_floor() and (is_on_wall() or not ledge_ray.is_colliding()):
		direction *= -1
		ledge_ray.position.x = 16 * direction
		ledge_ray.force_raycast_update()

	velocity.x = direction * speed
	move_and_slide()
