func check(node) -> String:
	if not node is Node2D:
		return "Keep \"extends Node2D\" at the top so your node has a position."
	node.position = Vector2.ZERO
	node._process(0.5)
	if not node.position.is_equal_approx(Vector2(50, 0)):
		return "After _process(0.5) the node is at %s, expected (50, 0)." % str(node.position)
	node._process(0.25)
	if not node.position.is_equal_approx(Vector2(75, 0)):
		return "After another _process(0.25) the node is at %s, expected (75, 0)." % str(node.position)
	return ""
