def split(data, val_fraction):
    n_val = int(len(data) * val_fraction)
    return data[:len(data) - n_val], data[len(data) - n_val:]


def best_epoch(val_losses):
    return val_losses.index(min(val_losses))


def overfitting_starts(train_losses, val_losses):
    for i in range(1, len(train_losses)):
        if train_losses[i] < train_losses[i - 1] and val_losses[i] > val_losses[i - 1]:
            return i
    return None


examples = [f"example {i}" for i in range(50)]
train, val = split(examples, 0.2)
print(len(train), "training,", len(val), "validation")

# a recorded fine-tuning run, one value per epoch
train_losses = [2.10, 1.62, 1.31, 1.12, 0.95, 0.80, 0.66, 0.52, 0.41, 0.30]
val_losses = [2.15, 1.70, 1.45, 1.33, 1.30, 1.32, 1.38, 1.47, 1.59, 1.74]
print("keep the checkpoint from epoch", best_epoch(val_losses))
print("overfitting starts at epoch", overfitting_starts(train_losses, val_losses))
