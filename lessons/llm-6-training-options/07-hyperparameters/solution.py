import math


def effective_batch(per_device, accumulation, gpus=1):
    return per_device * accumulation * gpus


def total_steps(examples, per_device, accumulation, epochs, gpus=1):
    batch = effective_batch(per_device, accumulation, gpus)
    return math.ceil(examples / batch) * epochs


def warnings_for(config):
    warnings = []
    eb = effective_batch(config["per_device"], config["accumulation"])
    steps = total_steps(config["examples"], config["per_device"], config["accumulation"], config["epochs"])
    if config["lr"] > 5e-4:
        warnings.append("learning rate too high")
    if config["lr"] < 1e-5:
        warnings.append("learning rate too low")
    if config["epochs"] > 5:
        warnings.append("too many epochs")
    if eb < 8:
        warnings.append("effective batch too small")
    if steps < 20:
        warnings.append("very few steps")
    return warnings


good = {"lr": 2e-4, "epochs": 3, "examples": 600, "per_device": 2, "accumulation": 8}
risky = {"lr": 1e-3, "epochs": 10, "examples": 40, "per_device": 1, "accumulation": 2}
for name, cfg in [("good", good), ("risky", risky)]:
    steps = total_steps(cfg["examples"], cfg["per_device"], cfg["accumulation"], cfg["epochs"])
    print(f"{name}: effective batch {effective_batch(cfg['per_device'], cfg['accumulation'])}, {steps} steps, warnings: {warnings_for(cfg)}")
