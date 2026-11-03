def training_hours(examples, avg_tokens, epochs, tokens_per_second):
    return examples * avg_tokens * epochs / tokens_per_second / 3600


def cloud_cost(hours, price_per_hour, setup_hours=0.5):
    return (hours + setup_hours) * price_per_hour


def diagnose(cuda_available, hip_version):
    if hip_version is None:
        return "cpu-only build"
    if cuda_available:
        return "ready"
    return "check HSA_OVERRIDE_GFX_VERSION and groups"


h = training_hours(800, 450, 3, 1500)
print(f"800 examples × 450 tokens × 3 epochs at 1,500 tok/s: {h:.2f} hours")
print(f"on a €0.80/h cloud GPU: €{cloud_cost(h, 0.80):.2f}")
print(diagnose(True, "6.4.43482"), "|", diagnose(False, None), "|", diagnose(False, "6.4.43482"))
