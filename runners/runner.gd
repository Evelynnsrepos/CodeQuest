# Runs a learner's GDScript inside headless Godot and reports back to server.py.
# Usage: godot --headless --script runner.gd -- user.gd [check.gd]
extends SceneTree


func _initialize() -> void:
	# --script mode leaves physics off; lessons need areas, rigid bodies and raycasts to work.
	PhysicsServer2D.set_active(true)
	PhysicsServer3D.set_active(true)
	physics_frame.connect(_physics_tick)
	_run()


func _run() -> void:
	var args := OS.get_cmdline_user_args()
	var learner = _compile(args[0])
	if learner == null:
		print("__CQ_COMPILE_ERROR__")
		quit(1)
		return

	print("__CQ_BEGIN__")
	var obj = learner.new()
	if obj is Node:
		# Wait one frame so the node is really in the scene tree and _ready() has run,
		# just like a node in a running game.
		root.add_child.call_deferred(obj)
		await process_frame
		if not obj.is_node_ready():
			await obj.ready

	if obj.has_method("run"):
		obj.run()
	_learner = obj
	var moves: bool = learner.source_code.contains("func _physics_process") or learner.source_code.contains("func _process")
	if args.size() == 1 and moves and (obj is Node2D or obj is Node3D):
		await _playground(obj)
	print("__CQ_END__")

	if args.size() > 1:
		var checker = _compile(args[1])
		var result := {"passed": false, "message": "The lesson's check script has an error."}
		if checker != null:
			_recording = true
			var message = await checker.new().check(obj)
			_recording = false
			if message == null:
				message = "The check stopped with an error. Look at the messages above."
			result = {"passed": message == "", "message": message}
		print("__CQ_CHECK__ ", JSON.stringify(result))

	_print_replay()
	quit(0)


# ---- Replay: what moved during Run or the check, drawn as boxes in the lesson page ----

const MAX_SAMPLES := 180   # every 2nd physics frame, so about 6 seconds
const MAX_NODES := 40
var _learner
var _recording := false
var _frames: Array = []
var _tick := 0


func _physics_tick() -> void:
	_tick += 1
	if not _recording or _tick % 2 or _frames.size() >= MAX_SAMPLES or not is_instance_valid(_learner):
		return
	var frame: Array = []
	_collect(root, frame)
	_frames.append(frame)


# One entry per node: [id, kind, x, y, w, h] in 2D, [id, kind, x, y, z, w, h, d] in 3D.
# kind: 0 = the learner's node, 1 = solid (StaticBody), 2 = area, 3 = other bodies and spawned nodes.
func _collect(node: Node, frame: Array) -> void:
	for child in node.get_children():
		if frame.size() >= MAX_NODES:
			return
		var kind := -1
		if child == _learner:
			kind = 0
		elif child is StaticBody2D or child is StaticBody3D:
			kind = 1
		elif child is Area2D or child is Area3D:
			kind = 2
		elif child is CollisionObject2D or child is CollisionObject3D or child.get_script() != null:
			kind = 3
		if kind >= 0 and child is Node2D:
			var s := _size_2d(child)
			frame.append([child.get_instance_id() % 100000, kind, roundf(child.global_position.x), roundf(child.global_position.y), s.x, s.y])
		elif kind >= 0 and child is Node3D:
			var s := _size_3d(child)
			var g: Vector3 = child.global_position
			frame.append([child.get_instance_id() % 100000, kind, snappedf(g.x, 0.01), snappedf(g.y, 0.01), snappedf(g.z, 0.01), s.x, s.y, s.z])
		_collect(child, frame)


func _size_2d(node: Node) -> Vector2:
	for c in node.get_children():
		if c is CollisionShape2D and c.shape:
			if c.shape is RectangleShape2D:
				return c.shape.size
			if c.shape is CircleShape2D:
				return Vector2.ONE * c.shape.radius * 2
			if c.shape is CapsuleShape2D:
				return Vector2(c.shape.radius * 2, c.shape.height)
	return Vector2(16, 16)


func _size_3d(node: Node) -> Vector3:
	for c in node.get_children():
		if c is CollisionShape3D and c.shape:
			if c.shape is BoxShape3D:
				return c.shape.size
			if c.shape is SphereShape3D:
				return Vector3.ONE * c.shape.radius * 2
			if c.shape is CapsuleShape3D or c.shape is CylinderShape3D:
				return Vector3(c.shape.radius * 2, c.shape.height, c.shape.radius * 2)
	return Vector3(0.5, 0.5, 0.5)


func _print_replay() -> void:
	if _frames.size() < 2 or _frames.all(func(f): return f == _frames[0]):
		return  # nothing moved, nothing to watch
	print("__CQ_REPLAY__ ", JSON.stringify({"dim": 3 if _learner is Node3D else 2, "frames": _frames}))


# ---- Run in a test scene: a floor, scripted key presses and a short log ----

const SCRIPT_KEYS := [[10, 50, "ui_right"], [55, 58, "ui_accept"], [65, 85, "ui_up"], [95, 135, "ui_left"]]


func _playground(obj) -> void:
	var is_2d: bool = obj is Node2D
	if obj is CharacterBody2D or obj is CharacterBody3D:
		await _add_floor(obj, is_2d)
	print("Test scene: CodeQuest holds → for 0.7 s, taps Space (ui_accept), holds ↑, then holds ←.")
	print("time    position        velocity")
	_recording = true
	for f in 150:
		for k in SCRIPT_KEYS:
			if f == k[0]:
				Input.action_press(k[2])
			elif f == k[1]:
				Input.action_release(k[2])
		if f % 15 == 0:
			_log_line(obj, f)
		await physics_frame
	_recording = false
	_log_line(obj, 150)
	print("Open the Replay below to watch it. Change a number and press Run again to compare.")


func _log_line(obj, f: int) -> void:
	var line := "%.2f s  " % (f / 60.0)
	if obj is Node2D:
		line += "(%.0f, %.0f)" % [obj.position.x, obj.position.y]
	else:
		line += "(%.2f, %.2f, %.2f)" % [obj.position.x, obj.position.y, obj.position.z]
	if "velocity" in obj:
		var v = obj.velocity
		line += "   (%.0f, %.0f)" % [v.x, v.y] if v is Vector2 else "   (%.1f, %.1f, %.1f)" % [v.x, v.y, v.z]
	if obj.has_method("is_on_floor"):
		line += "   on floor" if obj.is_on_floor() else "   in the air"
	print(line)


func _add_floor(obj, is_2d: bool) -> void:
	var floor_body
	if is_2d:
		if not obj.get_children().any(func(c): return c is CollisionShape2D):
			var shape := CollisionShape2D.new()
			shape.shape = RectangleShape2D.new()
			shape.shape.size = Vector2(20, 30)
			obj.add_child(shape)
		floor_body = StaticBody2D.new()
		var fs := CollisionShape2D.new()
		fs.shape = RectangleShape2D.new()
		fs.shape.size = Vector2(2000, 100)
		floor_body.add_child(fs)
		floor_body.position = Vector2(0, 50)
		if obj.position == Vector2.ZERO:
			obj.position = Vector2(0, -15)
	else:
		if not obj.get_children().any(func(c): return c is CollisionShape3D):
			var shape := CollisionShape3D.new()
			shape.shape = CapsuleShape3D.new()
			obj.add_child(shape)
		floor_body = StaticBody3D.new()
		var fs := CollisionShape3D.new()
		fs.shape = BoxShape3D.new()
		fs.shape.size = Vector3(100, 1, 100)
		floor_body.add_child(fs)
		floor_body.position = Vector3(0, -0.5, 0)
		if obj.position == Vector3.ZERO:
			obj.position = Vector3(0, 1, 0)
	root.add_child(floor_body)
	for i in 3:
		await physics_frame


func _compile(path: String):
	var script := GDScript.new()
	script.source_code = FileAccess.get_file_as_string(path)
	if script.reload() != OK:
		return null
	return script
