---
title: LM Studio, Ollama, llama.cpp, Lemonade
minutes: 15
xp: 25
hint: The ports are in the table above: LM Studio 1234, Ollama 11434, llama.cpp 8080. Replace each 0.
hint: base_url, line 1: port = PORTS[runner]
hint: base_url, line 2: return "http://localhost:" + str(port) + "/v1"
---
# Same engine, different packaging

⏱️ About 15 minutes

> **Warm-up:** you've used LM Studio and Lemonade. What do you think is actually *different* between them, and what is the same?

Most local runners are wrappers around the same few engines:

| Runner | What it is | Engine(s) | API port (default) |
|---|---|---|---|
| **llama.cpp** | The C/C++ engine itself. `llama-cli` to chat in a terminal, `llama-server` for an API with a small web UI. | itself | 8080 |
| **LM Studio** | Desktop app: model browser, chat UI, server, `lms` command line tool. Closed source, free. | llama.cpp (+ MLX on Macs) | 1234 |
| **Ollama** | Command line + background service, its own model library (`ollama run qwen3:8b`). Open source. | its own engine built on GGML (llama.cpp's library) | 11434 |
| **Lemonade** | AMD's open-source local server, aimed at Ryzen AI NPUs and Radeon GPUs. | llama.cpp (Vulkan/ROCm), ONNX Runtime for NPUs | see its docs |
| **vLLM**, **SGLang** | High-throughput servers for many users at once. Mostly NVIDIA, some ROCm support. Use safetensors, not GGUF. | their own | 8000 |

What really differs: model management, how settings are exposed, which GPU backends are bundled, and update speed. The same GGUF with the same settings gives very similar output and speed in all llama.cpp-based runners. When a brand-new model architecture appears, **llama.cpp supports it first**, and the wrappers follow when they update their bundled copy.

All of them speak the **OpenAI-compatible API**: the same HTTP requests work against any of them, only the address changes. That's why other tools (editors, agents, scripts) can use "your local model" without caring which runner you chose.

On NixOS, nixpkgs has `lmstudio`, `ollama` (plus `services.ollama` with an `acceleration` option) and `llama-cpp`. Version numbers in nixpkgs can lag behind upstream; `nix search nixpkgs llama-cpp` shows what you'd get.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `"lmstudio": 1234,` | | one pair in the dictionary: name → port. Numbers have no quotes. |
| `PORTS[runner]` | "ports at runner" | the port for that runner |
| `str(1234)` | "string of 1234" | turns the number into text, so `+` can glue it |
| `"a" + "b"` | | glues texts |

### 👀 Worked example

```python
FLOORS = {"kitchen": 0, "office": 3}

def room_sign(room):
    floor = FLOORS[room]
    return "Go to floor " + str(floor) + "!"

print(room_sign("office"))   # Go to floor 3!
```

`FLOORS["office"]` is 3, `str(3)` is `"3"`, and the three pieces are glued together.

## 🎯 Your quest

1. In `PORTS`, replace each `0` with the right default port from the table above.
2. In `base_url(runner)`, replace `return ""` with:
   - `port = PORTS[runner]`
   - `return "http://localhost:" + str(port) + "/v1"`

## Review

<details><summary>What decides an MoE model's speed, and what decides its memory?</summary>Speed: the active parameters per token. Memory: the total parameters.</details>
<details><summary>Roughly how fast can a 4.9 GB model generate on a 384 GB/s GPU?</summary>At most about 384 / 4.9 ≈ 78 tokens/s, in practice 60–80% of that.</details>
