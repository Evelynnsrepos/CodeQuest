import math


def effective_batch(per_device, accumulation, gpus=1):
    return 0


def total_steps(examples, per_device, accumulation, epochs, gpus=1):
    return 0


def warnings_for(config):
    warnings = []
    return warnings


good = {"lr": 2e-4, "epochs": 3, "examples": 600, "per_device": 2, "accumulation": 8}
risky = {"lr": 1e-3, "epochs": 10, "examples": 40, "per_device": 1, "accumulation": 2}
for name, cfg in [("good", good), ("risky", risky)]:
    steps = total_steps(cfg["examples"], cfg["per_device"], cfg["accumulation"], cfg["epochs"])
    print(f"{name}: effective batch {effective_batch(cfg['per_device'], cfg['accumulation'])}, {steps} steps, warnings: {warnings_for(cfg)}")
