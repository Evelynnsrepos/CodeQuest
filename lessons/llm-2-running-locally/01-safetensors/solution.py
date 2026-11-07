import json


def read_header(data):
    n = int.from_bytes(data[0:8], "little")
    return json.loads(data[8:8 + n].decode("utf-8"))


def count_params(header):
    total = 0
    for name in header:
        if name == "__metadata__":
            continue
        size = 1
        for number in header[name]["shape"]:
            size = size * number
        total = total + size
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
