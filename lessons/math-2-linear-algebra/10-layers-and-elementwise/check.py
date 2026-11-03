rl, hd, lp = ns.get("relu_layer"), ns.get("hadamard"), ns.get("layer_params")
assert rl and hd and lp, "Keep relu_layer, hadamard and layer_params."
assert rl([[1, -1], [2, 0]], [0, -4], [3, 5]) == [0, 2], f"Should be [0, 2], got {rl([[1, -1], [2, 0]], [0, -4], [3, 5])!r}."
assert rl([[1, 0], [0, 1], [1, 1]], [1, 1, 1], [2, -5]) == [3, 0, 0], "A 3×2 layer gives 3 outputs; negatives become 0."
assert hd([1, 2, 3], [4, 5, 6]) == [4, 10, 18], f"hadamard gives a vector [4, 10, 18], not the dot product. Got {hd([1, 2, 3], [4, 5, 6])!r}."
assert lp(3, 2) == 8 and lp(4096, 14336) == 4096 * 14336 + 14336, "Weights d_in·d_out plus d_out biases."
