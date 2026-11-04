import math
import struct
ep, mv, rb, bf = ns.get("epsilon"), ns.get("max_value"), ns.get("round_to_bits"), ns.get("bytes_for")
assert ep and mv and rb and bf, "Keep epsilon, max_value, round_to_bits and bytes_for."
assert ep(7) == 2 ** -7 and ep(23) == 2 ** -23, "epsilon(m) = 2^−m."
assert mv(5, 10) == 65504, f"FP16 max is 65504, got {mv(5, 10)!r}."
assert abs(mv(8, 7) / 3.3895313892515355e38 - 1) < 1e-12, "BF16 max ≈ 3.39e38."
assert abs(mv(8, 23) / 3.4028234663852886e38 - 1) < 1e-12, "FP32 max ≈ 3.40e38."
assert rb(1.001, 7) == 1.0, f"In BF16, 1.001 rounds to 1.0 (the update is lost), got {rb(1.001, 7)!r}."
assert rb(1 + 2 ** -7, 7) == 1 + 2 ** -7, "1 + ε is representable."
for x in (0.1, 3.14159, -1234.5678, 6.5e-3):
    want = struct.unpack("e", struct.pack("e", x))[0]
    assert rb(x, 10) == want, f"round_to_bits({x}, 10) should match real FP16: {want}, got {rb(x, 10)!r}."
assert bf(7e9, "bf16") == 14e9 and bf(1000, "fp32") == 4000 and bf(8, "fp8") == 8, "bytes_for: 4, 2, 2, 1 bytes per parameter."
