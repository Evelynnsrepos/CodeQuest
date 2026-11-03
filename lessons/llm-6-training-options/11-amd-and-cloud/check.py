th, cc, dg = ns.get("training_hours"), ns.get("cloud_cost"), ns.get("diagnose")
assert th and cc and dg, "Keep training_hours, cloud_cost and diagnose."
assert abs(th(1000, 360, 2, 200) - 1.0) < 1e-9, f"training_hours(1000, 360, 2, 200) returned {th(1000, 360, 2, 200)!r}, expected 720,000 tokens / 200 / 3600 = 1.0."
assert abs(cc(2.0, 1.5) - 3.75) < 1e-9, f"cloud_cost(2, 1.5) returned {cc(2.0, 1.5)!r}, expected (2 + 0.5) × 1.5 = 3.75."
assert abs(cc(1.0, 2.0, 0) - 2.0) < 1e-9, "cloud_cost with setup_hours=0 is just hours × price."
assert dg(True, "6.2") == "ready", "A ROCm build that sees the GPU is ready."
assert dg(False, None) == "cpu-only build" and dg(True, None) == "cpu-only build", "hip_version None means PyTorch wasn't built for ROCm."
assert dg(False, "6.2") == "check HSA_OVERRIDE_GFX_VERSION and groups", "A ROCm build that can't see the GPU usually needs the override or group membership."
