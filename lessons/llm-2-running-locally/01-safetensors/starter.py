import json
import math


def read_header(data):
    n = 0  # the header length from the first 8 bytes
    return {}


def count_params(header):
    total = 0
    return total


# a tiny fake model file: a 2-layer network
fake_header = {
    "embed.weight": {"dtype": "BF16", "shape": [1000, 64], "data_offsets": [0, 128000]},
    "layer.0.weight": {"dtype": "BF16", "shape": [64, 64], "data_offsets": [128000, 136192]},
    "layer.0.bias": {"dtype": "BF16", "shape": [64], "data_offsets": [136192, 136320]},
    "__metadata__": {"format": "pt"},
}
text = json.dumps(fake_header).encode("utf-8")
data = len(text).to_bytes(8, "little") + text + bytes(136320)

header = read_header(data)
print(sorted(header))
print(count_params(header), "parameters")
