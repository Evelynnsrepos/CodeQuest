an, mv, di, pe, lp = (ns.get(n) for n in ("angle_deg", "matvec", "distance", "perpendicular", "layer_params"))
assert all((an, mv, di, pe, lp)), "Keep all five functions."
assert abs(an([1, 0], [1, 1]) - 45) < 1e-6 and abs(an([1, 0], [-1, 0]) - 180) < 1e-6 and abs(an([3, 0], [0, 2]) - 90) < 1e-6, "1. angle_deg: arccos of the cosine, in degrees."
assert list(mv([[1, 2], [3, 4]], [1, 1])) == [3, 7] and list(mv([[1, 0, 2]], [1, 2, 3])) == [7], "2. matvec: each row dotted with v."
assert abs(di([1, 2], [4, 6]) - 5) < 1e-12, "3. distance: √(9 + 16) = 5."
assert pe([2, 1], [-1, 2]) is True and pe([1, 1], [1, 0]) is False, "4. perpendicular: dot product 0."
assert lp(768, 3072) == 2362368 and lp(2, 1) == 3, "5. layer_params: n_out · n_in + n_out."
