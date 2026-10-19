# Runs a learner's GDScript inside headless Godot and reports back to server.py.
# Usage: godot --headless --script runner.gd -- user.gd [check.gd]
extends SceneTree


func _initialize() -> void:
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
	print("__CQ_END__")

	if args.size() > 1:
		var checker = _compile(args[1])
		var result := {"passed": false, "message": "The lesson's check script has an error."}
		if checker != null:
			var message = checker.new().check(obj)
			if message == null:
				message = "The check stopped with an error. Look at the messages above."
			result = {"passed": message == "", "message": message}
		print("__CQ_CHECK__ ", JSON.stringify(result))

	quit(0)


func _compile(path: String):
	var script := GDScript.new()
	script.source_code = FileAccess.get_file_as_string(path)
	if script.reload() != OK:
		return null
	return script
